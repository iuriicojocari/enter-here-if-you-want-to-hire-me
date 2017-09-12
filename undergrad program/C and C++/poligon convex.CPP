#include<stdlib.h>
#include<time.h>
#include<stdio.h>
#include<iostream>// we could use bool data type

struct punct{
int x,y,stare;
};


int Is(const int&,const int&,const int&,const int&);
void zeroState(punct* a,const int&);
int check(const punct&,const punct&,const punct&,const punct&);
float Sarus(const punct&,const punct&,const punct&);
//int overload(punct const&,punct const&);
int cooliniar(const punct&,const punct&,const punct&);
void poligon(punct*a,int&n);
void citirea(punct* a,int&n);






int main()
{
 punct a[100];
 int n=4;
 int i;
 int grafica[1000];
 int maxX,maxY;

 maxX=maxY=0;
 for(i=1;i<n;i++)
 {
     a[i].x=rand()%980;
     srand(time(NULL));
     a[i].y=rand()%980;
     a[i].stare=0;
     if(maxX<a[i].x) maxX=a[i].x;
     if(maxY<a[i].y) maxY=a[i].y;
 }


poligon(a,n);
return 0;
}


/*int cooliniar(const punct&a,const punct&b,const punct&c)
{
 if(overload(a,c)==overload(a,b)) return 1;else return 0;
} */

void zeroState(punct* a,const int&n){
int i;
 for(i=1;i<=n;i++)
  a[i].stare=0;

}

int Is(const int&l,const int&i,const int&j,const int&k)
{
    if((l!=i)&&(l!=j)&&(l!=k)) return 1;
    else return 0;
}

float Sarus(const punct&p1,const punct&p2,const punct&p)
{
    return (p1.x*p2.y+p2.x*p.y+p.x*p1.y-p2.y*p.x-p.y*p1.x-p1.y*p2.x);
}

int check(const punct& p1,const punct&p2,const punct&p3,const punct&p){
float d1=Sarus(p1,p2,p);
float d2=Sarus(p2,p3,p);
float d3=Sarus(p3,p1,p);

if((d1*d2<0)||(d1*d3 <0)) return 1;
else return 0;
}

/*int overload(punct const&a,punct const&b){
    return (a.x/b.x, a.y/b.y,0);
}*/

void poligon(punct*a,int&n){
    int i,j,k,l;
    for(i=1;i<=n-4;i++)
     for(j=i+1;j<=n-1;j++)
      for(k=j+1;l<=n;k++)
        //_____________O(n)=n^4
         for(l=j+1;l<=n;l++)
            if(Is(l,i,j,k)&&(!a[l].stare))
                if(check(a[i],a[i+1],a[i+2],a[i+3])) a[i].stare=1;

}

void citirea(punct* a,int&n)
{

    int i;
    FILE *f=fopen("pologon.in","r+");
    fscanf(f,"%d",&n);
    for(i=0;i<n;i++){
        fscanf(f,"%d %d",a[i].x, a[i].y);
        a[i].stare=0;
    }
    fclose(f);
}

