#include <stdio.h>
#include <stdlib.h>

void something();

int main() {
    something();
    return EXIT_SUCCESS;
}

void something(){
    int score = 0;
    scanf("%d", &score);
    switch (score/10) {
        case 10:
        case 9: printf("학점은 A\n");
        case 8: printf("학점은 B\n");
        case 7: printf("학점은 C\n");
        case 6: printf("학점은 D\n");
        // default: printf("학점은 F\n");
    }
}