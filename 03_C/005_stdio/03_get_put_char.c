#include <stdio.h>
#include <stdlib.h>

void get_char();
void put_char();

int main() {
    put_char();
    return EXIT_SUCCESS;
}

void get_char(){
    char a;
    a = getchar();
    printf("-------------\n");
    printf("a : %c\n", a);

    char b = getchar();
    printf("-------------\n");
    printf("b : %c\n", b);

    char c = getchar();
    printf("-------------\n");
    printf("c : %c\n", c);
}

void put_char(){

    char a = 'A';
    putchar(a);

    // char* b = 'The Greatest Showman';
    // putchar(b);

    putchar('K');

    // putchar("Kingsman");
}