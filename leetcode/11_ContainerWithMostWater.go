package main

import (
	"fmt"
	"math"
)

func updateMaxWater(height []int, maxWater *int, topLeft, topRight int) {
	curWater := int(math.Min(float64(height[topLeft]), float64(height[topRight])) * math.Abs(float64(topLeft-topRight)))
	if curWater > *maxWater {
		*maxWater = curWater
	}
}

func maxArea(height []int) int {
	length := len(height)
	curLeft := 0
	curRight := length - 1

	topLeft := curLeft
	topRight := curRight

	curWater := int(math.Min(float64(height[topLeft]), float64(height[topRight])) * math.Abs(float64(topLeft-topRight)))
	maxWater := curWater

	for curLeft < curRight {
		for height[curLeft] < height[topRight] && curLeft < curRight {
			curLeft++
			if height[curLeft] > height[topLeft] {
				topLeft = curLeft
				updateMaxWater(height, &maxWater, topLeft, topRight)
			}
		}

		for height[curRight] <= height[curLeft] && curLeft < curRight {
			curRight--
			if height[curRight] > height[topRight] {
				topRight = curRight
				updateMaxWater(height, &maxWater, topLeft, topRight)
			}
		}
	}

	return maxWater
}

func main() {
	//height := []int {1, 8, 6, 2 ,5, 4, 8, 3, 7}
	//height := []int {1, 1, 1}
	height := []int{1, 2, 4, 3}
	water := maxArea(height)
	fmt.Println(water)
}
