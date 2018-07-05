from tools import mlist

# 给定一个链表head, 判断链表是否有环, 如果有则返回环入口节点, 无环返回None

# 本题目最优解思路是: 
# 利用一个快指针fast, 每次走两步, 慢指针slow, 每次走一步, 第一次相遇时,
# fast重新指向head, 并且和slow一起开始每次走一步, 再次相遇时一定是环入口处

# 证明:
# 设第一次相遇时, fast走了2k步, slow走了k步, head距离环入口a步, 环入口距离相遇点b步(相遇一定在环内), 
# 设环长为L, 则有: a + b = k, a + b + n*L = 2k, 由以上两式可得: a + b = n*L, 两侧同时减去b,
# a = n*L - b, n*L - b的位置画图可得就是环入口, 所以第一次相遇时, 一个指针再走a步, 则另一个指针
# 一定在n*L-b处也就是环入口, 此时相遇

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

