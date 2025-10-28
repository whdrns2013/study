#include <stdio.h>

void datatype_enumerate();

void main() {
    datatype_enumerate();
}

void datatype_enumerate() {
    // enum 기본 사용
    enum sample {ENUM1, ENUM2, ENUM3};

    // enum의 각 이름에는 0부터 +1씩 증가되는 정수값이 할당된다.
    enum day {SUN, MON, TUE, WED, THU, FRI, SAT};
    printf("%s의 값 = %d\n", "SUN", SUN);
    printf("%s의 값 = %d\n", "MON", MON);
    printf("%s의 값 = %d\n", "SAT", SAT);

    // 특정 이름에 특정 값을 지정할 수 있음
    // 이후엔 지정한 특정 값으로부터 +1씩 된다.
    enum fruit {APPLE, BANANA, CHOCOLATE=10, DOTORI};
    printf("%s의 값 = %d\n", "APPLE", APPLE);
    printf("%s의 값 = %d\n", "BANANA", BANANA);
    printf("%s의 값 = %d\n", "CHOCOLATE", CHOCOLATE);
    printf("%s의 값 = %d\n", "DOTORI", DOTORI);

    // enum 데이터타입은 코드성으로 관리하는 데이터에 대해 쉽게 표현할 수 있다.
    enum USE_YN {YES=1, NO=0};
    int user_a_active_yn = YES; // 이렇게
    printf("컴파일이 될 떄 %s는 %d로 치환된다.\n", "YES", YES);

    // 특정 enum에 대한 이름값이 궁금할 경우, 별도 매핑테이블을 만들어줘야 한다.
    enum TAKE_OUT_YN {TAKEOUT=1, FOR_HERE=0};
    const char* take_out_array[] = {
        "TAKEOUT",
        "FOR_HERE"
    };
    int idx = 0;
    printf("%d번 인덱스의 이름값 : %s", idx, take_out_array[idx]);

    // enum에 할당된 값이 충돌되는 경우
    enum ABC {A=1, B=0, C};
    printf("%s의 값 = %d\n", "A", A);
    printf("%s의 값 = %d\n", "B", B);
    printf("%s의 값 = %d\n", "C", C);
    printf("새로이 할당된 이름값으로 덮어쓰여진다.\n");

    // size of
    enum SMALL_ENUM {a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p};
    enum BIG_ENUM {q, r, s=50000000000LL};
    printf("%s의 size : %d\n", "SMALL_ENUM", sizeof(enum SMALL_ENUM));
    printf("%s의 size : %d\n", "BIG_ENUM", sizeof(enum BIG_ENUM)); // 큰 값을 저장해야 하는 경우 사이즈가 바뀐다.
}