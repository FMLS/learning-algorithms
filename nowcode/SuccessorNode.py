from tools import DrawTree

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value 
    
    def __str__(self):
        return str(self.value)

class SuccessorNode:

    @staticmethod
    def getSuccessorNode(node):
        if node == None:
            return node
        #如果右子树不为空, 则返回右子树中最左侧节点
        if node.right:
            return SuccessorNode.getLeftMost(node.right)
        else:
            parent = node.parent
            while parent != None and parent.left != node:
                node = parent
                parent = node.parent
            return parent

        
    @staticmethod
    def getLeftMost(node):
        while node.left:
            node = node.left
        return node

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

    node4.parent = node2
    node5.parent = node2
    node2.parent = node1
    node6.parent = node3
    node7.parent = node3
    node3.parent = node1

    print(SuccessorNode.getSuccessorNode(node2))
