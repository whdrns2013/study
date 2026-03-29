#include <stdio.h>
#include <stdlib.h>

void bool_type();

int main() {
    bool_type();
    return EXIT_SUCCESS;

}

void bool_type(){
    // C 언어는 0과 0이 아닌 값으로 Bool 값을 나눈다.
    // 0 = False, 거짓. 그 외는 True, 참.
    int false_int = 0;
    int true_int = 1;

    if (true_int) {
        printf("true 는 %d 입니다.\n", true_int);
    }
    if (false_int) {
        printf("false 는 %d 입니다.\n", false_int);
    }
    if (false_int == 0) {
        printf("**false 는 %d 입니다.\n", false_int);
    }

    // 실수값도 될까?
    float true_float = 1.4f;
    if (true_float) {
        printf("float_true 는 %f 입니다.\n", true_float);
    }

    // char 형은?
    char ch = 66;
    if (ch) {
        printf("ch 는 %c 입니다.\n", ch);
    }

    // string 형은?
    char* str_true = "STRING";
    if (str_true) {
        printf("str 는 %s 입니다.\n", str_true);
    }
    
}