#include<stdio.h>
#include<stdlib.h>

struct S {
    int x;
    int y;
};

// sort ascending by member x
/*int cmp (const void *a, const void *b) {
    S* aa = (S *)a;
    S* bb = (S *)b;
    return aa->x - bb->x;

}*/
int cmp (const void *a, const void *b) {
    S* aa = (S *)a;
    S* bb = (S *)b;
    return bb->x - aa->x ;//ordine descrescatoare

}

int main()
{
    S s[5]; // initialize s etc.
    s[0].x =rand();
    s[0].y = rand();
    s[1].x =rand();
    s[1].y = rand();
    s[2].x =rand();
    s[2].y = rand();
    s[3].x =rand();
    s[3].y = rand();
    s[4].x =rand();
    s[4].y = rand();


    qsort(s, 5, sizeof(struct S), cmp);
    for(int i=0;i<5;++i)
        printf("%d ",s[i].x);
}
