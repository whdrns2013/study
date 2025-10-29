#include <stdio.h>
#include <stdlib.h>

void variable_declare();

int main() {
    variable_declare();
    return EXIT_SUCCESS;
}

void variable_declare(){
    // 기본적인 선언
    // 자료형 변수명;
    int a;
    printf("%c : %d\n", 'a', a);

    // 동일한 자료형의 여러 변수 동시에 선언
    int b, c;
    printf("%c : %d, %c : %d\n", 'b', b, 'c', c);

    // 변수를 선언하면서 값을 할당 (=초기화)
    int d = 10;
    int e = 10 - 59.9;
    printf("%c : %d, %c : %d\n", 'd', d, 'e', e);

    // 동일한 자료형의 여러 변수를 동시에 선언하면서 값도 할당
    int f = 10, g = 20, h;
    printf("%c : %d, %c : %d, %c : %d\n", 'f', f, 'g', g, 'h', h);
}
