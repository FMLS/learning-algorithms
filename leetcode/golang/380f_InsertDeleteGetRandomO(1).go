package main

import (
	"fmt"
	"math/rand"
	"time"
)

type RandomizedSet struct {
	keyIndex map[int]int
	IndexKey map[int]int
	size     int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{
		keyIndex: make(map[int]int, 100),
		IndexKey: make(map[int]int, 100),
		size:     0,
	}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {

	if _, ok := this.keyIndex[val]; ok {
		return false
	}

	size := this.size
	this.keyIndex[val] = size
	this.IndexKey[size] = val

	this.size++
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {

	if _, ok := this.keyIndex[val]; !ok {
		return false
	}

	this.size--

	lastItem := this.IndexKey[this.size]
	delIndex := this.keyIndex[val]

	this.IndexKey[delIndex] = lastItem
	this.keyIndex[lastItem] = delIndex

	delete(this.keyIndex, val)
	delete(this.IndexKey, this.size)

	return true
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	rand.Seed(time.Now().UnixNano())
	randomIndex := rand.Intn(this.size)
	return this.IndexKey[randomIndex]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */

func main() {
	obj := Constructor()

	fmt.Println(obj.Insert(1))
	fmt.Println(obj.Remove(2))
	fmt.Println(obj.Insert(2))
	fmt.Println(obj.GetRandom())
	fmt.Println(obj.Remove(1))
	fmt.Println(obj.Insert(2))
	fmt.Println(obj.GetRandom())

}
