pub fn bools() {
    // bool 변수 선언
    let the_true = true;
    let the_false : bool = false;  // 명시적 타입 어노테이션

    // bool 논리 연산
    let bool_and    = true && false;
    let bool_or     = true || false;
    let bool_not    = !true;

    println!("AND: {}", bool_and);
    println!("OR: {}", bool_or);
    println!("NOT: {}", bool_not);

    // bool 논리 연산은 "단락 평가"를 한다 (short circuit evaluation)
    // 따라서 &&으로 연결된 두 가지 bool 중 앞쪽 항목이 false 면 뒤쪽 항목은 계산하지 않고 false 가 된다.

    let short_circuit_eval = false && some_func();
    println!("short circuit eval : {}", short_circuit_eval);
    // >> short circuit eval : false

    let short_circuit_eval = true && some_func();
    println!("short circuit eval : {}", short_circuit_eval);
    // >> This is some func!!
    // >> short circuit eval : true

    // bool 비트 연산
    let bool_and    = true & false;
    let bool_or     = true | false;

    println!("AND: {}", bool_and);
    println!("OR: {}", bool_or);

    let x = 10;
    let y = 11;
    println!("x & y : {}", x&y);
    // >> 10
    println!("x | y : {}", x|y);
    // >> 11

    // 00001010
    // 00001011
    // -------- AND
    // 00001010

    // 00001010
    // 00001011
    // -------- OR
    // 00001011

    let x = 2;
    let y = 4;
    println!("x & y : {}", x&y);
    // >> 0
    println!("x | y : {}", x|y);
    // >> 6

}

fn some_func()-> bool{
    // let overflow_integer : u8 = 255;
    // overflow_integer
    println!("This is some func!!");
    true
}