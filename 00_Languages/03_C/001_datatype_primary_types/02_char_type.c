#include <stdio.h>
#include <limits.h>

void datatype_char();

void main() {
    datatype_char();
}

void datatype_char(){
    char ch1;
    ch1 = 'A'; // 홑따옴표 안에 문자
    printf("ch = '%c'\n", ch1); // %c 로 표현
    printf("'%c'의 ASCII 코드 = %d\n", ch1, ch1); // %d 문자형은 정수형으로도 표현할 수 있음
    char ch2 = 0x42;
    printf("ASCII 코드 %d의 문자 = '%c'\n", ch2, ch2); // 정수형을 문자형으로도 표현할 수 있음 (16진수)
    char ch3 = 67;
    printf("ASCII 코드 %d의 문자 = '%c'\n", ch3, ch3); // 10진수 정수형으로도 가능

    // min max
    char min_char = CHAR_MIN;
    char max_char = CHAR_MAX;
    printf("char 자료형의 범위(s) : %c, %c\n", min_char, max_char);
    printf("char 자료형의 범위(s) : %d, %d\n", min_char, max_char);
    unsigned char min_uchar = 0;
    unsigned char max_uchar = UCHAR_MAX;
    printf("char 자료형의 범위(us) : %c, %c\n", min_uchar, max_uchar);
    printf("char 자료형의 범위(us) : %d, %d\n", min_uchar, max_uchar);

    // size of
    char ch;
    printf("char 의 size : %d\n", sizeof(ch));
}