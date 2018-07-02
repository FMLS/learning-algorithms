from tools import printList, reverseList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def RemoveLastKthNode(head, k):
    if head == None or k < 1:
        return head

    p = head
    while p != None:
        p = p.next
        k -= 1
    
    if k > 0:
        return head
    elif k == 0:
        return head.next
    # k < 0
    else:
        p = head
        k += 1
        while k != 0:
            p = p.next
            k += 1
        p.next = p.next.next
        
        return head

if __name__ == '__main__':
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)

    head1 = Node1
    Node1.next = Node2
    Node2.next = Node3

    head = RemoveLastKthNode(head1, 0)
    printList(head)

    printList(reverseList(head))
