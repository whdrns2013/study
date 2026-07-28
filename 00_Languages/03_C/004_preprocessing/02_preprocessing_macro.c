#include <stdio.h>
#include <stdlib.h>

// 매크로
// 정의 : 특정 코드 패턴으로 치환되도록 정의된 명칭
// #define 으로 선언
// 자주 사용되는 명령이나 수식 또는 상수에 이를 대표하는 이름(=매크로 이름)을 붙여서 사용한다.
// (1) 매크로 상수 : #define 매크로명 상수값
// (2) 매크로 함수 : #define 매크로명(인수리스트) (수식)
// 매크로를 해제하려면 #undef

#define MACRO_VALUE 5 // 매크로 상수 (전역)
#define MACRO_FUNC(a, b) (MACRO_VALUE * (a) * (b)) // 매크로 함수 (전역)

void re_define_macro_in_block();
void after_re_define_in_block();
void inflict_macro_and_variable();
void un_define_macro();
void caution_at_using_macro();

int main(){
    int x = 10;
    int y = 20;
    printf("MACRO RESULT : %d\n", MACRO_FUNC(x, y));
    re_define_macro_in_block();
    after_re_define_in_block();
    caution_at_using_macro();
    return EXIT_SUCCESS;
}

void re_define_macro_in_block(){
    #define MACRO_VALUE 1000 // 경고가 발생(redefine 되었다는 경고), 에러는 아님.
    int x = 10;
    int y = 20;
    printf("REDEFINE_MACRO : %d\n", MACRO_FUNC(x, y)); // 뒤에서 같은 이름으로 다시 define 하면 값이 덮어씌워진다.
}

void after_re_define_in_block(){
    int x = 10;
    int y = 20;
    printf("AFTER REDEFINE : %d\n", MACRO_FUNC(x, y)); // MACRO 는 전역과 지역의 개념이 없다. 어디에서 선언되든 무조건 전역이다. 따라서 전체 프로그램 관점에서 매크로 상수와 함수 이름 관리가 중요하다.
    // 매크로는 단순히 "텍스트 치환" 만 수행한다.
    // 매크로는 기계어 번역에 앞선 전처리 단계에서 사용되는데, 이 때에 이미 값으로 치환되기 때문에 전역과 지역의 구분이 없다. 변수같은 게 아니다.
}

void inflict_macro_and_variable(){
    // int MACRO_VALUE = 5000; // --> 오류 발생
    // 표준 c 문법에서는 예외처리가 없다. 그래서 테스트 값 출력을 못함.
    int x = 10;
    int y = 20;
    printf("INFLICT WITH MACRO : %d\n", MACRO_FUNC(x, y));
}

void un_define_macro(){
    #undef MACRO_VALUE
    int x = 10;
    int y = 20;
    // printf("UNDEFINE MACRO : %d\n", MACRO_FUNC(x, y)); // -> "식별자 "MACRO_VALUE"이(가) 정의되어 있지 않습니다." 오류 발생
}

void caution_at_using_macro(){
    #define MACRO_VALUE 1000
    #define MACRO_FUNC(a, b) (MACRO_VALUE * a * b)
    int x = 5;
    int y = 15;
    printf("CAUTION AT USING MACRO [WRONG]: %d\n", MACRO_FUNC(x+5, y+5));
    // MACRO_VALUE * x + 5 * y + 5 로 번역됨
    // 1000 * 5 + 5 * 15 + 5 = (1000 * 5) + (5 * 15) + 5 = 5000 + 75 + 5 = 5080
    
    #define MACRO_FUNC(a, b) (MACRO_VALUE * (a) * (b))
    printf("CAUTION AT USING MACRO [CORRECT]: %d\n", MACRO_FUNC(x+5, y+5));
    // 원래 의도를 살리려면 괄호로 묶어줘야 한다.
    // 따라서 MACRO 함수를 사용할 때에는 적극적으로 괄호를 써주는 게 좋다.
};