package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	son := strconv.Itoa(x)
	firstPointer := 0
	lastPointer := len(son) - 1
	for _ = range son {
		if string(son[firstPointer]) != string(son[lastPointer]) {
			return false
		}
		firstPointer += 1
		lastPointer -= 1
	}
	return true
}

func main() {
	fmt.Println(isPalindrome(121))
}
