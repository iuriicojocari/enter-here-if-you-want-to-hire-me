#include<graphics.h>
#include<conio.h>
#include<math.h>
#include<stdlib.h>
#include<stdio.h>
#include<dos.h>
#include<math.h>
#define n 600
#define ymax 230

void modeleazagrafic(int*,int&);
void calcVReal(float*,float&,float&);
void vmax_c(float*,float&);
void OnDisplay(float*,int*,float&);
void MeTangentei(int*,float,float,int,int&);
void meCoardelor(int*,float,float&,int&,int&);
void meCoardelor_e(int*ze,float a,float &b,float &eps,float &Minf,float&minf,int&ce);
void Metoda_Mixta_e(int* ze,float &a,float &b,float epsilon);
void MeTangentei_e(int*ze, float a, float b,float epsilon,int &M2,int m1,int &ce);
void meniu_tangenta(int* ze,float&a,float&b,int&ce);
void meniu_cooardei(int* ze,float&a,float&b,int&ce);
void meniu_principal(int* ze,float&a,float&b,int&ce)
{
  char alegere;
 textcolor(RED);
 printf("\n1-Metoda tangentei\n 2-metoda cooardei\n0-Iesire\n");
 textcolor(GREEN);

 while(1)
 {
   alegere = getchar();
   switch(alegere)
   {
   case '1': meniu_tangenta(ze,a,b,ce); break;
   case '2':meniu_cooardei(ze,a,b,ce);break;
   case '0':exit(1);
   }
 }
}



float  f(float x);
float  fd1(float x);

int main()
{
clrscr();
float a,b,ce,h,vmax;;
a=-1.7; b=-1.58;
float z[n];
int ze[n];

h=(b-a)/n;
calcVReal(z,a,h);
vmax_c(z,vmax);
OnDisplay(z,ze,vmax);
meniu_principal(ze,a,b,ce);


//meCoardelor(ze,a,b,iter,ce);
//Metoda_Mixta_e(ze,a,b,3);
getch();
closegraph();
return 0;
}
/***********************************/
void MeTangentei(int*ze, float a, float b,int iter,int &ce)
{
 float c,e,x1,x0;
 int  ee,xe,i,x0e,x1e;
c=a-(f(a))/(f(b)-f(a))*(b-a);
if(f(c)*f(a)> 0) x0 =b; else x0=a;
setcolor(GREEN);
//line(20+ee,10+ze[ee], 20+xe,10+ze[xe]);
//circle(20+ce, 240,4);
i=0;
while(i<iter){
i=i+1;
 x1=x0-f(x0)/fd1(x0);

 printf("i= %d x=%15.12f f=%15.12f\n",i,x1,f(x1));

   x0e=ceil((x0-a)/(b-a)*n);
   x1e=ceil((x1-a)/(b-a)*n);
   if(x0e<1) x0e=1;
    if (x1e<1) x1e=1;
   line(20+x0e,10+ze[x0e], 20+x1e,240);
line(20+x1e,240,20+x1e,ze[x1e]+10);
x0=x1;
circle(20+xe, 240,4);
delay(500);
//getch();
}
}


void MeTangentei_e(int*ze, float a, float b,float epsilon,int &M2,int m1,int &ce)
{
 float c,e,x1,x0;
 int  ee,xe,x0e,x1e;
 float xv,xn;
c=a-(f(a))/(f(b)-f(a))*(b-a);
if(f(c)*f(a)> 0)x0=b; else x0=a;
setcolor(GREEN);

while((M2*( (xn-xv)/(2*m1))*((xn-xv)/(2*m1)) )>epsilon){
 xv=xn;
 x1=xv-f(xv)/fd1(xv);

 printf("x=%15.12f f=%15.12f\n",x1,f(x1));

   x0e=ceil((xv-a)/(b-a)*n);
   x1e=ceil((xn-a)/(b-a)*n);
   if(x0e<1) x0e=1;
    if (x1e<1) x1e=1;
   line(20+x0e,10+ze[x0e], 20+x1e,240);
line(20+x1e,240,20+x1e,ze[x1e]+10);
circle(20+xe, 240,4);
delay(500);
//getch();
}
}

/******************************/
void meCoardelor(int*ze,float a,float &b,int &iter,int&ce){
cleardevice();
modeleazagrafic(ze,ce);
float c,e,x;
int ee,i,xe;
char *s;
c=a-f(a)/(f(b)-f(a))*(b-a);
if((f(a)*f(c)>0)) {e=b; x=a; }else {e=a; x=b; }
ce=ceil((c-a)/(b-a)*n);
xe=ceil((x-a)/(b-a)*n);
if(e==a) ee=1; else ee=n;
setcolor(GREEN);
line(20+ce,240,20+ce,ze[ce]+10);
for(i=0;i<iter;i++){
x=x-f(x)/(f(e)-f(x))*(e-x);
xe=ceil((x-a)/(b-a)*n);
line(20+ee,10+ze[ee], 20+xe,10+ze[xe]);
line(20+xe,240,20+xe,ze[xe]+10);
setcolor(GREEN+i+3);
circle(20+xe, 240,4);
delay(500);
}
sprintf(s,"%.2f",x);
outtextxy(xe,250,s);
}

