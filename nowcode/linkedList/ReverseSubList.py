from tools import mlist

# 给定一个单向链表的头结点head, 以及两个整数from和to, 在单链表上把第from个节点到第to个节点
# 这一部分进行反转
# 要求:
#    1. 如果链表长度为N, 时间复杂度要求O(N), 额外空间复杂度要求O(1)
#    2. 如果不满足1 <= from <= to <= N, 则不用调整

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reversePart(self, head, from_, to_):
        len_ = 0
        node1 = head
        fPre = tPos = None

        while node1 != None:
            len_ += 1
            fPre = node1 if len_ == from_ - 1 else fPre
            tPos = node1 if len_ == to_ + 1 else tPos
            node1 = node1.next 
        
        if from_ > to_ or from_ < 1 or to_ > len_:
            return head
        # 确定开始反转的位置 
        node1 = head if fPre == None else fPre.next
        node2 = node1.next
        node1.next = tPos
        next_ = None

        # 开始反转
        while node2 != tPos:
            next_ = node2.next
            node2.next = node1
            node1 = node2
            node2 = next_
        
        # 从头开始反转, 没有fPre
        if fPre != None:
            fPre.next = node1
            return head
        
        return node1


    #def reverseSubList(self, head, start, end):

    #    step = 1
    #    cur = head
    #    while step < start - 1:
    #        cur = cur.next
    #        step += 1

    #    cutHead = cur
    #    cur = cur.next
    #    subTail = cur

    #    #开始反转
    #    count = end - start + 1
    #    pre = None
    #    while count > 0 and cur != None:
    #        next_ = cur.next
    #        cur.next = pre
    #        pre = cur
    #        cur = next_
    #        count -= 1
    #    
    #    # 注意这里的赋值
    #    subHead = pre
    #    cutTail = cur

    #    cutHead.next = subHead
    #    subTail.next = cutTail

    #    return head

if __name__ == '__main__':
    #head = mlist.createSampleList(1, 7)
    head = mlist.createSampleList(1, 7)
    head = Solution().reversePart(head, 1, 3)
    mlist.printList(head)
