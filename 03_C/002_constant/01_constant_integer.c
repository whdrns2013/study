#include <stdio.h>

void constant_integer();

int main(){
    constant_integer();
    return 0;
}

void constant_integer() {
    // 10을 표현하는 방법
    printf("10진수 %d은 10진수로 %s 라고 표현합니다.\n", 10, "10");
    printf("10진수 %d은 8진수로 %s 라고 표현합니다.\n", 012, "012");
    printf("10진수 %d은 16진수로 %s 라고 표현합니다.\n", 0xa, "0xa");
    printf("10진수 %d은 16진수로 %s 라고 표현합니다.\n", -0xe9, "-0xe9");

    // unsigned
    printf("부호 없는 10진수 %d은 12진수로 %s 라고 표현합니다.\n", 0xc3u, "0xc3u");
    printf("부호 없는 10진수 %d은 8진수로 %s 라고 표현합니다.\n", 017u, "017u");
    printf("대문자로 써도 된다. : %d, %s\n", 017U, "017U");

    // long 형
    printf("long 형 10진수 %d은 10진수로 %s 라고 표현합니다.\n", -45L, "-45L");
    printf("long 형 10진수 %d은 8진수로 %s 라고 표현합니다.\n", -0x2dL, "-0x2dL");
    printf("long 형 10진수 %d은 12진수로 %s 라고 표현합니다.\n", -055L, "-055L");
    printf("소문자로 써도 되나, 1과 구분하기 어려울 수 있다. : %d, %s\n", -055l, "-055l");

    // 10진 상수
    int deci = 10;
    printf("10진수 %s 은 10진수로 %d 입니다.\n", "10", deci);
    printf("10진수 %s 은 8진수로 %o 입니다.\n", "10", deci);    // 8진수 : o (octal)
    printf("10진수 %s 은 8진수로 %#o 입니다. (8진수 형식)\n", "10", deci);    // 8진수형식 : #o
    printf("10진수 %s 은 16진수로 %x 입니다.\n", "10", deci);   // 16진수 : x (Hexadecimal)
    printf("10진수 %s 은 16진수로 %#x 입니다. (16진수 형식)", "10", deci);   // 16진수 형식 : #x

    // 8진 상수
    int octal = 010;    // 8진 상수는 앞에 0을 붙인다.
    printf("\n8진수 %s 은 10진수로 %d 입니다.\n", "10", octal);
    printf("8진수 %s 은 8진수로 %o 입니다.\n", "10", octal);    // 8진수 : o (octal)
    printf("8진수 %s 은 8진수로 %#o 입니다. (8진수 형식)\n", "10", octal);    // 8진수형식 : #o
    printf("8진수 %s 은 16진수로 %x 입니다.\n", "10", octal);   // 16진수 : x (Hexadecimal)
    printf("8진수 %s 은 16진수로 %#x 입니다. (16진수 형식)\n", "10", octal);   // 16진수 형식 : #x

    // 16진 상수
    int hexa_deci = 0x10;    // 16진 상수는 앞에 0x를 붙인다.
    printf("\n16진수 %s 은 10진수로 %d 입니다.\n", "10", hexa_deci);
    printf("16진수 %s 은 8진수로 %o 입니다.\n", "10", hexa_deci);    // 8진수 : o (octal)
    printf("16진수 %s 은 8진수로 %#o 입니다. (8진수 형식)\n", "10", hexa_deci);    // 8진수형식 : #o
    printf("16진수 %s 은 16진수로 %x 입니다.\n", "10", hexa_deci);   // 16진수 : x (Hexadecimal)
    printf("16진수 %s 은 16진수로 %#x 입니다. (16진수 형식)\n", "10", hexa_deci);   // 16진수 형식 : #x

    // unsigned 형
    int unsigned_int = 10u;    // unsigned 형은 숫자 뒤에 0을 붙인다.
    int unsigned_octal = 010u;
    int unsigned_hexadeci = 0x10u;
    printf("\nunsigned int, octal, hexadeci : %d, %d, %d", unsigned_int, unsigned_octal, unsigned_hexadeci);

    // long 형
    long int long_int = 513513613613613616L;
    printf("\nlong int : %ld", long_int);
}