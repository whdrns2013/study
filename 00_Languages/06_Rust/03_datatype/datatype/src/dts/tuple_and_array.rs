pub fn tuple_and_array() {
    let tup = (1, 2, 3, "한", 3.123);
    let arr = [5, 6, 7, 8, 9];

    println!("{}", tup.1);
    println!("{}", arr[1]);
    println!("{:?}", &arr[1..3]);
}