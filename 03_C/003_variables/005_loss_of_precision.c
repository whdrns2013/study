#include <stdio.h>

void loss_of_precision_min();
void loss_of_precision_max();

int main() {
    loss_of_precision_min();
    loss_of_precision_max();
    return 0;
}

void loss_of_precision_min() {
    float a = 1.0f;
    float b = 0.0000000001f;  // 10^-10, float이 표현 가능한 경계 근처의 작은 값
    float c = a + b;

    printf("a = %.6f\n", a);
    printf("b = %.6f\n", b);
    printf("a + b = %.6f\n", c);

    // 두 값의 차이 확인
    printf("a + b - a = %.6f\n", c - a);
}

void loss_of_precision_max() {
    float a = 10000000.0f;
    float b = 0.1f;
    float c = a + b;

    printf("a         = %.10f\n", a);
    printf("b         = %.10f\n", b);
    printf("a + b     = %.10f\n", c);
    printf("a + b - a = %.10f\n", c - a);
}