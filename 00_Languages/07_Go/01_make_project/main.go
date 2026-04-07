package main

import "fmt"

func main() {
	// 짧은 출력
	fmt.Println("Hello World!")
	
	// 변수 선언
	var name string = "jongya"
	var runCount int = 2
	fmt.Println(name, runCount)

	// 자동 자료형 추론 가능
	var fruit = "banana"
	var price = 3000
	fmt.Println(fruit, price)

	// 함수(func) 내부에서만 사용할 수 있는 짧은 변수 선언
	fruit2 := "apple"
	price2 := 5000
	fmt.Println(fruit2, price2)
}