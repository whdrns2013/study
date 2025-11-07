#include <stdio.h>
#include <stdlib.h>

void println_str(const char* str){
    printf("%s\n", str);
};

void println_int(const char* str, int a){
    // c 언어는 함수 오버로딩을 지원하지 않음.
    printf(str, a);
};

void assignment_operator();

int main() {
    assignment_operator();
    return EXIT_SUCCESS;
}

// 대입 연산자
void assignment_operator(){
    // 대입 연산자 : 좌측 피연산자에 우측 피연산자의 값 혹은 연산의 결과값을 저장함
    // expr1 = expr2
    
}