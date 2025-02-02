package main

func intersection(nums1 []int, nums2 []int) []int {
	checker := make(map[int]bool)
	var result []int
	for i := range nums1 {
		for i2 := range nums2 {
			if nums1[i] == nums2[i2] && !checker[nums2[i2]] {
				result = append(result, nums2[i2])
				checker[nums2[i2]] = true
			}
		}
	}
	return result
}

func main() {
	print(intersection([]int{1, 2, 3}, []int{3, 2, 0}))
}
