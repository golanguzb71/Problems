package main

import "slices"

func majorityElement(nums []int) int {
	slices.Sort(nums)
	count := 0
	currentElement := nums[0]
	for i := 0; i < len(nums); i++ {

		if nums[i] == currentElement {
			count++
			if count > len(nums)/2 {
				return currentElement
			}
		} else {
			count = 1
			currentElement = nums[i]
		}
	}

	return currentElement
}

func main() {
	print(majorityElement([]int{1, 1, 1, 1, 2, 2, 2, 3, 4, 3, 4}))
}
