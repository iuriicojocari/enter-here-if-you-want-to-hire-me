#include<graphics.h>
#include<stdlib.h>
#include<stdio.h>
#include<dos.h>
#include<conio.h>
#include<math.h>

const int n=600, ymax=230;
float h;
//float c,e;
float vmax;
float xe,iter,i;
float z[n];
int ze[n];

void modeleazagrafic(){
int i;
int gdriver = DETECT, gmode, errorcode;
/* initialize graphics mode */
initgraph(&gdriver, &gmode, "");

setcolor(BLUE);
 // axa oX
 line(1,240,640,240);
 // graficul:
 setcolor(RED);
 for(i=0;i<n-1;i++) line(i+20,10+ze[i],i+21,10+ze[i+1]);
 circle(20,240,4); outtextxy(20,250,"A");
 circle(620,240,4); outtextxy(620,250,"B");
}

float f(float x){
//  f:=cos(x)*cos(x)-x/4;
return  (sqrt(x+sqrt(x+sqrt(x)))-12);
}

void meCoardelor(int*ze,float a,float &b,int &iter)
{
float c,e,x;
int ce,ee,i;
char *s;
c=a-f(a)/(f(b)-f(a))*(b-a);
if((f(a)*f(c)>0)) {e=b; x=a; }else {e=a; x=b; }
ce=ceil((c-a)/(b-a)*n);
xe=ceil((x-a)/(b-a)*n);
if(e==a) ee=1; else ee=n;
setcolor(GREEN);
line(20+ee,10+ze[ee], 20+xe,10+ze[xe]);
line(20+ce,240,20+ce,ze[ce]+10);
circle(20+ce, 240,4);

for(i=0;i<iter;i++){
x=x-f(x)/(f(e)-f(x))*(e-x);
xe=ceil((x-a)/(b-a)*n);
line(20+ee,10+ze[ee], 20+xe,10+ze[xe]);
line(20+xe,240,20+xe,ze[xe]+10);
circle(20+xe, 240,4);
delay(300);
}
sprintf(s,"%.2f",x);
//str(x:0:5,s);
outtextxy(xe,250,s);
}

int main(){
float a,b;
a=1; b=300; iter=5;
h=(b-a)/n;
// calculam valorile reale pe interval;
for(i=0;i<n;i++) z[i]=f(a+(i-1)*h);
// determinam valoarea maxima ca modul
vmax=0;
for(i=0;i<n;i++)
 if(fabs(z[i])>vmax ) vmax=fabs(z[i]);
// transformam in coordonate de ecran. Axa 0X - pe mijloc!
for(i=0;i<n;i++)  ze[i]=ceil(z[i]/vmax*ymax)+230;

//setwindowsize(640,480);
//setWindowTitle('FunctionDrawer');
modeleazagrafic();
meCoardelor(ze,a,b,iter);
getch();
}
