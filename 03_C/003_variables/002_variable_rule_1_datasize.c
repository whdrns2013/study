#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <math.h>

void normal_situation();
void int_overflow();
void float_overflow();
void underflow();
void loss_of_precision();

int main() {
    normal_situation();
    int_overflow();
    float_overflow();
    loss_of_precision();
    return EXIT_SUCCESS;
}

void normal_situation(){
    // 데이터타입이 표현할 수 있는 범위 내라면 문제 없이 변수가 선언됨
    short int a = 100 + 1;
    short int b = 0 - 1;
    short int c = a + b;
    printf("%d, %d, %d\n", a, b, c);
}

void int_overflow(){
    // 데이터타입이 표현할 수 있는 범위를 벗어나면 오버플로라는 문제가 발생
    // 오버플로 : 계산 결과가 해당 데이터 타입이 표현할 수 있는 최대값보다 커서 올바른 값을 저장하지 못하는 현상
    // 정수형에서 오버플로가 발생하면 wrap-around 가 발생한다.
    short int a = 32767 + 1;
    short int b = -32768 -1;
    printf("%d, %d\n", a, b);

    // 이 일이 일어나는 원리는 다음과 같다.
    // short int 형은 -32768 ~ 32767 까지 총 65536 2byte(16비트)를 저장할 수 있다.
    // short int가 표현할 수 있는 최대값을 32767을 이진수로 표현하면 0111111111111111
    // 그런데 여기에 1을 더하면 1000000000000000 이 되면서 10진수로 -32768 가 되어버린다.
    // 비슷하게 -32768 은 1000000000000000 인데, 여기서 1을 빼게 되면서 0111111111111111 이 되면서 10진수로 32767이 되어버린다.
}

void float_overflow(){
    // 부동소수형에서의 오버플로는 결과 양상이 조금 다르다.
    // 부동소수형이 표현할 수 있는 최대 값보다 더 큰 값이 입력될 경우, 해당 변수에는 Inf 즉 무한대가 표시된다.
    float a = FLT_MAX;
    printf("float이 표현 가능한 최대값이 몇이더라 : %f\n", a);

    float b = FLT_MAX * 2.0f;
    printf("%f\n", b);

    // 그런데 위의 부동소수형 오버플로 테스트에서는 곱하기를 한 것을 볼 수 있다.
    // 그 이유는, 부동소수형에서는 단순 더하기를 해서는 오버플로가 일어나지 않기 때문이다.
    float c = FLT_MAX + 2.0f;
    printf("%f\n", c);

    // 이것을 좀 더 살펴보자
    // float 형, 단정밀도 부동소수점은 숫자를 c * 2^q 형태로 저장한다.
    // 여기서 c는 가수부(유효숫자)고, q는 지수이다. float은 이 유효숫자를 약 10진수 7자리 정도의 정밀도로 저장한다.
    // 예를 들어 FLT_MAX 는 3.402823 * 10^38 이라는 값을 가진다.
    // 그리고 2.0f 는 0.000000...2 * 10^38 가 된다. (소수점 아래 0이 37개)
    // 따라서 float의 유효숫자 정밀도 (소수점 이하 7자리)의 범위를 아득히 벗어난 37번째 자리에 2가 있기 때문에 이 값은 그냥 0.0f 와 동일하게 처리되어 버린다.
    // 그러므로 오버플로를 일으키려면 반올림했을 때 최소 10^32 이상(??맞나?)의 크기인 값을 더해야 한다.

    float d = FLT_MAX +  (pow(10, 32)); // 10의 32제곱
    printf("%f\n", d);

    // 그 이하가 되면 오버플로가 일어나지 않는다.
    float e = FLT_MAX +  (pow(10, 31));
    printf("%f\n", e);
}

void loss_of_precision(){
    // 이것을 바로 정밀도 손실 또는 반올림 오차라고 한다.
    // 정밀도 손실은 부동소수형 데이터타입이 표현할 수 있는 정밀도보다 더 정밀한 값을 입력받았을 때 발생하는 문제다.
    // 예를 들어 소수점 아래 6자리까지 표현이 가능한 자료형에 소수점 아래 10자리까지의 값을 넣으면, 소수점 아래 7번째 자리에서 반올림이 되고,
    // 소수점 아래 6번째 자리까지의 값만 저장하며, 그 이하의 값은 버려지게 된다.
    // 즉, 원래의 정밀도를 잃는 것이다.
    float a = 0.0123456789;
    double b = 0.0123456789L;
    printf("%f\n", a);
    printf("%d\n", b); // 여기부터
}

void underflow(){

}

