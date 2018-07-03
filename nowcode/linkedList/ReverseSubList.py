from tools import mlist

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverseSubList(self, head, start, end):

        step = 1
        cur = head
        while step < start - 1:
            cur = cur.next
            step += 1
        
        cutHead = cur
        cur = cur.next
        subTail = cur

        #开始反转
        count = end - start + 1
        pre = None
        while count > 0 and cur != None:
            next_ = cur.next
            cur.next = pre
            pre = cur
            cur = next_
            count -= 1
        
        # 注意这里的赋值
        subHead = pre
        cutTail = cur

        cutHead.next = subHead
        subTail.next = cutTail

        return head

if __name__ == '__main__':
    head = mlist.createSampleList(1, 7)
    Solution().reverseSubList(head, 2, 7)
    mlist.printList(head)
