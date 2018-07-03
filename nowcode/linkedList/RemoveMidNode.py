from tools import mlist

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def removeMidNode(self, head):
        if not head or not head.next:
            return head
        if not head.next.next:
            return head.next
        
        #错误, p2应比p1现行一步, 否则p1会停在目标节点上无法删除
        # p1 = p2 = head

        #这样会让p1停在目标节点的前一个节点
        p1 = head
        p2 = head.next.next

        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        p1.next = p1.next.next
        return p1

if __name__ == '__main__':
    head = mlist.createSampleList(0, 7)
    print('before remove mid:')
    mlist.printList(head)
    so = Solution().removeMidNode(head)
    print('after remove mid:')
    mlist.printList(head)
