#include <stdio.h>
#include <stdlib.h>

void println_str(const char* str){
    printf("%s\n", str);
};

void println_int(const char* str, int a){
    // c 언어는 함수 오버로딩을 지원하지 않음.
    printf(str, a);
};

void something();

int main() {
    something();
    return EXIT_SUCCESS;
}

void something(){

}