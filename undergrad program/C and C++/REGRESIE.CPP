#include <graphics.h>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include<math.h>
#include<dos.h>
#define true 1
#define false 0
const int n=30; //nr max
const int Ymax = 460;
const int Xmax = 680;

typedef float mat[n+1][n+1];


void beep(){
  printf("%c ",7);
  delay(220);
 // nosound;
 }

 /************** Modelul pentru Regresia multipla *****************/

 void model(float&x,float* vx,const int&gc){
 int i;
  vx[1]=1;
  vx[2]=x;
 for(i=2;i<gc;i++) vx[i+1]=vx[i]*x;//here instead  of i=1 may be 2
 } //may crash here i+1 invalid location


/****************** procedura pentru calcul plotare ******************/
float polinom(const float&x, const float*b, int&gmax)
{
 int i;
 float y,xx;

y=b[1];
xx=1;
for(i=2;i<=gmax;i++)
{
 xx*=x;
 y+=b[i]*xx;
}
return y;
}



 /*** PROCEDURA PENTRU CALCULUL SUMELOR DIN SISTEMUL LINIAR ****/
void sume(const float&x, const float&y, mat a, float* b,const int&gc)
{
 int j,m;
 float vx[100];
 model(x,vx,gc);
for(m=1;m<=gc;m++)
 {
  for(j=m;m<=gc+1;j++)
    {
	  a[m][j]+=vx[j]*vx[m];
	  a[j][m]=a[m][j];
	}
	b[m]+=vx[m]*y;
 }
}



void kaletski(const int&n,mat a,float* b,float* x, float* anorm)
{
  int i, j, k, is, l, it;
  float s, t, fac;

   b[1]=b[1]/a[1][1];
   for(j=2;j<=n;j++)
    {
	   a[1][j] = a[1][j] / a[1][1];
	   for (i = 2; i <= n; i++){
	   if (i > j) a[i][j] = a[j][i] / a[i][i];
	   else  {
		   s = 0;
		   for (k = 1; k <= j - 1; k++) s += a[i][k] * a[k][j];
		   a[i][j] = a[i][j] - s;//Dreapta spre stinga
	   }

	   }
	   s=0;
	   for(l=1;k<=j-1;k++) s+=a[j][k]*b[k];
	   b[j]=(b[j]-s)/a[j][j];
	}

}

/***** CONSTRUIREA SOLUTILOR SISTEMULUI LINIAR ****/
void solutii(const int&n, const mat a, const float*b, float*x){
	int i,j;
	float t;
	x[n] = b[n];
	for (i = n - 1; i != 0; i--)//downto eq
	{
		t = 0;
		for (j = i + 1; j <= n; j++) t += a[i][j] * x[j];
		x[i] = b[i] - t;
	}
}



void matinvk(const mat a,const int&n,mat ainv)
{
	int ii, i, j, k;
	float b[100], x[100];
	float  s, t;

	for (ii = 1; ii <= n; ii++)
	{
		for(j=1;j<=n;j++) b[j]=0; //zerografiere
		b[ii]=1;

		b[1]=b[1]/a[1][1];
		for(j=2;j<=n;j++)
		{
			s=0;
			for(k=1;k<=j-1;k++) s+=a[j][k]*b[k];
			b[j]=(b[j]-s)/a[j][j];
		}

		ainv[n][ii]=b[n];
		for(i=n-1;i!=0;i--)
		{
		t=0;
		for(j=i+1;j<=n;j++)  t+=a[i][j]*ainv[j][ii];
		 ainv[i][ii]=b[i]-t;
		}
	}
}



/************************************************************************************
#*********************************** PRINCIPAL *************************************#
#***********************************************************************************#*/

