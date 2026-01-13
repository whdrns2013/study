#include <stdio.h>
#include <stdlib.h>

void eq(int a, int b);

int main() {
    eq(100, 101);
    eq(100, 100);
    return EXIT_SUCCESS;
}

void eq(int a, int b){
    int result = a & b;
    printf("%d\n", result);
}