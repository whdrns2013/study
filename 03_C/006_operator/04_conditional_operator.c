#include <stdio.h>
#include <stdlib.h>

void conditional_operator();

void println_str(const char* str){
    printf("%s\n", str);
};

void println_int(const char* str, int a){
    // c 언어는 함수 오버로딩을 지원하지 않음.
    printf(str, a);
};

int main() {
    conditional_operator();
    return EXIT_SUCCESS;
}

// 조건 연산자
void conditional_operator(){
    // 조건문의 결과에 따라 대입할 값이나 실행할 수식을 선택할 수 있는 연산자
    // expr1 ? expr2 : expr3 
    // 위와 같이 표현한다.
    // expr1 : 조건식 / expr2 : 조건이 참일 때의 값 / expr3 : 조건이 거짓일 때의 값

    int a = 1;
    int b = 2;
    int max = a > b ? a : b;
    println_int("the max is %d", max);

    // 수식을 담는 경우
    int c = 1;
    int d = 2;
    c > d ? d++ : c++;
    printf("c's value : %d / d's value : %d", c, d);
}