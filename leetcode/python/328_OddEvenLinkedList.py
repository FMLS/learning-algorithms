# Definition for singly-linked list.
from tools.mlist import (
    createSampleList, 
    printList,
    createListFromArr
)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        oddHead = head
        evenHead = head.next        

        op = oddHead
        ep = evenHead

        while op.next is not None and ep.next is not None:
            op.next = ep.next
            op = ep.next

            ep.next = op.next
            ep = op.next
        
        op.next = evenHead
        return oddHead

if __name__ == '__main__':

    head = createSampleList(0, 10)
    head = createListFromArr([2, 1, 3, 5, 6, 4, 7])
    head = Solution().oddEvenList(head)
    printList(head)

