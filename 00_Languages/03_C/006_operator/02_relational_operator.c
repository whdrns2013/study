#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void relational_operator();
void println(const char* str){
    printf("%s\n", str);
};

int main() {
    relational_operator();
    return EXIT_SUCCESS;
}

void relational_operator(){
    int a = 10;
    int b = 11;
    int c = 10;

    if (a == b) {
        println("a == b");
    }
    else if (a != b) {
        println("a != b");
    }

    if (b > c) {
        println("b > c");
    }
    else if (b < c ){
        println("b < c");
    }

    if ((a >= c) && (b > a)) {
        println("a >=c and b > a");
    }

}