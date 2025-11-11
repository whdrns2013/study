#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

char *to_binary_string(int num){
    // 비트 수 계산
    int bits = sizeof(int) * CHAR_BIT;

    // 이진수 문자열 : 동적 할당으로 함수 바깥에서도 메모리가 해제되지 않도록 함
    char *binary_string = (char *)malloc(bits + 1 + 2);

    for (int i = 0; i < bits; i++){
        int bit_value = num >> i & 1;                   // num의 오른쪽에서부터 i 번째 이진수
        binary_string[bits - 1 - i] = bit_value + '0';  // '+0' 을 하면 ASCII 문자 0 또는 1을 반환함
    }

    // 문자열 끝을 뜻하는 널문자 ('\0')를 추가
    binary_string[0] = '0', binary_string[1] = 'B'; // 이진수임을 표현
    binary_string[bits] = '\0';                     // 문자열의 끝을 지정

    return binary_string;
}

int main() {
    char* binary_string = to_binary_string(10);
    printf("%s", binary_string);
    free(binary_string); // malloc 함수를 사용해 할당한 메모리 공간은 반드시 free 함수를 사용해 명시적으로 메모리 해제를 해줘야 함
    return EXIT_SUCCESS;
}