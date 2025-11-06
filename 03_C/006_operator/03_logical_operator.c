#include <stdio.h>
#include <stdlib.h>

void logical_operation();
void short_circuit_evaluation();

void println(const char* str){
    printf("%s\n", str);
};

int main() {
    logical_operation();
    short_circuit_evaluation();
    return EXIT_SUCCESS;
}

void logical_operation(){
    // && : 논리곱 (AND : 두 가지 모두 참이어야 참)
    if ((8 > 3) && (9 < 2) ) println("(1) both are true");
    else println("(1) someone is false");
    if ((8 > 3) && (9 > 2) ) println("(2) both are true");
    else println("(2) someone is false");

    // || : 논리합 (AND : 둘 중 하나라도 참이면 참)
    if ((8 > 3) && (9 > 2) ) println("(1) both are true");
    if ((8 > 3) && (9 < 2) ) println("(2) someone is true");
    if ((8 < 3) && (9 < 2) ) println("(3) both are false");

    // 논리합과 논리곱은 기호를 두 개씩
    // 비트연산은 기호를 하나씩 사용한다.
    // 논리합과 논리곱은 단축평가라는 게 있다. (아래에서 설명)
    // 논리합, 논리곱은 면접관 두 명이 있고, 그 중 한 명은 단축평가를 하는 면접관, 다른 하나는 연산을 하는 면접관이라고 생각하자.
    // 단축평가를 하는 면접관을 먼저 만나고, 앞쪽의 수식이 거짓이라면 바로 돌려보낸다. 다음 면접관을 만나지 못하고 바로.
    // 비트연산은 이러한 단축평가가 없다.
    // 그래서 두개다!

    // ! : 부정 (NOT : 단항연산, 참->거짓 / 거짓->참)
    int a = 2 > 1;
    printf("a : %d\n", a);
    printf("not a : %d\n", !a);
}


// 단축평가
void short_circuit_evaluation(){
    // &&
    // 논리 곱연산에서 좌측의 피연산자가 거짓이면 전체 식의 결과는 거짓이 되기 때문에, 오른쪽 피연산자는 연산할 필요가 없다.
    // 따라서 좌측의 피연산자가 거짓이라면 오른쪽 피연산자는 연산되지 않는다.
    // 또한 오른쪽 피연산자의 수식으로 인한 오류도 방지할 수 있다.
    int a = 0;
    int b = 10;
    if (a != 0 && b / a > 10){
        println("참입니다.");
    }
    
    // 연산이 되지 않기 때문에 증감연산자 또한 계산되지 않는다.
    int c = 1;
    int d = 2;
    if (c > d && ++c == d){
        println("c의 값은 d와 같습니다.");
    }
    printf("c : %d\n", c);

    // ||
    // 논리 합연산에서는 좌측의 피연산자가 참이면 저체 식의 결과는 참이 되기 때문에, 오른쪽 피연산자는 연산할 필요가 없다.
    // 따라서 좌측이 참이면 오른쪽 피연산자는 연산되지 않으며
    // 또한 ~ 동일
    int e = 1;
    int f = 20;
    if (e == 1 && f / e > 10){
        println("참입니다.");
    }

    // 연산이 되지 않기 때문에 증감연산자 또한 계산되지 않는다.
    int g = 3;
    int h = 2;
    if (g > h && --g == h){
        println("g의 값은 h와 같습니다.");
    }
    printf("g : %d\n", g);
}