# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        p1 = head
        p2 = p1.next

        while p2 != None and p2 != p1:
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
            else:
                break

        if p2 != None:
            return True
        else:
            return False

if __name__ == '__main__':
    one = ListNode(0)
    two = ListNode(1)
    thr = ListNode(2)
    head = one
    one.next = two
    #two.next = thr
    #thr.next = None

    print(Solution().hasCycle(head))
