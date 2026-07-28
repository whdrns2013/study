pub fn integers() {

    // ## 데이터 타입
    // - Rust 는 정적 타입의 언어 : 모든 변수 타입이 컴파일 시점에 반드시 정해져 있어야 함  
    // - 데이터는 스칼라 타입 (Scalar Type) 과 복합 타입(Compound Type)으로 나뉨

    // ### Scalar Type  
    // - 네 가지 : 정수, 부동 소수점 숫자, 부울, 문자
    // - Integers, floating-point numbers, Booleans, characters.
    // - 즉, Single Value를 포함하는 데이터 타입
    
    // #### Integers 정수형  
    // - 소수점이 없는 숫자
    // - 표현할 수 있는 크기에 따라 8bit, 16bit, 32bit, 64bit, 128bit와 시스템 비트수인 arch 로 나뉘며
    // - 부호 있음(signed; i), 부호 없음 (unsigned; u) 두 가지로 나뉜다.
    // - 각 타입은 2^n (n: 비트수) 개의 숫자를 표현 가능하며, 
    // - signed 는 -2^(n-1) ~ 2^(n-1) - 1 까지, unsigned 는 0 ~ 2^n - 1 까지 표현이 가능하다.  
    
    // 길이	부호 있음 (signed)	부호 없음 (unsigned)
    // 8-bit	i8	u8
    // 16-bit	i16	u16
    // 32-bit	i32	u32
    // 64-bit	i64	u64
    // 128-bit	i128	u128
    // arch	isize	usize

    /* ------------------------------------ e.g. integer :: start ------------------------------------ */

    // u8
    // let a_number: u8 = 7;
    // print!("{a_number}");
    // >> 7

    // u32 - 2^31
    // let a_number: u32 = u32::pow(2, 31);
    // print!("{a_number}");
    // >> 2147483648

    // u32 - 2^32 :: overflow
    // let a_number: u32 = u32::pow(2, 32);
    // print!("{a_number}");
    // >> attempt to multiply with overflow
    // >> note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

    // Max of Integer Type
    // let max_number:u16 = u16::MAX;
    // print!("{max_number}");
    // >> 65535

    // system architecture
    // let arch_number: isize = 16;
    // print!("{arch_number}");
    // >> 16

    // system architecture
    // let arch_max: isize = isize::MAX;
    // print!("{arch_max}");
    // >> 9223372036854775807

    // 타입 접미사를 붙여서 타입을 지정할 수 있음
    // let type_tail = 16u8;
    // print!("{type_tail}");
    // >> 16

    /* ------------------------------------ e.g. integer :: end ------------------------------------ */

    // ### 부동소수점 타입
    // - f32 와 f64 두 가지 타입이 있음
    // - 기본 타입은 f64
    // - 현대 CPU 상에서 f64 와 f32 가 대략 비슷한 속도를 내면서 더 정밀한 값 표현 가능
    // - Rust 에서 모든 부동소수점 타입은 signed (부호가 있음)

    /* ------------------------------------ e.g. float :: start ------------------------------------ */

    // float
    // let float_1 = 0.34f32;
    // let float_2:f32 = 0.34;
    // let float_3:f32 = 0.34f32;

    // float overflow
    // overflow 오류가 나지 않고 표시할 수 있는 정밀도까지만 표현함
    // 표시 못하는 부분들은 버림처리 됨 (반올림 아님)
    // let float_overflow_1:f32 = 0.65352154754845354354;
    // print!("{float_overflow_1}");


    // ### Operation of Integer Type 정수형 타입 연산
    // 더하기 연산
    // let a :i8 = -5;
    // let b :i8 = 10;
    // let sum = a + b;
    // println!("{sum}");

    // 곱하기 연산
    // let multiply = a * b;
    // println!("{multiply}");

    // 나누기 연산 ==> 나누기 후 몫만 반환됨
    // let divide = a / b;
    // println!("{divide}");

    // let divide_2 = b / a;
    // println!("{divide_2}");

    // 나머지 연산 (Modulation)
    // let modulation = a % b;
    // println!("{modulation}");

    // ### 서로 다른 타입 간 연산
    // - u8 + u16 처럼 다른 타입간 연산은 불가능

    // let a = 5u8;
    // let b = 10u16;
    // let sum = a + b;
    // println!("{sum}")

    // let a = 5u8;
    // let b = 10i8;
    // let sum = a + b;
    // println!("{sum}")

    // let a = 5u8;
    // let b = 3.41274f32;
    // let sum = a + b;
    // println!("{}", sum)

    // ## 부동소수점 형 연산  
    // - 기본적으로 정수형 연산과 동일
    // let float_a : f32 = 3.523;
    // let float_b : f32 = 1.234575;
    // let modulation = float_b / float_a;
    // println!("{modulation}")
    // >> 0.35043287

    // - 정수형과 마찬가지로 서로 다른 데이터타입간 연산은 불가능
    // let float_a : f32 = 3.523;
    // let float_b : f64 = 1.234575;
    // let modulation = float_b / float_a;
    // println!("{modulation}")
    // >> cannot divide `f64` by `f32`

    // ## 오버플로우를 다루기  
    // ### wrapping_add와 같은 wrapping_* 메서드로 감싸기 동작 실행하기
    // - 오버플로우가 발생해도 panic 없이 결과값을 래핑하는 메서드
    // - 예를 들어, 정수의 최대값을 넘으면 다시 최소값부터 시작하게 된다.
    // - wrapping_add : 오버플로우시 다시 최-소값에서 시작
    // 
    // let int_a : u8 = 254;
    // let int_b : u8 = 4;
    // let sum = int_a + int_b;
    // println!("{sum}");
    // >> attempt to compute `254_u8 + 4_u8`, which would overflow

    // let int_a : u8 = 254;
    // let int_b : u8 = 4;
    // let sum = int_a.wrapping_add(int_b);
    // println!("{sum}");
    // >> 2

    // let int_a : u8 = 128;
    // let int_b : u8 = 4;
    // let mul = int_a.wrapping_mul(int_b);
    // println!("{}", mul)
    // >> 0

    // let int_a : u8 = 128;
    // let int_b : u8 = 4;
    // let rem = int_a.wrapping_rem(int_b);
    // println!("{}", rem)

    // ### checked_add : 오버플로우시 None 값을 반환
    // let int_a : u8 = 254;
    // let int_b : u8 = 4;
    // let sum = int_a.checked_add(int_b);
    // println!("{:?}", sum);
    // >> None

    // ### saturating_add : 오버플로우시 최대값으로 고정
    // - saturating : 포화
    // let int_a : u8 = 254;
    // let int_b : u8 = 4;
    // let sum = int_a.saturating_add(int_b);
    // println!("{}", sum);
    // >> 255

    // ### overflowing_add : 튜플 (값, 오버플로우 여부)를 반환
    // let int_a : u8 = 254;
    // let int_b : u8 = 4;
    // let sum = int_a.overflowing_add(int_b);
    // println!("{:?}", sum);
    // >> (2, true)

}