#include <iostream>
#include <queue>
#include <set>
#include <math.h>

using namespace std; // Cînd folosim VS 2008/2012/2013, sau codeblocks


typedef pair<double, double> point; //Definim tipul punct ca perechea de două uple.
#define x first
#define y second

// structuri Arc, Event și segment
struct arc;
struct seg;

struct event {
   double x;
   point p;
   arc *a;
   bool valid;

   event(double xx, point pp, arc *aa)
      : x(xx), p(pp), a(aa), valid(true) {}
};

struct arc {
   point p;
   arc *prev, *next;
   event *e;

   seg *s0, *s1;

   arc(point pp, arc *a=0, arc *b=0)
    : p(pp), prev(a), next(b), e(0), s0(0), s1(0) {}
};

vector<seg*> output;  // Masiv de segmente care urmează fi afisat la sfărsit

struct seg {
   point start, end;
   bool done;

   seg(point p)
      : start(p), end(0,0), done(false)
   { output.push_back(this); }

    // marcarea segmentului și setarea sfășitului segmentului.
   void finish(point p) { if (done) return; end = p; done = true; }
};

arc *root = 0; //Primul item din lista parabolică

// Prototipul funcților
void process_point();
void process_event();
void front_insert(point  p);

bool circle(point a, point b, point c, double *x, point *o);
void check_circle_event(arc *i, double x0);

bool intersect(point p, arc *i, point *result = 0);
point intersection(point p0, point p1, double l);

void finish_edges();
void print_output();

// "Mai mare ca" pentru schimbarea ordinei în lista de priorități
struct gt {
   bool operator()(point a, point b) {return a.x==b.x ? a.y>b.y : a.x>b.x;}
   bool operator()(event *a, event *b) {return a->x>b->x;}
};

// Mărginele
double X0 = 0, X1 = 0, Y0 = 0, Y1 = 0;
