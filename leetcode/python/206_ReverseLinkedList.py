class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        prev = None
        while(head):
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return curr

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4

p = Solution().reverseList(node1)
while(p):
    print(p.val)
    p = p.next
        