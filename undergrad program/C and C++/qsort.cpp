#include<iostream>
#include<cstdlib>
#include<time.h>
using namespace std;

/*
de scris un program p/t sortare rapida. De completat programul cu elementele masurari timpului
*/
int a[35000];
int divide(int st, int dr);
void quickSort(int st, int dr);
void bubleSort(int length,int* b);
void assigner(int length,int* b);
void timeMeassurment(bool b = true);

int main(){
assigner(200,a);

timeMeassurment(1);
timeMeassurment(0);

        return 0;
}



int divide(int st, int dr)
{
 int i, j, val;
 val = a[ st ];
 i = st;
 j = dr;

while(i < j){
 while( (i < j) && (a[j] >= val))
     j = j - 1;
 a[i] = a[j];
 while( (i < j)&&( a[i] <= val) )
     i = i+1;

 a[j] = a[i];
}
a[i] = val;
return i;
}

void quickSort(int st, int dr)
{
    int m;
    if(st < dr){
    m = divide(st, dr);
    quickSort(st,m-1);
    quickSort(m+1,dr );

    }
}

void bubleSort(int length, int* b)
{

    int temp;
    for(int i = 0;i<length-1; i++)
        if(b[i] < b[i+1])
    {
        temp = b[i];
        b[i] = b[i+1];
        b[i+1] = temp;
    }

}
void assigner(int length,int* b)
{
    for(int i = 0; i < length; i++)
                  b[i]  = rand();

}
void timeMeassurment(bool b)
{
    switch(b)
    {
    case 1:
        {
           clock_t begin = clock();
           bubleSort(200,a);
           clock_t end = clock();
           double delta = double(end - begin)/CLOCKS_PER_SEC;
           cout<<delta;
        }
    case 0:  {
           clock_t begin = clock();
           quickSort(0,200);
           clock_t end = clock();
           double delta = double(end - begin)/CLOCKS_PER_SEC;
           cout<<delta;
        }
    }

}
