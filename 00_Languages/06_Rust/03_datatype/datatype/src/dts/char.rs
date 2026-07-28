pub fn chars() {
    // 문자형 데이터타입으로, `char` 라고 쓴다.
    // 문자형은 작은따옴표로 감싼다. (문자열은 큰따옴표로 감쌈)
    // 4바이트의 크기를 가진다.

    let character = 'z';
    let korean: char = '한';
    let some_imozy: char = '😊';

    println!("{}", character);
    println!("{}", korean);
    println!("{}", some_imozy);
}