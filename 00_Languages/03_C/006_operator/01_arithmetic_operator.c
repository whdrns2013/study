#include <stdio.h>
#include <stdlib.h>
#include <float.h>

void overflow();
void zero_denominator();
void byebye_remain();
void float_vs_int();
void solo_calc();

int main() {

    // 더하기, 빼기, 곱하기, 나누기  
    int i = 5;
    printf("i + 5 = %d\n", i + 5);
    printf("i - 5 = %d\n", i - 5);
    printf("i * 5 = %d\n", i * 5);
    printf("i / 5 = %d\n", i / 5);

    // 나눗셈의 나머지
    int j = 6;
    printf("j %% 5 = %d\n", j % 5);

    // 양수부호 및 음수부호
    int a = +1;
    int b = -1;
    printf("a + b = %d\n", a + b);

    // 증감 연산자 ++ --
    int c = 10;
    int d = c++;
    printf("d = %d, c = %d\n", d, c);

    int e = 10;
    int f = ++e;
    printf("f = %d, e = %d\n", e, f);

    int g = 10;
    int h = c--;
    printf("g = %d, h = %d\n", g, h);

    int k = 10;
    int l = --e;
    printf("k = %d, l = %d\n", k, l);

    overflow();
    zero_denominator();
    short t = 32767;
    printf("%d\n", t / 0);

    byebye_remain();

    float_vs_int();

    solo_calc();

    return EXIT_SUCCESS;
}

void overflow(){

    short i = 32767;
    printf("%d\n", i + 1);

    float f = FLT_MAX;
    printf("%f\n", f * 2.0f);

    float fm = FLT_MIN;
    printf("%f\n", fm / 10e+10);
}

void zero_denominator(){
    short i = 32768;
    printf("%d\n", i / 0);
}

void byebye_remain() {
    int a = 10;
    int b = 3;
    printf("a / b = %d\n", a / b);
}

void float_vs_int() {
    int a =1;
    printf("a * b = %f\n", a * 1.5);
}

// 단항 연산자
void solo_calc(){
    int x = 5, a, b;
    a = ++x * x--;
    b = x * 10;
    printf("a = %d, b = %d, x = %d\n", a, b, x);

    int y = 5, c, d;
    c = y-- * ++y;
    d = y * 10;
    printf("c = %d, d = %d, y = %d\n", c, d, y);
}