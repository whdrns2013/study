#include <stdio.h>
#include <stdlib.h>

void global_not_initialized();
void local_not_initialized();
void not_initialized_sum();
void initialized_sum();

int global_var;

int main() {
    global_not_initialized();
    local_not_initialized();
    not_initialized_sum();
    initialized_sum();
    return EXIT_SUCCESS;
}

void not_initialized_sum(){
    int i, sum;
    for (i=1; i<=10; i++){
        sum = sum + i;
    }
    printf("초기화 안됨 : 1부터 10까지의 합 = %d\n", sum);
}
void initialized_sum(){
    int i, sum = 0; // 초기화 (같은 자료형에 같은 값을 넣을 경우 이런 식으로도 초기화 가능)
    for (i=1; i<=10; i++){
        sum = sum + i;
    }
    printf("초기화 됨 : 1부터 10까지의 합 = %d\n", sum);
}

void global_not_initialized(){
    printf("not initialized global var : %d\n", global_var);
}

void local_not_initialized() {
    int local_var;
    printf("not initialized local var : %d\n", local_var);
}