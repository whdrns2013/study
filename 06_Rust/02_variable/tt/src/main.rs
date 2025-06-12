fn main() {

    // 기본적인 변수 선언법
    let sentence = "The First Sentence";
    println!("{}", sentence);
    // >> The First Sentence

    // 변수는 기본적으로 불변성 (immutable) 을 가지고 있음  
    // sentence = "The Second Try";
    // println!("{}", sentence);
    // >> sentence = "The Second Try";
    // >> ^^^^^^^^^^^^^^^^^^^^^^^^^^^ cannot assign twice to immutable variable
    // >> For more information about this error, try `rustc --explain E0384`.
    // >> error: could not compile `tt` (bin "tt") due to 1 previous error

    // 변수를 다시 선언할 수 있게 하려면, mut 지시어를 사용
    let mut mutable_sentence = "The Second Sentence";
    mutable_sentence = "The Thrid Sentence";
    println!("{}", mutable_sentence);
    // >> The Thrid Sentence

}
