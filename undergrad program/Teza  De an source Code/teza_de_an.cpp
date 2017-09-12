#include "teza_de_an.h"

#include<stdio.h>

priority_queue<point,  vector<point>,  gt> points;
priority_queue<event*, vector<event*>, gt> events;


void print_output_inFile();

int main()
{
   // citirea punctelor de la tastatur
   point p;
   while (cin >> p.x >> p.y) {
      points.push(p);

      // Monitorizarea marginilor
      if (p.x < X0) X0 = p.x;
      if (p.y < Y0) Y0 = p.y;
      if (p.x > X1) X1 = p.x;
      if (p.y > Y1) Y1 = p.y;
   }
   // stabilirea marginilor
   double dx = (X1-X0+1)/5.0, dy = (Y1-Y0+1)/5.0;
   X0 -= dx;  X1 += dx;  Y0 -= dy;  Y1 += dy;

   cout<<"================================================================="<<endl;

   // procesarea listei; scoate primul element cu cea mai mică coordonata
   while (!points.empty())
      if (!events.empty() && events.top()->x <= points.top().x)
         process_event();
      else
         process_point();

    //! după ce toate punctele au fost procesate, calculează evenimentele rămase.
   while (!events.empty())
      process_event();

   finish_edges(); //! stergerea nodurilor inutile
   print_output(); //! afisarea diagramei lui Voronoi (puncte)
}

void process_point()
{
   //! scoaterea următorului punct din lista ordonată
   point p = points.top();
   points.pop();

   //! Adaugă un arc nou pentru focarul parabolic
   front_insert(p);
}

void process_event()
{

   //! trecerea la evenimentul următor
   event *e = events.top();
   events.pop();

   if (e->valid) {
      // Crează un nou segment
      seg *s = new seg(e->p);

      // Șterge arcul de la început
      arc *a = e->a;
      if (a->prev) {
         a->prev->next = a->next;
         a->prev->s1 = s;
      }
      if (a->next) {
         a->next->prev = a->prev;
         a->next->s0 = s;
      }

      // setarea extremitea segmentelor a

      if (a->s0) a->s0->finish(e->p);
      if (a->s1) a->s1->finish(e->p);



	  // Verificarea condidiției cercului nul în punctul p
      if (a->prev) check_circle_event(a->prev, e->x);
      if (a->next) check_circle_event(a->next, e->x);
   }
   delete e;
}

void front_insert(point p)
{
   if (!root) {
      root = new arc(p);
      return;
   }


   // Căutăm arcul de lungime p.y (dacă există )
   for (arc *i = root; i; i = i->next) {
      point z, zz;
      if (intersect(p,i,&z)) {
         // parabola nouă intersectează arcul i, dacă este necesar i se copie
         if (i->next && !intersect(p,i->next, &zz)) {
            i->next->prev = new arc(i->p,i,i->next);
            i->next = i->next->prev;
         }
         else i->next = new arc(i->p,i);
         i->next->s1 = i->s1;

         // crează parabola p între i și i->next
         i->next->prev = new arc(p,i,i->next);
         i->next = i->next->prev;

         i = i->next; //Pinteru i are adresa noului arc

         // Setarea extremitatea segmentului conectată cu i.
         i->prev->s1 = i->s0 = new seg(z);
         i->next->s0 = i->s1 = new seg(z);

		 // Determină dacă este posibl formarea circumcencul pentru arcul nou
         check_circle_event(i, p.x);
         check_circle_event(i->prev, p.x);
         check_circle_event(i->next, p.x);

         return; //transmiterea datelor procesate.
      }
   }

   // Caz special: Dacă punctul p nici odată nu intersectează un arc atunci îl adaugă în listă.
   arc *i;
   for (i = root; i->next; i=i->next) ; // Find the last node.

   i->next = new arc(p,i);
   // Inserează segmentu între p și i
   point start;
   start.x = X0;
   start.y = (i->next->p.y + i->p.y) / 2;
   i->s1 = i->next->s0 = new seg(start);
}

// Look for a new circle event for arc i.
void check_circle_event(arc *i, double x0)
{
   // Invalidate any old event.
   if (i->e && i->e->x != x0)
      i->e->valid = false;
   i->e = NULL;

   if (!i->prev || !i->next)
      return;

   double x;
   point o;

   if (circle(i->prev->p, i->p, i->next->p, &x,&o) && x > x0) {
      // Adaugă în lista evenimentelor.
      i->e = new event(x, o, i);
      events.push(i->e);
   }
}


