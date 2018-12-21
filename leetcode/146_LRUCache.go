package main

import (
	"container/list"
	"fmt"
)

type LRUCache struct {
	store map[int]*Pack
	li    *list.List
	cap   int
}

type Pack struct {
	Value int
	Node  *list.Element
}

func Constructor(capacity int) LRUCache {
	lruCache := LRUCache{
		store: make(map[int]*Pack, capacity),
		li:    list.New(),
		cap:   capacity,
	}

	return lruCache
}

func (this *LRUCache) Get(key int) int {
	pack, ok := this.store[key]
	if !ok {
		return -1
	}

	node := pack.Node
	this.li.MoveToFront(node)

	return pack.Value
}

func (this *LRUCache) Put(key int, value int) {

	if pack, ok := this.store[key]; ok {
		this.li.MoveToFront(pack.Node)
		this.store[key] = &Pack{
			Value: value,
			Node:  pack.Node,
		}
		return
	}

	if this.cap == 0 {
		end := this.li.Back()
		Ikey := this.li.Remove(end)

		delKey, _ := Ikey.(int)
		delete(this.store, delKey)
		this.cap++
	}

	node := this.li.PushFront(key)
	pack := Pack{
		Value: value,
		Node:  node,
	}

	this.store[key] = &pack
	this.cap--

}

func main() {
	lru := Constructor(2)

	lru.Put(2, 1)
	lru.Put(1, 1)
	lru.Put(2, 3)
	lru.Put(4, 1)

	fmt.Println(1)
	fmt.Println(2)

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
