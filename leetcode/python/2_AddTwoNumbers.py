# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        carry = 0

        while cur1 and cur2:
            res = cur1.val + cur2.val + carry
            if res > 9:
                cur1.val = res % 10
                carry = 1
            else:
                cur1.val = res
                carry = 0
            
            pre1 = cur1
            pre2 = cur2

            cur1 = cur1.next
            cur2 = cur2.next
        
        if not cur1 and not cur2:
            if carry:
                carryNode = ListNode(1)
                pre1.next = carryNode
            return l1

        if not cur1:
            pre1.next = cur2
            cur1 = cur2
            while cur1:
                res = cur1.val + carry
                cur1.val = res % 10
                if res > 9:
                    carry = 1
                else:
                    carry = 0
                pre1 = cur1
                cur1 = cur1.next
            #最后的进位1
            if not cur1 and carry:
                carryNode = ListNode(1)
                pre1.next = carryNode
        
        if not cur2:
            if carry:
                while cur1:
                    res = cur1.val + carry
                    cur1.val = res % 10
                    if res > 9:
                        carry = 1
                    else:
                        carry = 0
                    pre1 = cur1
                    cur1 = cur1.next
                            #最后的进位1
            if not cur1 and carry:
                carryNode = ListNode(1)
                pre1.next = carryNode

        return l1
    
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


l1 = createFromList([9, 8])
l2 = createFromList([1])

head = Solution().addTwoNumbers(l1, l2)

while head != None:
    print(head.val)
    head = head.next
