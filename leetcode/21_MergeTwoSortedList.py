# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        elif not l2:
            return l1

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        cur = head
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head
        

def createFromList(l):
    head = None
    pre = None
    current = None

    for i in l:
        if head == None:
            head = ListNode(i)
            pre = head
            continue
        current = ListNode(i)
        pre.next = current
        pre = current
    return head



l1 = createFromList([4, 5])
l2 = createFromList([1, 10])

so = Solution()
head = so.mergeTwoLists(l1, l2)

while head != None:
    print(head.val)
    head = head.next