//////////////////////////////
void meCoardelor_e(int*ze,float a,float &b,float &eps,float &Minf,float&minf,int&ce){
cleardevice();
modeleazagrafic(ze,ce);
float c,e,x,oldx;
int ee,i,xe;
char *s;
c=a-f(a)/(f(b)-f(a))*(b-a);
if((f(a)*f(c)>0)) {e=b; x=a; }else {e=a; x=b; }
ce=ceil((c-a)/(b-a)*n);
xe=ceil((x-a)/(b-a)*n);
if(e==a) ee=1; else ee=n;
setcolor(GREEN);
line(20+ce,240,20+ce,ze[ce]+10);
do{
oldx =x;
x=x-f(x)/(f(e)-f(x))*(e-x);
xe=ceil((x-a)/(b-a)*n);
line(20+ee,10+ze[ee], 20+xe,10+ze[xe]);
line(20+xe,240,20+xe,ze[xe]+10);
setcolor(GREEN+i+3);
circle(20+xe, 240,4);
setcolor(GREEN);
delay(500);
}while((abs(Minf-minf)/(minf)*(x-oldx))<eps);
sprintf(s,"%.2f",x);
//str(x:0:5,s);
outtextxy(xe,250,s);
}

/**************Metoda Mixta cu eps****************/
void Metoda_Mixta_e(int* ze,float &a,float &b,float epsilon)
{
float c,x,z;

c=a-(f(a))/(f(b)-f(a))*(b-a);
if(f(c)*f(a)> 0){z=b; x=a;}else{ z=a; x=b;}

while(fabs(z-x)>epsilon)
{
z=z-(f(z))/fd1(z);//z=x0
x = x - (f(x))/(f(z)-f(x))*(z-x);
printf("z=%9.5f f(z)=%9.5f x=%9.5f f(x)=%9.5f\n",z,f(z),x,f(x));
}
}

/*****************************/
float  f(float x){
 return (4*x*x*x*x+8*x*x*x-3*x*x-7*x+3);
}

float  fd1(float x){
return (16*x*x*x+24*x*x-6*x-7);
}
void calcVReal(float* z,float&a,float&h){
int i;
for(i=0;i<n;i++)  z[i]=f(a+(i-1)*h);// calculam valorile reale pe interval;
}

void vmax_c(float*z,float&vmax){
int i;
vmax=0;
for(i=0;i<n;i++)
 if(fabs(z[i])>vmax) vmax=fabs(z[i]);// determinam valoarea maxima ca modul
}

void OnDisplay(float*z,int*ze,float& vmax){
int i;
for(i=0;i<n;i++)  ze[i]=ceil(z[i]/vmax*ymax)+230;// transformam in coordonate de ecran. Axa 0X - pe mijloc!
}
/********************************/
void modeleazagrafic(int* ze,int&ce)
{
int i;
int gdriver = DETECT, gmode;
initgraph(&gdriver, &gmode, "");
 setcolor(BLUE);
 line(1,240,640,240); // axa oX
 setcolor(RED); // graficul:
 for(i=0;i<n-1;i++) line(i+20,10+ze[i],i+21,10+ze[i+1]);
 setcolor(WHITE);
 circle(20,240,4); outtextxy(20,250,"A");
 line(20+ce,240,20+ce,ze[ce]+10);//|
 circle(620,240,4); outtextxy(620,250,"B");
 line(620+ce,240,620+ce,ze[ce]+10);
}


void meniu_tangenta(int* ze,float&a,float&b,int&ce)
{clrscr();
int ch;
while(1)
{ int ch;
  printf("Metoda tangentei pe [%2.2f,%2.2f]\n1-p/u un numar de iterati\n 2-cu aproximatie epsilon 0-inapoi\n",a,b);
  scanf("%d",&ch);
switch(ch){
case 1:{int iter;
		  printf("nr de iteratie ");
		  scanf("%d",&iter);
		  modeleazagrafic(ze,ce);
		  MeTangentei(ze,a,b,iter,ce);

	 };break;
case 2:{int M2,m1;
		  float epsilon;
	  printf("\nintroduceti M2 ");
		  scanf("%d",&M2);
		  printf("Introduceti m1 ");
		  scanf("%d",&m1);
		  printf("\nIntroduceti epsilon \n");
		  scanf("%f",&epsilon);
		  modeleazagrafic(ze,ce);
		  MeTangentei_e(ze,a,b,epsilon,M2,m1,ce);//MeTangentei_e(int*ze, float a, float b,float epsilon,int &M2,int m1,int &ce)
	 }break;
case 0:meniu_principal(ze,a,b,ce);break;
default:clrscr();
 }
 }
}

void meniu_cooardei(int* ze,float&a,float&b,int&ce){
int ch;
  printf("Metoda coardei pe [%2.2f,%2.2f]\n1-p/u un numar de iterati\n 2-cu aproximatie epsilon 0-inapoi\n",a,b);
  scanf("%d",&ch);
switch(ch){
	case 1:{int iter;
		  printf("nr de iteratie ");
		  scanf("%d",&iter);
		  modeleazagrafic(ze,ce);
		  meCoardelor(ze,a,b,iter,ce);
	 };break;
	case 2:{int M2,m1;
		  float epsilon;
		  printf("\nintroduceti M2 ");
		  scanf("%d",&M2);
		  printf("Introduceti m1 ");
		  scanf("%d",&m1);
		  printf("\nIntroduceti epsilon \n");
		  scanf("%f",&epsilon);
		  modeleazagrafic(ze,ce);
		  meCoardelor_e(ze,a,b,epsilon,M2,m1,ce);
		  }break;
    case 0:meniu_principal(ze,a,b,ce);break;
default:clrscr();
 }
 }