int main()
{
int iquit;
int i, j,k;
int  errcode, gmax,gc;
int  ipx, ipy, ipy1;
float max,min,may,miy,mix;
float scx,scy,x1,y1;
float factor,temp,y;
float an,ani;
char si[50],sii[50],ssi[50],ssii[50];
mat	 a,ainv,aa;
float anorm[50],anormi[50],x[50],b[50],xx[50],yy[50];

srand(0);
clrscr();
iquit=true;
do{
printf("Gradul maxim al regresiei = ");
scanf("%d",&gmax);
if(gmax>n-1){
 clrscr();
 beep();
 highvideo();
 gotoxy(1,1);
 printf("radul maxim admins este: %.2d\n", (n-1));
 lowvideo();
 }
 }while(gmax <=n);

 gmax=gmax+1;
 printf("Factorul de eroare ");
 scanf("%f",&factor);
 factor=factor*2.0;
 clrscr();
 gotoxy(10,12);
 printf("Programul este in executie Normala \n");
 for(i=1;i<=gmax+1;i++){
   for(j=1;j<=gmax+1;j++)  a[i][j]=0;
	x[i]=0;
	}

/*Generam un polinom afectat de erori "exeprimentale"	*/
for(i=1;i<=n;i++) {
 x1=i;
 y1=x1*x1;
 y1=-12*3*x1-30*y1+2*x1*y1;
 xx[i]=x1; /*vectorul necesar pentru grafic */
 yy[i]=(y1+factor*(rand()-0.5)*sqrt(fabs(y1))); ///!!!
 }
 /*Pregatim sistemul de eciatoo pt.regresie robusta */
 gc=gmax;
  for(i=1;i<=n;i++) sume(xx[i],yy[i],a,x,gc);
 kaletski(gmax,a,x,b,anorm);//-------------
 matinvk(a,gmax,ainv);//---------------
 an=0;
 for(k=1;k<=gmax;k++)
  {
   anorm[k]=0;
   anormi[k]=0;
   for(i=1;i<=k;i++)
    {
    for(j=1;j<=k;j++)
     {
	  anorm[k]=anorm[k]+a[i][j]*a[i][j];
	  anormi[k]=anormi[k]+ainv[i][j]*ainv[i][j];
	  }
	}
}

/*Inceputul regresie robusta */
i=DETECT;
initgraph(&i,&i,"..\\bgi");
errcode=graphresult();
if (errcode == grOk) {
  cleardevice();
/* cleardeivce;*/
 max=xx[1];
 mix=xx[1];
 may=yy[1];
 miy=yy[1];
 for(i=1;i<=n;i++)
  {
  if(yy[i]<miy)  miy=yy[i];
  if (yy[i]>may ) may=yy[i];
  if (xx[i]<mix )  mix=xx[i];
  if (xx[i] > max ) max=xx[i];
  }

  scx=400/(max-min);
  scy=200/(may-mix);

  for(i=1;i<=n;i++) /*semnul "+" pt.datele experim. */
   {
    line(200+ceil(scx*(xx[i]-mix)+4),
	     250-ceil(scy*(yy[i]-miy)),
		 ceil(200+scx*(xx[i]-mix)-4),
		 250-ceil(scy*(yy[i]-miy)));
	line(ceil(200+scx*(xx[i]-mix)),
	     246-ceil(scy*(yy[i]-miy)),
		 ceil(200+scx*(xx[i]-mix)),
		 254-ceil(scy*(yy[i]-miy)));
	}

	sprintf(si,"Gradul maxim al polinomului de regresie = %.2f",(gmax-1));//str(x:0:5,s);

	outtextxy(0,320,si);
	sprintf(ssi,"Factorul de eroare este= %.2f",(factor/2));
	outtextxy(0,310,ssi);
	iquit=true;
	while(iquit==true){
	 setviewport(0,0,185,260,false);
	 clearviewport;
	 //!!!
	 do{
	 textcolor(6);
	 outtextxy(0,10,"Grd.actual al regresie= ? ");
	 gotoxy(120,1);
	 scanf("%d",&gc);
	 gc=gc+1;
	 sprintf(ssi,"%2d",gc);

	 if(gc > gmax){
	  beep;
	  clearviewport;
	  sprintf(si,"Gresit! Grd.max.=");
	  outtextxy(0,0,si);
	}
}while(gc <= gmax);

an=0;/*calculam numarul de coditionare */
ani=0; /*al matricii sist.lin.pt grad gc. */
for(i=1;i<=gc;i++){
 an=an+anorm[i];
 ani=ani+anormi[i];
 }

 an=sqrt(an); /*norma matricii a*/
 ani=sqrt(ani); /*norma matricii ain*/
 clearviewport();
 solutii(gc,a,x,b);
 outtextxy(1,15,"Coeficientii: ");
 for(i=1;i<=gc;i++){
   sprintf(sii,"a(%d)= %9.3f",(i-1),b[i]);
   outtextxy(1,20+10*i,sii);
   }
sprintf(ssi,"Nr.cond.= %9f",(ani*an));
outtextxy(0,250,ssi);
moveto(200,250);
y1=polinom(mix,b,gc);
ipx=1;
ipy=250-ceil(scy*(y1-miy));
ipy1=ipy;
moveto(200,ipy);
for(i=2;i<=400;i++){
 x1=(i-1)/scx+mix;
 y1=polinom(x1,b,gc);
 ipy=250-ceil(scy*(y1-miy));
 if((ipy<0)||(ipy>270)){
  if(ipy<0) ipy1=10;
  else ipy1=270;
  ipx=i; /*punctul iesit din scala */
  moveto(200+i,ipy);
  }else  lineto(200+i,ipy);
  }
outtextxy(200+ipx,ipy1+8,sii);
outtextxy(0,290,"Apasa <ENTER> pentru a continua regresia");
outtextxy(0,300,"Sau orice alta tasta pentru a terminare. ");
scanf("%c",&si);
if(si!="")  iquit=false;
clearviewport();
  }//end iquite
 }
closegraph();
return 0;
}














































































































































