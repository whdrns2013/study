#include <stdio.h>
#include <stdlib.h>

void scanf_int();
void scanf_float();
void scanf_with_comma();
void scanf_char_string();

int main() {
    // scanf_int();
    // scanf_float();
    // scanf_with_comma();
    scanf_char_string();
    return EXIT_SUCCESS;
}

void scanf_int(){
    int a;
    short b;
    long long c;
    printf("값을 입력해주세요 : ");
    scanf("%d", &a);
    scanf("%hi", &b);
    scanf("%llx", &c);
    printf("--------------------\n");
    printf("%d, %d, %lld\n", a, b, c);
}

void scanf_float(){
    float a;
    double b;
    scanf("%f %lf", &a, &b);
    printf("--------------------\n");
    printf("%f, %e\n", a, b);
}

void scanf_with_comma(){
    int a;
    int b;
    scanf("%d, %d", &a, &b);
    printf("--------------------\n");
    printf("%d, %d\n", a, b);
}

void scanf_char_string() {
    char a;
    char b[100];
    scanf("%c", &a);
    scanf("%s", b);
    printf("--------------------\n");
    printf("%c %s\n", a, b);
}