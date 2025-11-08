#include <stdio.h>
#include <stdlib.h>

void print_binary(int number, int binary_digits){
    // int a[binary_digits];
    // for (int i=0; i <= binary_digits-1; i++){
    for (int i = (binary_digits-1); i >= 0; i--){
        // a[binary_digits-1-i] = number%2;
        int result = (number >> i) & 1;
        printf("%d", result);
    }
    printf("\n");
}
void bit_operator();
void bit_masking();
void square();
void vs_logical_operator();

int main() {
    bit_operator();
    printf("\n");
    bit_masking();
    printf("\n");
    square();
    printf("\n");
    vs_logical_operator();
    return EXIT_SUCCESS;
}

void bit_operator(){
    // 포스팅 : C 언어에서 2진수 표현하기 :: https://m.blog.naver.com/tipsware/221498120704
    // 포스팅 : C 2진수 출력하기

    // & : 비트의 AND 연산
    // 둘 다 1이면 1, 그 외는 모두 0
    int a = 0B11001000;
    int b = 0B00111001;
    print_binary(a&b, 8);

    // | : 비트의 OR 연산
    // 둘 중 하나라도 1이면 1, 둘 다 0이면 0
    print_binary(a|b, 8);

    // ^ : 비트의 XOR 연산
    // 둘이 다르면 1, 같으면 0
    print_binary(a^b, 8);

    // ~ : 비트의 NOT 연산
    // 0은 1로, 1은 0으로 반전
    print_binary(~a, 8);

    // a << n : 비트의 좌측 이동
    // a의 각 비트를 n자리씩 왼쪽으로 이동
    // 빈 공간은 0으로 채워짐
    print_binary(a << 2, 8);

    // a >> n : 비트의 우측 이동
    // a의 각 비트를 n자리씩 오른쪽으로 이동
    // 빈 공간은 0으로 채워짐
    print_binary(a >> 2, 8);
}

void bit_masking(){
    // 앞 네 자리를 지우는 마스크
    // 0과 &표시를 하면 상대의 비트값이 뭐든 모두 지워지며
    // 1과 &표시를 하면 상대의 비트값이 그대로 유지된다.
    // 즉, 마스킹 되는 것
    int mask;
    mask = 0B00001111;
    int a = 0B10110011;
    print_binary(a&mask, 8);

    // 특정 비트를 1로 채우는 마스크
    // 0과 |표시를 하면 상대 비트값이 그대로 유지됨
    // 1과 |표시를 하면 연산 결과값이 1이 됨
    print_binary(a|mask, 8);

    // 특정 비트값만 반전하기
    // 0과 ^표시를 하면 상대 비트값이 1이면 1, 0이면 0으로 그대로 유지됨
    // 1과 ^표시를 하면 상대 비트값이 1이면 0, 0이면 1로 바뀜 (반전)
    print_binary(a^mask, 8);
}

void square(){
    // 비트의 이동으로 제곱 및 제곱근 계산을 할 수 있음.  

    // << : 좌측이동 : 2^n 제곱을 하는 효과
    int a = 0B00000100; // 4
    int b = a << 3;
    printf("%d\n", b);  // 4 * 2^3 = 4 * 8 = 32
    print_binary(b, 8); // 4 * 2^3 = 4 * 8 = 32

    // >> 우측이동 : 2^n 제곱근을 하는 효과
    int c = a >>2;
    printf("%d\n", c);
    print_binary(c, 8);
}

void vs_logical_operator(){
    // 논리 연산자와는 계산 결과가 다르다.
    int a = 1;
    int b = 2;

    int result_of_logical = a && b;
    printf("%d\n", result_of_logical);
    print_binary(result_of_logical, 8);

    int result_of_binary = a & b;
    printf("%d\n", result_of_binary);
    printf("a : ");
    print_binary(a, 8);
    printf("b : ");
    print_binary(b, 8);
    print_binary(result_of_binary, 8);
}