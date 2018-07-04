from tools import mlist

# 给定一个链表head, 判断链表是否有环, 如果有则返回环入口节点, 无环返回None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def getLoopNode(self, head):
        if head == None or head.next == None or head.next.next == None:
            return None
        # 这里需要注意
        slow = head.next
        fast = head.next.next

        while slow != fast:
            if fast.next == None or fast.next.next == None:
                return None
            slow = slow.next
            fast = fast.next.next

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node4

    head = node1

    res = Solution().getLoopNode(head)
    print(res.value)

