#include <stdio.h>
#include <stdlib.h>

void constant_string();

int main(){
    constant_string();
    return EXIT_SUCCESS;
}

void constant_string(){

    char str[] = "abc";
    printf("%s", str);

    printf("c에서 String 문자열 데이터는 가장 마지막에 문자열의 끝을 나타내기 위해 널 문자'\\0'가 추가된다.");
    printf("null 문자는 문자형 상수이므로 1바이트의 크기를 가진다.");
    printf("이는 문자열 상수값이 메모리에 들어갈 때 자동적으로 추가되는 것이며, ");
    printf("터미널에서 출력 결과를 보면 .. 보이지 않습니다. 널문자는 보이는 문자가 아니기 때문입니다.");
}