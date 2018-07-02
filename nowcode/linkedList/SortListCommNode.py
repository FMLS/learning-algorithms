class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SortListCommNode:
    @staticmethod
    def printCommNode(head1, head2):

        while head1 != None and head2 != None:
        
            #if head1.value < head2.value and head1 != None:
            while head1.value < head2.value and head1 != None:
                head1 = head1.next
        
            #if head2.value < head1.value and head2 != None:
            while head2.value < head1.value and head2 != None:
                head2 = head2.next

            if head1.value == head2.value:
                print(head1.value)
                head1 = head1.next
                head2 = head2.next

if __name__ == '__main__':
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)

    head1 = Node1
    Node1.next = Node2
    Node2.next = Node3

    Node22 = Node(1)
    Node33 = Node(3)
    Node44 = Node(4)

    head2 = Node22
    Node22.next = Node33
    Node33.next = Node44

    SortListCommNode.printCommNode(head1, head2)
