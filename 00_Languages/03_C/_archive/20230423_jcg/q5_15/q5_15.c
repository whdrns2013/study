#include <stdio.h>

struct insa{
    char name[10];
    int age;
} a[] = {"Kim", 28, "Lee", 38, "Han", 32};

int main(){
    struct insa *p;
    p = a;
    p++;
    printf("%s\n", p -> name);
    printf("%d\n", p -> age);

    return 0;
}