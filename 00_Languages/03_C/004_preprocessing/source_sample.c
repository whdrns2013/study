#include <stdio.h>

char* source_sample(){
    printf("header_sample.c 파일이 실행되었습니다.\n");
    char* return_value = "header sample 함수 리턴값";
    return return_value;
}