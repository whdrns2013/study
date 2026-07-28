#include <stdio.h>
#include <stdlib.h>

void get_s();
void put_s();

int main() {
    put_s();
    return EXIT_SUCCESS;
}

void get_s(){
    // char str[100];
    char* str;
    printf("입력 : ");
    gets(str);
    printf("--------------------\n");
    printf("%s", str);
}

void put_s(){

    char* str = "The Greatest Showman";
    puts(str); // *str 과 같이 포인터변수를 쓰지는 않는다.

    puts("Kings Man");   
}