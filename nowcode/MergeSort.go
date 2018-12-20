package main

import "fmt"

func merge(data []int, l int, mid int, r int) {
	help := make([]int, r-l+1)

	i := 0
	p1 := l
	p2 := mid + 1

	for p1 <= mid && p2 <= r {
		if data[p1] < data[p2] {
			help[i] = data[p1]
			p1++
		} else {
			help[i] = data[p2]
			p2++
		}

		i++
	}

	for p2 <= r {
		help[i] = data[p2]
		i++
		p2++
	}

	for p1 <= mid {
		help[i] = data[p1]
		i++
		p1++
	}

	for i := 0; i < len(help); i++ {
		data[l+i] = help[i]
	}

}

func processHalf(data []int, l int, r int) {

	if l == r {
		return
	}

	mid := l + (r-l)/2
	processHalf(data, l, mid)
	processHalf(data, mid+1, r)
	merge(data, l, mid, r)
}

func mergeSort(data []int) {
	processHalf(data, 0, len(data)-1)
}

func main() {
	data := []int{10, 2, 8, 6, 5, 9, 3, 1, 0}
	mergeSort(data)

	fmt.Println(data)
}
