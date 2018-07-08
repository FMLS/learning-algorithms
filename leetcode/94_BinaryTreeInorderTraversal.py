# Definition for a binary tree node.
from tools import draw

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    @property
    def value(self):
        return self.val

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        head = root
        while stack or head:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                res.append(head.val)
                head = head.right
        return res
                
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

    draw.sampleDrawTree(node1)

    print(Solution().inorderTraversal(node1))
