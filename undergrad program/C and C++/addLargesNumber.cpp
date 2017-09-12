/*
This program reads two large number from DATA1 and outputs is store in another files called DATA.in.
program was tested in turbo C++, also codeblocks. Results was compared with python calculator.
*/


#include <iostream>
#include <fstream>
#include<math.h>

using namespace std;
int n = 0;
int m = 0;

void zero(int*a)
{
         for(int i = 0;i<3000;i++)
        a[i]=0;
}
     
     

void zero(int*a,int*b)
{
    for(int i = 0;i<3000;i++)
        a[i]=b[i]=0;
}


void rebuild(int* a)
{
    int temp[3000];
    zero(temp);

    int delta = fabs(m-n);//k1 -dim a
    for(int i = delta;i<n+delta;i++)
        {
            temp[i] = a[i-delta];
            a[i-delta] = 0;
        }
        a = temp;
    n += delta;
}

void rebuildS(int* a)
{
    int temp[3000];
    zero(temp);

    int delta = abs(m-n);//k1 -dim a
    for(int i = delta;i<m+delta;i++)
        temp[i] = a[i-delta];
        a = temp;
    m += delta;
}


void citirea(int* ar){
    ifstream f;
    f.open("data1.in");
    if(f.is_open())
    {
    char data;
    while (f>>data){
    ar[n++] = data;
    }
    }else cout<<"Erroare\n";
    f.close();
}

void citirea_(int* ar){
    ifstream f("data2.in");
    if(f.is_open())
    {
    int data;
    while (f>>data){
    ar[m++] = data;
    }
    }else cout<<"Erroare\n";
    f.close();
}




void adunarea(int*a, int* b)
{
    int transport = 0;
    int sum;

    for(int i = n;i>1;i--)
    {
        sum = a[i]+b[i]+transport;
        if(sum >9)
        {
            transport = (sum)/10;
            sum %=10;
          }
          a[i] = sum;

    }


}



int main()
{
    int a[3000],b[3000];
    zero(a,b);

    citirea(a);
    citirea_(b);

    if(n > m)
        rebuildS(b);

    else if(m > n)
         rebuild(a);
         adunarea(a,b);


ofstream rez;
rez.open("data.out");
for(int i = 0;i<m;i++)
if(a[i]!= 0)
   rez<<a[i];
rez.close();
cin.get();
  return 0;
}
