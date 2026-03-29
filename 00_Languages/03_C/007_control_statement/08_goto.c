#include <stdio.h>
#include <stdlib.h>

void something();

int main() {
    something();
    return EXIT_SUCCESS;
}

void another() {
    some_label:
        printf("여기로 점프했습니다.\n");
}

void something(){
    int a = 1;
    goto some_label;
    a *= 20;
    printf("%d", a);
}