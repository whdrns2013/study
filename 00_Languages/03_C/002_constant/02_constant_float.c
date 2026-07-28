#include <stdio.h>
#include <stdlib.h>

void constant_float();

int main(){
    constant_float();
    return EXIT_SUCCESS; 
}

void constant_float(){
    // 기본적인 표현 방법
    // (1) 소수 형식으로 표현
    double decimal_format = 3.14;
    // (2) 가수와 지수 형식으로 표현 (=지수 형식)
    double exponential_format = 314e-2;
    printf("3.14 to decimal_format : %f\n", decimal_format);
    printf("3.14 to exponential_format : %f\n", exponential_format);

    // float 형과 double 형을 상수에 표현하는 방법
    // (1) float 형
    float float_value = 3.14f;
    // (2) long double 형
    long double long_double_value = 3.14L;
    printf("3.14 to float : %e\n", float_value);
    printf("3.14 to long double : %Le\n", long_double_value);
}