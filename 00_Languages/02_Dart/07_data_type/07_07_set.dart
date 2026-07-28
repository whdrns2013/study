

void main() {
    // declaration set
    var numbers01 = {1, 2, 3, 4};
    Set<int> numbers02 = {5, 6, 7, 8};

    // set has unique values
    var numbers03 = {1, 2, 3};
    numbers03.add(1);
    numbers03.add(2);
    numbers03.add(4);
    numbers03.add(5);
    print(numbers03);  // >> {1, 2, 3, 4, 5}

    // 순서는 없다.  
    print({1, 2, 3}.containsAll({1, 2, 3}));  // >> true
    print({1, 2, 3}.containsAll({3, 2, 1}));  // >> true

    // methods
    //    add
    Set<String> text01 = {"a", "b", "c"};
    text01.add("d");
    print(text01);  // >> {"a", "b", "c", "d"}

    text01.addAll({"z", "y"});
    print(text01);  // >> {"a", "b", "c", "d", "z", "y"}

    //    contains
    print(text01.contains("b"));    // true

    //    
    print(text01.union({"a","b", "t"}));                // {a, b, c, d, z, y, t}
    print(text01.intersection({"c", "d", "안녕하세요"}));  // {c, d}

    //    remove
    print("== remove ==");
    print(text01.remove({"c", "d"}));    // >> false
    
    //    clear
    print("== clear ==");
    text01.clear();
    print(text01);    // >> {}

    // Attributes
    text01.addAll({"a", "b", "c", "d"});
    print(text01);               // >> {a, b, c, d}
    print(text01.first);         // >> a
    print(text01.length);        // >> 6
    print(text01.isEmpty);       // >> true
    print(text01.runtimeType);   // >> _Set<Strign>

}