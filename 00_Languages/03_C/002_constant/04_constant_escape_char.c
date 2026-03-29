#include <stdio.h>
#include <stdlib.h>

void constant_escape_char();
void expression_escape_char_word();

int main(){
    constant_escape_char();
    expression_escape_char_word();
    return EXIT_SUCCESS; 
}

void constant_escape_char() {

    /*
    white space 의 정의 : 
    인쇄되거나 화면에 표시될 때 눈에 보이는 특정 기호(glyph)를 가지지 않고, 대신 빈 공간을 만들거나 커서(또는 출력 위치)를 제어하는 문자들의 집합을 의미.
    */

    char space = ' ';
    printf("%s * 4번: '%c' '%c' '%c' '%c' <end>\n", "space", space, space, space, space);

    char tab = '\t';
    printf("%s * 4번: '%c' '%c' '%c' '%c' <end>\n", "tab", tab, tab, tab, tab);

    char vertical_tab = '\v';
    printf("%s * 4번: '%c' '%c' '%c' '%c' <end>\n", "vertical_tab", vertical_tab, vertical_tab, vertical_tab, vertical_tab);

    char new_line = '\n';
    printf("%s : '%c' <end>\n", "new_line", new_line); // 줄바꿈 됨

    char carriage_return = '\r';
    printf("%s : '%c' <end>\n", "carriage_return", carriage_return); // 캐리지 리턴은 글자를 쓰는 커서를 현재 줄의 맨 앞으로 옮기는 작업을 수행합니다. 줄은 바꾸지 않으며, 줄을 덮어쓰는 효과가 있습니다. 특히 진행률 바를 업데이트 할 때 잘 쓰입니다.

    char form_feed = '\f';
    printf("%s : '%c' <end>\n", "form_feed", form_feed); // 페이지변경 됨

    char alarm = '\a';
    printf("%s : '%c' <end>\n", "alarm", alarm);
    printf("알람이 울리게 하려면 문자열에 직접 포함시키거나 \a\n");
    printf("putchar 를 통해 문자 하나를 표준출력으로 즉시 전송하는 방법이 있습니다.\n");
    putchar('\a');
    fflush(stdout);

    char null = '\0';
    printf("%s : '%c' <end>\n", "null", null); // 아무 문자도 출력 안됨

    char back_space = '\b';
    printf("%s : '%c' <end>\n", "back_space", back_space); // 작은따옴표 하나가 지워짐
}

void expression_escape_char_word() {
    printf("escape 문자를 직접 문자로 출력할 때에는\n");
	printf("escape 문자를 연속으로 두 번 사용한다. \\");
}