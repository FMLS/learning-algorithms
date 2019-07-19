package main

import (
	"fmt"
)

func containsDuplicate(nums []int) bool {
	mmp := make(map[int]int, 10)
	for _, i := range nums {
		if _, ok := mmp[i]; ok {
			return true
		}
		mmp[i] = 1
	}
	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))
}
