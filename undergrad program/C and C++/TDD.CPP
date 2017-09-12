#include<stdio.h>
#include "gen.h"

int copyOnecolumn(const int source[100],int dest[][100],int&f,int&n);
void findSol(const int a[][100], int *solution,int& n);

int main()
{
    int a[100][100],b[100][100];
    int n=10;
    generated(a,n);
    generated(b,n);



    afisare(a,n);
    afisare(b,n);

    int sol[100]={1,1,1,1,1,1,1,1,1,1,1};


   findSol(a,sol,n);
    //copyFrom(a,)

}

int copyOnecolumn(const int source[100],int dest[][100],int&f,int&n)
{
    int i;
    for(i=0;i<n;i++) dest[f][i]=source[i];
}

void findSol(const int a[][100], int *solution,int& n)
{
 //   copy(a.begin(),)
    int temp[100][100];
    int i;
    float deterxyn,det=determinant(n,temp);

 for(i=0;i<n;i++) copyFrom(a,temp,i,n);//operam cu matricea temporara

  i=0;

  while(i<n-1)
  {

      copyOnecolumn(solution,temp,i,n);
      deterxyn=determinant(n,temp);
      printf("x%d=%f\n",i+1,deterxyn/(det));
      i++;
      copyFrom(a,temp,i-1,n);
  }


}
