#include <stdio.h>
#include <stdlib.h>

void size_of_operator();
void comma_operator();
void type_cast_operator();
void address_operator();
void pointer_operator();
int mooksi();

int main() {
    size_of_operator();
    comma_operator();
    type_cast_operator();
    address_operator();
    pointer_operator();
    mooksi();
    return EXIT_SUCCESS;
}

// size_of
void size_of_operator(){
    // 자료형이나 특정 값을 담은 식의 메모리상 크기(바이트)를 반환
    int a = 4;
    double b = 123.42;
    printf("sizeof(a)    : %d\n", sizeof(a));
    printf("sizeof(b)    : %d\n", sizeof(b));
    printf("sizeof(10/3) : %d\n\n", sizeof(10/3));
}

// comma operator
void comma_operator(){
    // 2개 이상의 식을 하나의 식으로 묶는 연산자
    // expr1, expr2
    int a = 0, b = 4;
    printf("a + b = %d\n", a + b);
    
    // 동일한 자료형 변수를 동시에 여러 개 선언할 때나
    // for 문과 같이 한 줄에 2개 이상의 식을 표현할 필요가 있을 때 주로 사용한다.
    for (int i = 0, j = 4; i <5; i++, j--){
        printf("(%d/5)[%d, %d]\n", i+1, i, j);
    }

    // 콤마 연산식의 결과값은 마지막 식의 값이다.
    int x = 1, y = 2, z;
    z = (x = x + 1, y = y + 1);
    printf("z : %d", z);
}

// type cast
void type_cast_operator(){
    // 형변환 type cas
    // 식의 자료형을 다른 자료형으로 바꾸는 것
    // 형변환은 (1) 명시적 형변환 (2) 암묵적 형변환 두 가지가 있다.

    // (1) 명시적 형변환
    // 형변환 연산자 (typename)expr 을 이용하는 형변환
    // typename : 변환할 자료형 / expr : 변환할 식 또는 값 / 결과 : 형변환된 값
    int a = 3, b = 4;
    double c;
    c = a / b;
    printf("a / b 나눗셈 결과         : %f\n", c);
    // 대입 연산은 우측 식에서부터 계산이 됨
    // a / b = 0; (int 형)
    // c = (double) 0; :: c = 0.000000

    c = (double)a / b;
    printf("(double) a / b나눗셈 결과 : %f\n", c);
    // (double) a = 3.000000
    // 3.000000 / b = 3.000000 / 4.000000 = 0.750000
    // c = (double) 0.750000; :: c = 0.750000

    // (2) 묵시적 형변환
    // 명시적으로 형변환 연산자를 사용하지 않아도, 연산이 가능한 자료형으로 자동적으로 형변환 됨
    // ...1 정수형 승격
    // char, uchar, short, ushort 등 int 형보다 작은 자료형은 효율적인 처리를 위해 int 형 또는 uint 형으로 변환됨
    // ...2 더 큰 자료형으로 변환
    // 서로 다른 자료형이 혼재하는 식에서는 표현 범위가 더 큰 자료형으로 변환됨
    // 연산 순서에 따라 꼭 필요한 지점에서 변환된다.
}

// address operator
void address_operator(){
    int value = 100;
    int *ptr_addr;
    ptr_addr = &value;
    printf("변수 value의 값: %d\n", value);
    printf("변수 value의 메모리 주소 (%%p): %p\n", &value);
    printf("포인터 ptr_addr에 저장된 주소 (%%p): %p\n", ptr_addr);
}

// pointer operator
void pointer_operator(){
    int data = 50;
    int *p;
    p = &data;
    int retrieved_value = *p;
    *p = 100;
    printf("포인터 p가 가리키는 값: %d\n", retrieved_value);
    printf("값 변경 후 data의 값: %d\n", data);
}

#include <stdio.h>

// 함수 호출 변환 예시를 위한 함수 선언
// 이 함수는 double 타입의 인수를 받도록 정의됨
void print_double(double value) {
    printf("  [4. 함수 호출 변환] 함수가 받은 값: %.2f (double)\n", value);
}

void print_int_to_double(int a){
    printf("print int to double  : %lf\n", a);
    printf("and how about int..? : %d", a);
}

int mooksi(void) {
    char c = 10;
    int i = 50;
    float f = 20.5f;

    // 1. 확대 변환 (Promotion)
    // char c는 연산에 참여하기 전에 int로 확대 변환됩니다.
    int result_p = c + i; 
    printf("1. 확대 변환 (char + int): %d (char가 int로 변환됨)\n", result_p);
    printf("sizeof(c)        : %d\n", sizeof(c));
    printf("sizeof(i)        : %d\n", sizeof(i));
    printf("sizeof(result_p) : %d\n", sizeof(result_p));

    // 2. 일반 산술 변환 (Usual Arithmetic Conversions)
    // 확대 변환(char -> int) 후, int와 float 중 더 정밀한 float으로 통일됩니다.
    float result_a = c + f;
    printf("2. 일반 산술 변환 (char + float): %.1f (char, int 모두 float으로 변환됨)\n", result_a);
    
    // 3. 대입 변환 (Assignment Conversion)
    // 큰 double 변수에 작은 float 값을 대입하면 float이 double로 자동 확대 변환됩니다. (안전)
    double d;
    d = f; 
    printf("3. 대입 변환 (float -> double): %.2f (확대 변환)\n", d);

    // 작은 int 변수에 큰 float 값을 대입하면 float의 소수점 이하가 버려집니다. (데이터 손실)
    int small_i;
    small_i = f; 
    printf("3. 대입 변환 (float -> int): %d (축소 변환, 소수점 버림)\n", small_i);

    // 4. 함수 호출 변환 (Function Call Conversions)
    // 함수는 double을 요구하지만, float f를 인수로 전달합니다.
    // 함수 호출 시 f가 double로 묵시적 변환됩니다.
    printf("4. 함수 호출 변환 (float -> double):\n");
    print_double(f);
    double its_double = 3.14;
    print_int_to_double(its_double);

    return 0;
}