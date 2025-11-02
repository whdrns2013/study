#include <stdio.h>
#include <stdlib.h>

void printf_test();
void int_printf();
void char_printf();
void string_printf();
void float_printf();
void printf_edit();

int main() {
    printf_test();
    int_printf();
    char_printf();
    string_printf();
    float_printf();
    printf_edit();
    return EXIT_SUCCESS;
}

void printf_test(){
    int a = 66;
    char c = 66;
    char* s = "문자열 입니다.";
    printf("%c 의 ASCII 코드값은 %d\n", c, c);
    printf("정수를 표현할 때에는 %%d를 사용하여 표현한다. : %d\n", a);
    printf("문자열은 %%s 라는 양식 변환 기호를 사용한다 : %s\n", s);
}

void int_printf(){
    // 기본적인 변환기호  
    int ten = -10;
    printf("10진수 -10을 10진수로 출력하면 : %d\n", ten);
    printf("10진수 -10을 부호 없는 10진수로 출력하면 : %u\n", ten);
    printf("10진수 -10을 부호 없는 8진수로 출력하면 : %#o\n", ten);
    printf("10진수 -10을 부호 없는 16진수로 출력하면 : %#x\n", ten);
    printf("10진수 -10을 부호 없는 16진수로 출력하면 : %#X\n", ten);
    printf("10진수 -10을 부호 없는 short int로 출력하면 : %hu\n", ten);
    printf("10진수 -10을 부호 없는 long int로 출력하면 : %lu\n", ten);

    // 수식 또는 함수 등을 함께 넣을 수도 있다.  
    printf("10 + 20 의 결과는 16진수로 %#X 입니다.\n", 10 + 20);
}

void char_printf(){
    printf("%c\n", 'A');
    printf("%c\n", 65);
    // 비정상적인 경우
    printf("%c\n", "한 문자가 아닌 문자열이 들어가는 경우");
    printf("%c\n", 1545348573);
}

void string_printf(){
    printf("%s\n", "기본적인 문자열 출력");
    printf("%s\n", "중간에 널값이 \0 들어간 문자열");
    // printf("%s\n", 'r'); // 정상적으로 작동하지 않음
    // printf("%s\n", 123); // 정상적으로 작동하지 않음
}

void float_printf(){
    printf("%f\n", 12.34f);
    printf("%f\n", 31.4e-1);
    printf("%e\n", 123.45678);
    printf("%E\n", 123.45678e-6);
    printf("%g\n", 123.45678);
    printf("%G\n", 123.45678e-6);
}

void printf_edit(){
    // 정수형
    printf("|%d| \n", 123);
    printf("|%d| \n", -123);
    printf("|% d| \n", 123);
    printf("|% d| \n", -123);
    printf("|%+d| \n", 123);
    printf("|%5d| \n", 123);
    printf("|%-5d| \n", 123);
    printf("|%05d| \n", 123);
    printf("|%+5d| \n", 123);
    printf("|%+05d| \n", 123);

    // 실수형
    printf("|%6.1f| \n", 123.456);
    printf("|%2.1f| \n", 123.456);
    printf("|%2.9f| \n", 123.456);
    printf("|%07.2f| \n", 123.456);
    printf("|%10f| \n", 123.456);
    printf("|%10.1f| \n", 123.456);
    printf("|% 10.4f| \n", 123.456);
    printf("|%+10.4f| \n", 123.456);
    printf("|%10.4g| \n", 123.456);

    // 지수형
    printf("|%10.4e| \n", 123.456);
    printf("|%10.3e| \n", 123.456);
    printf("|% 10.4e| \n", 123.456);
    printf("|%+10.4e| \n", -123.456);
}