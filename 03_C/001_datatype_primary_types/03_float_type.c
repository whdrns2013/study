#include <stdio.h>
#include <float.h>

void datatype_float();

void main() {
    datatype_float();
}

void datatype_float() {

    // 표현 범위
    float min_float = FLT_MIN;
    float max_float = FLT_MAX;
    printf("float 자료형의 범위(f : 부동소수 표기) : %f, %f\n", min_float, max_float);  // 부동소수형 표기법
    printf("float 자료형의 범위(e : 지수 표기) : %e, %e\n", min_float, max_float);  // 지수형 표기법
    printf("float 자료형의 범위(g : 일반 표기) : %g, %g\n", min_float, max_float);  // 일반 표기법. 어떤 값이 출력될지 모를 때, 가장 "알아서 잘" 깔끔하게 보여주는 방식.
    double min_double = DBL_MIN;
    double max_double = DBL_MAX;
    printf("double 자료형의 범위(f : 부동소수 표기) : %f, %f\n", min_double, max_double);
    printf("double 자료형의 범위(e : 지수 표기) : %e, %e\n", min_double, max_double);
    printf("double 자료형의 범위(g : 일반 표기) : %g, %g\n", min_double, max_double);  // 일반 표기법
    long double min_long_double = LDBL_MIN;
    long double max_long_double = LDBL_MAX;
    printf("long double 자료형의 범위(f : 부동소수 표기) : %lf, %lf\n", min_long_double, max_long_double); // 제대로 표현 불가
    printf("long double 자료형의 범위(e : 지수 표기) : %le, %le\n", min_long_double, max_long_double);
    printf("long double 자료형의 범위(g : 일반 표기) : %lg, %lg\n", min_long_double, max_long_double);

    // unsigned
    printf("\n=========== 실수형의 sign unsign ===========\n");
    printf("C언어에서 실수형은 unsigned 형이 없다.\n");
    printf("실수형은 크게 세 부분으로 나뉜다.\n");
    printf("(1) 부호 비트 : 1비트를 사용해 이 숫자가 양수(+)인지 음수(-)인지를 명확하게 구분한다.\n");
    printf("(2) 지수부 : 수의 크기(자릿수)를 나타낸다.\n");
    printf("(3) 가수부 : 수의 정밀도(실제 숫자)를 나타낸다.\n");
    printf("==> 실수형은 이미 '부호'를 담당하는 비트(Sign bit)가 구조적으로 분리되어있다.\n");
    printf("=========== 실수형의 sign unsign ===========\n\n");

    // 크기
    float f;
    printf("float 의 size : %d\n", sizeof(f));

    double d;
    printf("double 의 size : %d\n", sizeof(d));

    long double ld;
    printf("long double 의 size : %d\n", sizeof(ld));

}