#include <stdio.h>
#include <stdlib.h>

void something();
void println(const char* str){
    printf("%s\n", str);
};

int main() {
    something();
    return EXIT_SUCCESS;
}

void something(){

}