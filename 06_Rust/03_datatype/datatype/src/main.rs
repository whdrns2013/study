fn main() {

    // ## 데이터 타입
    // - Rust 는 정적 타입의 언어 : 모든 변수 타입이 컴파일 시점에 반드시 정해져 있어야 함  
    // - 데이터는 스칼라 타입 (Scalar Type) 과 복합 타입(Compound Type)으로 나뉨

    // ### Scalar Type  
    // - 네 가지 : 정수, 부동 소수점 숫자, 부울, 문자
    // - Integers, floating-point numbers, Booleans, characters.
    // - 즉, Single Value를 포함하는 데이터 타입
    
    // ### Integers 정수형  
    // - 소수점이 없는 숫자

    let guess: u32 = "42".parse().expect("Not a number!");
    let guess = "42".parse().expect("Not a number!");
}
