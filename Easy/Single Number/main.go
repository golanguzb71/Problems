package main

import "fmt"

func singleNumber(nums []int) int {
	result := 0
	for _, num := range nums {
		result ^= num
	}
	return result
}

func main() {
	fmt.Println(singleNumber([]int{1, 2, 3, 4, 1, 2, 3})) // Output: 4
}
