#include <stdio.h>
#include <stdlib.h>

void constant_char();

int main(){
    constant_char();
    return EXIT_SUCCESS;
}

void constant_char() {
    // char
    char eng = 'a';
    printf("char %s expression : %c\n", "eng", eng);
    char digit = '1';
    printf("char %s expression : %c\n", "digit", digit);
    char sign = '-';
    printf("char %s expression : %c\n", "sign", sign);
    
}