#include<ctype.h>
//#include<graphics.h>
#include<conio.h>
#include<math.h>
#include<dos.h>
#include<stdio.h>
#include<stdlib.h>

int xmax =640;// getmaxx();
int ymax =380;// getmaxy();
const int greater =215;// p/u Vmax
const int  lowest = 10; // p/u vmin

float r,h;//???
int i;

void meniu(float ,float ,int );
void MeBis_e(float , float ,float ,float);
void MeBis(float , float ,float);
void Co(float , float , float );
void Co_eps(float , float , float,float,float,float );
void modeleazaGrafic(float* ,int ,const float* ,const float* ,const float* , const float* );
void axay(const float* ,const float* );
void axax(int,const float* ,const float* );
void normare(float* ,int* ,float* ,float*);
void calcul(float ,float , float* );
void grafica();
float f(float);




int main()
{ grafica();

 int linie0,n;
 float y[3000];
 float a,b,vmax,vmin;
 char ch;


while(1)
{
 printf("a= ");
 scanf("%f",&a);

 printf("b= ");
 scanf("%f",&b);

 printf("\nn= ");
 scanf("%d",&n);
 meniu(a,b,n);

 calcul(a,b,y);
 normare(y,&linie0,&vmax,&vmin);
 printf("apasa Orice buton...");
 getch();
 grafica();
// modeleazaGrafic(y,linie0,&a,&b,&vmax,&vmin);
 //linerel(0,(int)y[0]);

 printf("\nDatele Noi\n");
 getch();
// closegraph();
}

   return 0;

}
/***********************************/
void grafica(){
int gd=DETECT, gm;
initgraph(&gd, &gm, "" );
//initwindow(xmax,ymax, " Miscare ");
setcolor(15);
}


float f(float x)
{
 return x*x*x;

}


void calcul(float a,float b, float* z)
{
h = fabs(b-a)/(xmax-1);
for(i=0;i<xmax;i++)
 z[i]=f(a+(i-1)*h);

}

void normare(float* z,int* l0,float* vmax,float* vmin)
{

float delta, deplas;
*vmax= *vmin = z[0];
for(i = 0;i<xmax;i++){
if(z[i]> *vmax) *vmax=z[i];
if(z[i]<*vmin) *vmin=z[i];
 }
delta = (*vmax-*vmin)/(ymax);
deplas = 0-*vmin;
*l0=(int)floor(ymax-deplas/delta);//rotungeste
if(*vmin > 0) *l0=greater;
if(*vmax < 0) *l0=lowest;

for(i =0;i<xmax;i++)
z[i]=ymax-(z[i]+deplas)/delta;


}

void axax(int linie0,const float* a,const float* b)
{
 setcolor(11);
 char s[48];
 outtextxy(getmaxx()-15,getmaxy()-10,"X");
 line(20,linie0,getmaxx()-20,linie0);
 h=(*b-*a)/2;
 for(int i=0;i<2;i++)
 {
  fillellipse(20+i*200,linie0,2,2);//300
  r = *a+i*h;
  sprintf(s,"%2.1f",r);  //str(r); echivalent
  outtextxy(20+i*190,linie0+10,s);//290


//  line((int)fabs(r),

  free(s);
 }

}
void axay(const float* vmax,const float* vmin)
{
 setcolor(14);
 outtextxy(10,10,"Y");
 h=(*vmax-*vmin);
 char s[20];
 for(int i=0;i<1;i++){
 fillellipse(20,10+i*200,2,2);//400
 r=*vmax-i*h;
/* snprintf(s,sizeof(s),"%2.1f",r);  //str(r); echivalent */
  sprintf(s,"%2.1f",r);
 outtextxy(20,10+i*200,s);//400
 free(s);
}
line(20,10,20,getmaxy()-65);
}



void modeleazaGrafic(float* y,int linie0,const float* a,const float* b,const float* vmax, const float* vmin)

{
 rectangle(1,1,getmaxx(),getmaxy());
 setcolor(11);
 axay(vmax,vmin);
 axax(linie0,a,b);

//line(linie0,(int)fabs(linie0-y[0]),(int)fabs(a-b-linie0),(int)fabs(y[0]-y[1]-linie0));//Here look moveto(linie0,linie0);linerel((int)a,(int)y[0]);

 for(i=0;i<xmax;i++){
 putpixel(i+20,10+(int)floor(y[i]),15);
 outtextxy(20,260,"Alt interval (D)a / (N)u ");//460

}
}

/***************************************/
void MeBis(float a, float b,float n){
 float  c;

 for(int i=0;i<n;i++)
 {
  c=(a+b)/2;
  printf("i= %3d \tx= %8.4f \tf(x)= %8.4f \n",i,c,f(c));
   if( f(c)==0) break;
   else if(f(c)*f(a)>0) a=c;
   else b=c;
 }
}

void MeBis_e(float a, float b,float n,float epsilon)
{
 float c;
 do
 {
  c=(b+a)/2;
  printf("x= %8.4f \tf(x)= %8.4f \n",c,f(c));
  if( f(c)==0) break;
 if(f(c)*f(a)>0)a=c;
   else b=c;
  }while( fabs(b-a) <epsilon);
}

void Co(float a, float b, float n)
{
 int i=0;
 float x,e;
 float c = a - (f(a))/(f(b)-f(a))*(b-a);
 if(f(c)*f(a)>0){
  e=b;
  x = a;
}else{ e=a; x=b; }

for(;i<n;i++){
  x = x-(f(x))/(f(e)-f(x))*(e-x);
  printf("%d %2.1f f= %2.1f\n",i,x,f(x));
 }

}

void Co_eps(float a, float b, float n,float eps,float Msup, float minf)
{
    float x,e,xnou,xvechi;
    x = a-(f(a))/(f(b)-f(a))*(b-a);
    if(f(x)*f(a)>0)
    {
                   e=b;
                   xnou=a;
    }else{
          e=a;
          xnou=b;
          }

 do{
                   xvechi = xnou;
                   xnou = xvechi - (f(xvechi))/(f(e)-f(xvechi))*(e-xvechi);
                   printf("x=%2.1f   f(x)= %2.1f\n",xnou,f(xnou));
   }while((fabs(Msup-minf)/minf*(xnou-xvechi))<eps);


}


/***************************************/

void meniu(float a,float b,int n)
{


 int ch;
 printf("1-bisectie pe [%1.3f,%1.3f]\n2-bisectie pe [%1.3f,%1.3f] cu exactitatea epsilon \n",a,b,a,b);
 scanf("%d",&ch);

 switch(ch)
 {
  case 1:MeBis(a,b,n); break;
  case 2:{printf("epsilon: ");float eps;
          scanf("%f",&eps);
          MeBis_e(a,b,n,eps);
          }break;
  case 3:/*clrscr();*/ printf("Metoda coardelor Pe [%1.3f,%1.3f] p/u %d segmente \n ",a,b,n);
         Co(a,b,n);break;
  case 4:{
       float eps,Mi,mif;
       printf("\nIntroduceti Mi\n");
       scanf("%f",&Mi);
       printf("\nIntroduceti mif\n");
       scanf("%f",&mif);
       printf("\nIntroduceti epsilon\n");
       scanf("%f",&eps);
       /*clrscr(); */printf("Metoda coardelor Pe [%1.3f,%1.3f] p/u %d segmente egal cu [%2.1f,2.1f]\n ",a,b,n,Mi,mif);
      Co_eps(a,b,n,eps,Mi,mif);}break;


 default:printf("Alegerea %c, Nu exista Larevedere ",ch);

 }

}
/***************************************/



