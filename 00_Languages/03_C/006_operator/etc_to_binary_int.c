#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int* uint_to_binary(unsigned int num, int *result_arr){
    int binary_num = 0;
    int i = 0;
    while (num != 0) {
        binary_num += (num & 1)*pow(10, i);
        num >>= 1;
        i++;
    }
    result_arr[0] = binary_num;
    result_arr[1] = i + 1;
    return result_arr;
}

int main() {
    int num = -23;
    int result_arr[2];
    to_binary_int(num, result_arr);
    int digits = result_arr[1];
    char *result_str = (char*)malloc(digits * CHAR_BIT);
    sprintf(result_str, "%d", result_arr[0]);
    printf("%s\n", result_str);
    free(result_str); // 보통은 프로세스가 종료되면 운영체제에서 자동으로 메모리를 해제해줌
    return EXIT_SUCCESS;
}

// 음수인 경우 해결 필요