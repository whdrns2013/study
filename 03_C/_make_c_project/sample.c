#include <stdio.h>

int add(x, y);

main() {
    int a = 10;
    int b = 20;
    int result = add(a, b);
    printf("%d + %d = %d", a, b, result);
}

int add(x, y) {
    return x + y;
}