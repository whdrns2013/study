#include <stdio.h>
#include <stdlib.h>
#include "source_sample.c"

// (1) 헤더파일 포함
// #include : 헤더파일을 포함한다라는 뜻
// #include <파일명> : 표준 디렉터리에서 파일을 찾는다. 표준 디렉터리란 : 
// #include "파일명" : 현재 사용중인 디렉터리나 직접 지정한 경로에서 파일을 찾음

int main(){
    printf("printf 는 <stdio.h>의 함수입니다.\n");
    char* header_sample_result = source_sample();
    printf("header sample 함수로부터 리턴받은 값입니다. : %s\n", header_sample_result);
    return EXIT_SUCCESS;
}