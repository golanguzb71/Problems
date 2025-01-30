package main

func mySqrt(x int) int {
	var (
		base = 2
	)
	if x < 1 {
		return 0
	}
	for ; base*base <= x; base++ {
	}
	return base - 1
}

func main() {
	print(mySqrt(1000))
}
