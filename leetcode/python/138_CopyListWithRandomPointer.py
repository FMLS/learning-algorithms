# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        map_ = {}
        while p != None:
            map_[p] = RandomListNode(p.label)
            p = p.next
        
        p = head
        while p != None:
            map_.get(p).next = map_.get(p.next)
            map_.get(p).random = map_.get(p.random)
            p = p.next
        return map_.get(head)
            
