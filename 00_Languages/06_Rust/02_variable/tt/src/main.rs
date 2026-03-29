fn main() {  

    // 기본적인 변수 선언법
    // let sentence = "Sentence 1";
    // println!("{}", sentence);

    // 변수는 기본적으로 불변성 (immutable) 을 가지고 있음  
    // let sentence = String::new();
    // sentence = "Sentence 1";
    // sentence = "Sentence 2";
    // >> sentence = "The Second Try";
    // >> ^^^^^^^^^^^^^^^^^^^^^^^^^^^ cannot assign twice to immutable variable
    // >> For more information about this error, try `rustc --explain E0384`.
    // >> error: could not compile `tt` (bin "tt") due to 1 previous error

    // 변수를 다시 선언할 수 있게 하려면, mut 지시어를 사용
    // let mut mutable_sentence = "Sentence 3";
    // mutable_sentence = "Sentence 4";
    // println!("{}", mutable_sentence);
    // >> The Thrid Sentence

    // 변수 생성 후 값을 할당하기 
    // let mut sentence = String::new();
    // sentence = "Sentence 1";
    // println!("{sentence}")

    // 변수 생성 후 값 할당
    // let mut sentence = String::new();  // String 타입의 변수 생성
    // let sentence = "Sentence 1".to_string();       // 값을 할당  
    // println!("{sentence}")

    // 가변 변수
    // let mut sentence = "Sentence 1";
    // sentence = "Sentence 2";
    // println!("{sentence}");

    // ------------------------------------------- //

    // 상수
    // const THREE_HOURS_IN_SECOND: u32 = 60*60*3;
    // println!("{THREE_HOURS_IN_SECOND}");

    // ------------------------------------------- //

    // 섀도잉  
    // let x = 5;
    // println!("First x value : {x}");

    // let x = x + 1;
    // println!("Second x value : {x}");

    // {
    //     let x = x + 2;
    //     println!("Lat x value : {x}");
    // }

    // 섀도잉 + 변수 타입 변경
    // let x = 5;
    // println!("First x value : {x}");

    // let x = "Alter Sentence";
    // println!("Lst x value : {x}")
}