// Găsește punctul cel mai din dreapta din cercumcerul care trece ptrin punctele a,b,c
bool circle(point a, point b, point c, double *x, point *o)
{
   // Determină dacă bc este mai indreapta decît ab.
   if ((b.x-a.x)*(c.y-a.y) - (c.x-a.x)*(b.y-a.y) > 0)
      return false;

   //Determinarea coordonatele circumcercului care trece prin punctele a,b,c și are centrul o.
   double A = b.x - a.x,  B = b.y - a.y,
          C = c.x - a.x,  D = c.y - a.y,
          E = A*(a.x+b.x) + B*(a.y+b.y),
          F = C*(a.x+c.x) + D*(a.y+c.y),
          G = 2*(A*(c.y-b.y) - B*(c.x-b.x));

   if (G == 0) return false;  // punctele sunt coliniare.

   //Determinarea centrului O circumcercului care trece prin acestea trei puncte.
   o->x = (D*E-B*F)/G;
   o->y = (A*F-C*E)/G;

   // coordonata x a circumcercului este egal cu coordonata max x plus raza.
   *x = o->x + sqrt( pow(a.x - o->x, 2) + pow(a.y - o->y, 2) );
   return true;
}


// funcția de mai jos determină intersecția unui punct depe parabolă cu arcul i.
bool intersect(point p, arc *i, point *res)
{
   if (i->p.x == p.x) return false;

   double a,b;
   if (i->prev) // Obținerea intersecției i->prev,i
      a = intersection(i->prev->p, i->p, p.x).y;
   if (i->next) // Obținerea intersecției i->next, i.
      b = intersection(i->p, i->next->p, p.x).y;

   if ((!i->prev || a <= p.y) && (!i->next || p.y <= b)) {
      res->y = p.y;

      // Dacă punctele verifică ecuația parabolei atunci are loc intersecția.
      res->x = (i->p.x*i->p.x + (i->p.y-res->y)*(i->p.y-res->y) - p.x*p.x)
                / (2*i->p.x - 2*p.x);

      return true;
   }
   return false;
}


// Această funcție determină coordonaele punctului unde două parabole se intersectează
point intersection(point p0, point p1, double l)
{
   point res, p = p0;

   if (p0.x == p1.x)
      res.y = (p0.y + p1.y) / 2;
   else if (p1.x == l)
      res.y = p1.y;
   else if (p0.x == l) {
      res.y = p0.y;
      p = p1;
   } else {
      // formula pătratică
      double z0 = 2*(p0.x - l);
      double z1 = 2*(p1.x - l);

      double a = 1/z0 - 1/z1;
      double b = -2*(p0.y/z0 - p1.y/z1);
      double c = (p0.y*p0.y + p0.x*p0.x - l*l)/z0
               - (p1.y*p1.y + p1.x*p1.x - l*l)/z1;

      res.y = ( -b - sqrt(b*b - 4*a*c) ) / (2*a);
   }
   // înlocuiește în ecuația parabolei
   res.x = (p.x*p.x + (p.y-res.y)*(p.y-res.y) - l*l)/(2*p.x-2*l);
   return res;
}

void finish_edges()
{
   // Advance the sweep line so no parabolas can cross the bounding box.
   double l = X1 + (X1-X0) + (Y1-Y0);

   // Extinderea segmentului pentru o nouă intersecție cu parabolă.
   for (arc *i = root; i->next; i = i->next)
      if (i->s1)
         i->s1->finish(intersection(i->p, i->next->p, l*2));
}

void print_output()
{
   // Afisarea marginelor
   cout << X0 << " "<< X1 << " " << Y0 << " " << Y1 << endl;

   // Afisarea coordonatele segmentului în patrul coloane
   vector<seg*>::iterator i; // echivalent cu foreach in java
   for (i = output.begin(); i != output.end(); i++) {
      point p0 = (*i)->start;
      point p1 = (*i)->end;
      cout << p0.x << " " << p0.y << " " << p1.x << " " << p1.y << endl;
   }
}





