#include <stdio.h>
#include <stdlib.h>

// 전역변수 : 
// 지역변수 : 블럭 안에서
// 블럭 안에서는 해당 블럭의 지역변수가 우선된다.
int a = 1;

void local_function(){
    int a = 3; // 지역변수
    printf("local function 에서의 a : %d\n", a);
};

int main() {
    printf("전역변수 a : %d\n", a);
    local_function();
    int a = 2;
    printf("main 에서의 a : %d\n", a);
    return EXIT_SUCCESS;
}
