#include <stdio.h>

int add(int x, int y);

int main() {
    int a = 10;
    int b = 20;
    int result = add(a, b);
    printf("%d + %d = %d", a, b, result);
}

int add(int x, int y) {
    return x + y;
}