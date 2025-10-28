#include <stdio.h>
#include <limits.h>

void datatype_char();
void datatype_int();
void datatype_size_of();

void main() {
    datatype_char();
    datatype_int();
    datatype_size_of();
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
}

void datatype_int(){
    // char
    char min_char = CHAR_MIN;
    char max_char = CHAR_MAX;
    printf("char 자료형의 범위(s) : %c, %c\n", min_char, max_char);
    printf("char 자료형의 범위(s) : %d, %d\n", min_char, max_char);
    
    // char
    char min_uchar = 0;
    char max_uchar = UCHAR_MAX;
    printf("char 자료형의 범위(us) : %c, %c\n", min_uchar, max_uchar);
    printf("char 자료형의 범위(us) : %d, %d\n", min_uchar, max_uchar);

    // short int
    short int min_short_int = SHRT_MIN; // 자료형은 short int 로 써도 되고
    short max_short_int = SHRT_MAX;     // 그냥 short로 써도 됨
    printf("short int 자료형의 범위(s) : %d, %d\n", min_short_int, max_short_int);

    // short int
    short min_ushort_int = 0;
    short max_ushort_int = USHRT_MAX;
    printf("short int 자료형의 범위(us) : %d, %d\n", min_ushort_int, max_ushort_int);

    // int
    int min_int = INT_MIN;
    int max_int = INT_MAX;
    printf("int 자료형의 범위(s) : %d, %d\n", min_int, max_int);

    // int
    int min_uint = 0;
    int max_uint = UINT_MAX;
    printf("int 자료형의 범위(us) : %u, %u\n", min_uint, max_uint); // unsigned는 %u로 써야 함
    
    // long int
    long int min_long_int = LONG_MIN;   // long int 로 써도 되고
    long max_long_int = LONG_MAX;       // long 으로 써도 됨
    printf("long int 자료형의 범위(s) : %ld, %ld\n", min_long_int, max_long_int); // 그냥 %d형이 아니라 %ld 형으로 써야 함

    // long int
    long min_ulong_int = 0;
    long max_ulong_int = ULONG_MAX;
    printf("long int 자료형의 범위(us) : %lu, %lu\n", min_ulong_int, max_ulong_int); // lu는 %lu 로 써야 함

    // long long int
    long long int min_long_long_int = LLONG_MIN;    // long long int 로 써도 되고
    long long max_long_long_int = LLONG_MAX;        // long long 으로만 써도 됨
    printf("long long int 자료형의 범위(s) : %lld, %lld\n", min_long_long_int, max_long_long_int); // 그냥 %d형이 아니라 %lld 형으로 써야 함
    
    // long long int
    long long min_ulong_long_int = 0;
    long long max_ulong_long_int = ULLONG_MAX;
    printf("long long int 자료형의 범위(us) : %llu, %llu\n", min_ulong_long_int, max_ulong_long_int); // llu는 %llu 로 써야 함

}

void datatype_size_of(){
    char ch;
    printf("char 의 size : %d\n", sizeof(ch));
    short shrt;
    printf("short int 의 size : %d\n", sizeof(shrt));
    int intig;
    printf("int 의 size : %d\n", sizeof(intig));
    long lint;
    printf("long int 의 size : %d\n", sizeof(lint));
    long long llint;
    printf("long long int 의 size : %d\n", sizeof(llint));
}