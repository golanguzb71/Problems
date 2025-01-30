package main

import (
	"fmt"
)

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	reverse := 0
	num := x
	for num > 0 {
		reverse = reverse*10 + num%10
		num = num / 10
	}
	return reverse == x
}

func main() {
	fmt.Println(isPalindrome(1212))
}
