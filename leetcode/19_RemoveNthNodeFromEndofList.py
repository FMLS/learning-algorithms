# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or n < 1:
            return head
        
        p = head
        
        while p is not None:
            n -= 1
            p = p.next
        
        if n > 0:
            return head
        if n == 0:
            return head.next
        
        p = head
        n += 1
        while n != 0:
            n += 1
            p = p.next
        
        p.next = p.next.next
        return head
        