#include <stdio.h>
#include <stdlib.h>

void something();
void nested_for();

int main() {
    // something();
    nested_for();
    return EXIT_SUCCESS;
}

void something(){
    int i, sum = 0;
    for (i = 1; i <= 10; ++i){
        sum = sum + i;
    }
    printf("1 부터 %d까지의 합 = %d\n", i - 1, sum);
}

void nested_for() {
    int a, b;
    for (a = 1; a <= 3; ++a) {
        printf("a = %d\n", a);
        for (b = 0; b < 4; b++) {
            printf("b = %d\n", b);
        }
        putchar('\n');
    }
}