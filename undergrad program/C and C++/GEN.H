#include<stdlib.h>
#include<time.h>
#include<algorithm.h>
#include<math.h>
#include<iostream.h>


void afisare(int a[][100],int &s)
{
    int i,j;
    printf("|--------------------|\n");

    for(i=0;i<s;i++){
     for(j=0;j<s;j++)
      printf("%4.1d ",a[i][j]);
    printf("\n");
    }

}

void generated(int a[][100],int &s)
{
    int i,j;

     for(i=0;i<s;i++)
        for(j=0;j<s;j++)
	     a[i][j]=rand()%12+1;



}


void citirea(int a[][100]){

}



int determinant(int size,int det[][100])  // size & row of the square matrix
{
    int temp[100][100],a=0,b=0,i,j,k;
    int sum=0,sign;  /* sum will hold value of determinant of the current matrix */

    if(size==2) return (det[0][0]*det[1][1]-det[1][0]*det[0][1]);

    sign=1;
    for(i=0;i<size;i++)  // note that 'i' will indicate column no.
    {
        a=0;
        b=0;

        // copy into submatrix and recurse
        for(j=1;j<size;j++) // should start from the next row !!
        {
            for(k=0;k<size;k++)
            {
                if(k==i) continue;
                    temp[a][b++]=det[j][k];
            }
            a++;
            b=0;
        }
        sum+=sign*det[0][i]*determinant(size-1,temp);   // increnting row & decrementing size
        sign*=-1;
    }
    return sum;
}

float determinantt(int a[][100],int&n)
{
    int i;
    float det=1;
    for(i=0;i<n;i++)
        det*=a[i][i];
        return det;
}

void TriughiMatrice(int matrix[][100],int&n)
{
int i,j,k;
float ratio;

        for(i = 0; i < n; i++)
         for(j = 0; j < n; j++)
            if(j>i){
                ratio = matrix[j][i]/matrix[i][i];
                 for(k = 0; k < n; k++)
                    matrix[j][k] -= ratio * matrix[i][k];

    }
      printf("DetMatrice triungiulara %23.4f\n",determinantt(matrix,n));
}


float TriughiMatrice_with(int matrix[][100],int&n)
{
int i,j,k;
float ratio;

        for(i = 0; i < n; i++)
         for(j = 0; j < n; j++)
            if(j>i){
                ratio = matrix[j][i]/matrix[i][i];
                 for(k = 0; k < n; k++)
                    matrix[j][k] -= ratio * matrix[i][k];

    }
   return determinantt(matrix,n);
}

int copyFrom(const int source[][100],int destination[][100],const int&coloana,int&nr)
{
    int i;
    for(i=0;i<nr;i++)
        destination[coloana][i]=source[coloana][i];
}

