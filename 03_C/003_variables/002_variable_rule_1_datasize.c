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
    underflow();
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
    // 소수점 아래 6번째 자리까지의 값만 저장하며, 그 이하의 값은 버려지게 된다...? 이거 다시 검토 필요
    // 즉, 원래의 정밀도를 잃는 것이다.
    float x = 0.01234567891234;
    double y = 0.01234567891234L;
    printf("%.10e\n", x);
    printf("%.10e\n", y); // 여기부터
    // a 출력값 : 1.2345679104e-02 -- 8이 9로 반올림되고, 이하 숫자는 이진수가 이 숫자를 완벽한 완전수로 표현할 수 없기 때문에 일어나는 일
    // b 출력값 : 정밀도가 더 높기 때문에 원래 표현하려고 하는 값에 더 근접하게 저장이 가능

    // 'f' 접미사를 붙여 float 상수임을 명시
    float a = 0.0123456789f; 
    
    // 접미사가 없으면 double 상수 (L은 long double이므로 빼는 것이 맞음)
    double b = 0.0123456789; 

    printf("--- 기본 출력 (소수점 6자리) ---\n");
    printf("float  (%%e) : %e\n", a);
    printf("double (%%e) : %e\n", b);

    printf("\n--- 정밀도 지정 출력 ---\n");
    // float의 유효숫자(약 7)보다 조금 더 많이 출력 (e.g., 10자리)
    printf("float  (%%.10e): %.10e\n", a); 
    
    // double의 유효숫자(약 15)보다 조금 더 많이 출력 (e.g., 20자리)
    printf("double (%%.20e): %.20e\n", b);
}

void underflow(){
    /*
    부동소수점 연산에서 사용되는 용어.
    계산 결과의 절대값이 해당 데이터 타입이 표현할 수 있는 0에 가장 가까운 양수값보다 더 작아져서 값을 제대로 표현하지 못하는 현상.
    */
   
    // 양의 float형이 표현할 수 있는 가장 작은 수 FLT_MIN
    float flt_min = FLT_MIN;
    printf("\n%e\n", flt_min);

    // 이보다 더 정말한 값을 표현하면 언더플로우가 일어나야.. 하지만!
    float flt_min_under = flt_min / 100;
    printf("%e\n", flt_min_under);

    // 언더플로우가 일어나지 않는 이유 : 비정규 값 (Subnormal Numbers)
    /*
    FLT_MIN보다 더 작아지면, 컴퓨터는 정밀도를 조금씩 희생(유효숫자를 줄임)하면서 0에 더 가까운 값( $\approx 1.4 \times 10^{-45}$ 까지)을 표현하려고 시도합니다.
    이 영역을 **'점진적 언더플로'**라고 합니다.
    '비정규 값' 영역( $\approx 1.4 \times 10^{-45}$ )마저 벗어나는, 0에 너무 가까운 값을 만들면, 시스템은 이 값을 완전히 0.0으로 처리합니다.
    이를 "Flush-to-Zero"라고 부릅니다.
    */
   float flush_to_zero = FLT_MIN * 1.0e-8;
   printf("%e\n", flush_to_zero);
   float just_before_flush_to_zero = FLT_MIN * 1.0e-7;
   printf("%e\n", just_before_flush_to_zero);
}

