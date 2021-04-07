package main

import (
	"strconv"
)

func main() {
	firstName := "John"
	updateName(&firstName)
	println(firstName)
}

func updateName(name *string) {
	*name = "David"
}

func sum(number1 string, number2 string) (result int) {
	int1, _ := strconv.Atoi(number1)
	int2, _ := strconv.Atoi(number2)
	result = int1 + int2
	return
}

func calc(number1 string, number2 string) (sum int, mul int) {
	int1, _ := strconv.Atoi(number1)
	int2, _ := strconv.Atoi(number2)
	sum = int1 + int2
	mul = int1 + int2
	return
}
