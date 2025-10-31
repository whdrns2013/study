#include <stdio.h>
#include <stdlib.h>

// 전역변수 : 
// 지역변수 : 블럭 안에서
// 블럭 안에서는 해당 블럭의 지역변수가 우선된다.

void local_function();

int main() {

    int a = 10;
    local_function();
    return EXIT_SUCCESS;
}

void local_function(){
    int a = 20;
}
