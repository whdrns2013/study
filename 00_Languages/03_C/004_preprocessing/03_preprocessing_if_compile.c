#include <stdio.h>
#include <stdlib.h>

// 조건부 컴파일
// 조건에 따라 컴파일할 코드를 선택할 수 있게 하는 것  
// 아래와 같은 형식으로 사용한다.

/*
#if 조건문
코드...         // if 조건문에 해당하는 경우 실행됨
#elif 조건문
코드...         // if 조건문에 해당하지 않고, elif 조건문에 해당하는 경우 실행됨
#else
코드...         // if, elif 조건문에 모두 해당되지 않을 경우 실행됨
#endif         // 조건부 컴파일 문 종료
*/

// 이 때 조건문은 결과로 참(True, 1 이상으 정수)과 거짓(False, 0)을 가져야 한다.

#define DEBUG_MODE 0
#define HONEY_POT 1
// 4가지 경우의 수 테스트 DEBUG 1/0 HONEY_POT 1/0

int main(){
#if DEBUG_MODE
    int a = 10, b = 20;
#elif HONEY_POT
    int a = 10, b = 10;
#else
    int a = 1, b = 2;
#endif
    printf("a * b = %d", a * b);
    // DEBUG_MODE=1 HONEY_POT=0 >> a * b = 200
    // DEBUG_MODE=0 HONEY_POT=1 >> a * b = 100
    // DEBUG_MODE=1 HONEY_POT=1 >> a * b = 200
    // DEBUG_MODE=0 HONEY_POT=0 >> a * b = 2
    return EXIT_SUCCESS;
}