def printList(head):
    while head != None:
        print(head.value)
        head = head.next

# 相比于reverseList2, 本代码中将nn = cur.next放入循环中,
# 使得删除不必要的判断, 很结构精巧
def reverseList(head):
    pre = None
    cur = head
    while cur != None:
        nn = cur.next
        cur.next = pre
        pre = cur
        cur = nn
    return pre

def reverseList2(head):
    pre = None
    cur = head
    nn = cur.next
    while cur != None:
        cur.next = pre
        pre = cur
        cur = nn
        if nn:
            nn = nn.next
    return pre
