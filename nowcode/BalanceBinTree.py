class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BalanceBinTree:

    @staticmethod
    def isBalance(node):
        if node == None:
            return True, 0
        balLeft, hLeft = BalanceBinTree.isBalance(node.left)
        if not balLeft:
            return False, 0
        balRight, hRight = BalanceBinTree.isBalance(node.right)
        if not balRight:
            return False, 0
        if abs(hLeft - hRight) > 1:
            return False ,0
        return True, max(hLeft, hRight) + 1

if __name__ == '__main__':
    node4 = Node(4)
    node5 = Node(5)
    node2 = Node(2)
    node2.left = node4
    node2.right = node5
    node6 = Node(6)
    node7 = Node(7)
    node3 = Node(3)
    node3.left = node6
    node3.right = node7
    node1 = Node(1)
    node1.left = node2
    node1.right = node3

    print(BalanceBinTree.isBalance(node1))
