#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void marking();

int main() {
    marking(87);
    return EXIT_SUCCESS;
}

char* plus_zero(int score) {
    if (score % 10 >= 5) {
        return "+";
    } else {
        return "0";
    }
}

void marking(int score){
    if (score >= 95){
        printf("%s", "A+\0");
    }
    else if (score >= 90) {
        printf("%s", "A\0");
    }
    else if (score >= 80) {
        printf("%s", "B\0");
    }
    else if (score >= 70) {
        printf("%s", "C\0");
    }
    else if (score >= 60) {
        printf("%s", "D\0");
    }
    else {
        printf("%s", "F\0");
    }
}