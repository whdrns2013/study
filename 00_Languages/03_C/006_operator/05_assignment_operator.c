#include <stdio.h>
#include <stdlib.h>

void println(const char* str){
    printf("%s\n", str);
};

void assignment_operator();
void complex_assignment_operator();

int main() {
    assignment_operator();
    complex_assignment_operator();
    return EXIT_SUCCESS;
}

// 대입 연산자
void assignment_operator(){
    // 대입 연산자 : 좌측 피연산자에 우측 피연산자의 값 혹은 연산의 결과값을 저장함
    // expr1 = expr2
    // expr1 : l-value : 저장공간
    // expr2 : r-value : 값
    int a = 3;
    printf("a : %d\n", a);
    
    // 대입 연산자의 결과값 = 대입되어 저장된 값이 리턴됨
    int b;
    int c = b = a;
    printf("a : %d / b : %d / c : %d\n", a, b, c);

    // 중간에 다른 자료형이 있는 경우, 원래의 값이 전달됨  
    float d = 1.5f;
    int e;
    float f = e = d;
    printf("d : %f / e : %d / f : %f\n", d, e, f);
}

// 복합 대입 연산자
void complex_assignment_operator(){
    // 2항 연산자와 대입 연산자를 결합해 사용하는 경우
    // +=, -=, *=, /=, %=, <<= ...
    // expr1 op= expr2;
    // op : + - * / % << >> & ^ |
    // 이는 곳 expr1 = expr1 op expr2; 와 같음
    int a = 10, b = 3, c = 1, d=3;

    a *= b - 1;
    b /= 2 + 3;
    c += 2;
    d ^= 2;

    printf("a : %d, b : %d, c : %d, d : %d\n", a, b, c, d);
}

