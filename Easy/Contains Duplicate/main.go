package main

import "sort"

func containsDuplicate(nums []int) bool {
	sort.Ints(nums)
	for k := range len(nums) - 1 {
		if nums[k] == nums[k+1] {
			return true
		}
	}
	return false
}

func main() {
	print(containsDuplicate([]int{1, 2, 3, 4}))
}
