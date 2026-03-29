#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h> // bool 은 stdbool 에 정의됨

// bool : 참과 거짓을 표현하는 값  
// 거짓 : 0
// 참 : 1 또는 0이 아닌 값
// stdbool.h 표준 헤더에는 상수값 true, false 를 각각 1과 0으로 정의하고 있다.

void println(char* str){
    printf("%s\n", str);
}

int main() {
    if (1) println("if 조건문이 1일 경우의 출력입니다.");
    if (0) println("if 조건문이 0일 경우의 출력입니다.");
    if (true) println("if 조건문이 true일 경우의 출력입니다.");
    if (false) println("if 조건문이 false일 경우의 출력입니다.");
    if (2) println("if 조건문이 2일 경우의 출력입니다.");
    if (2.14f) println("if 조건문이 2.14f일 경우의 출력입니다.");
    if (2.14) println("if 조건문이 2.14일 경우의 출력입니다.");
    if ('c') println("if 조건문이 'c'일 경우의 출력입니다.");
    if ("hello") println("if 조건문이 hello일 경우의 출력입니다.");

    bool is_active;
    is_active = 1;
    if (is_active) println("활성화 되어 있습니다.");
    else println("비활성화 되어 있습니다.");
}

/*
bool.h
 * ===---- stdbool.h - Standard header for booleans -------------------------===
 *
 * Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
 * See https://llvm.org/LICENSE.txt for license information.
 * SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
 *
 *===-----------------------------------------------------------------------===
 

#ifndef __STDBOOL_H
#define __STDBOOL_H

#define __bool_true_false_are_defined 1

#if defined(__MVS__) && __has_include_next(<stdbool.h>)
#include_next <stdbool.h>
#else

#if defined(__STDC_VERSION__) && __STDC_VERSION__ > 201710L
// * FIXME: We should be issuing a deprecation warning here, but cannot yet due
// * to system headers which include this header file unconditionally.

#elif !defined(__cplusplus)
#define bool _Bool
#define true 1
#define false 0
#elif defined(__GNUC__) && !defined(__STRICT_ANSI__)
// Define _Bool as a GNU extension.
#define _Bool bool
#if defined(__cplusplus) && __cplusplus < 201103L
// For C++98, define bool, false, true as a GNU extension. 
#define bool bool
#define false false
#define true true
#endif
#endif

#endif //
#endif //
*/