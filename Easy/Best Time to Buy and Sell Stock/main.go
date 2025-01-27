package main

import "fmt"

func maxProfit(prices []int) int {
	if len(prices) < 2 {
		return 0
	}
	minPrice := prices[0]
	maProfit := 0
	for _, price := range prices {
		if price < minPrice {
			minPrice = price
		}
		if price-minPrice > maProfit {
			maProfit = price - minPrice
		}
	}
	return maProfit
}

func main() {
	fmt.Println(maxProfit([]int{2, 4, 1}))
}
