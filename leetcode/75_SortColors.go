package main

import "fmt"

func sortColors(nums []int) {
	i := 0
	j := len(nums) - 1

	lastLeft := 0
	lastRight := len(nums) - 1

	for i <= j {
		if nums[i] == 0 {
			nums[i], nums[lastLeft] = nums[lastLeft], nums[i]
			lastLeft++
			i++
		} else if nums[i] == 2 {
			nums[i], nums[lastRight] = nums[lastRight], nums[i]
			j--
			lastRight--
		} else {
			i++
		}
	}
}

func main() {
	nums := []int{2, 0, 2, 1, 1, 0}
	//nums = []int {0, 0}
	//nums = []int {2, 0, 1}
	//nums = []int {1, 2, 0}
	//nums = []int {2, 1, 2}
	sortColors(nums)
	fmt.Println(nums)
}
