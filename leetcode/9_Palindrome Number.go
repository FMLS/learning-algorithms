package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	result := 0
	tmp := x
	for tmp/10 > 0 {
		digit := tmp % 10
		tmp /= 10

		result *= 10
		result += digit
	}

	if tmp > 0 {
		result *= 10
		result += tmp
	}

	if result == x {
		return true
	}

	return false
}

func main() {

	fmt.Println(isPalindrome(1201))

}
