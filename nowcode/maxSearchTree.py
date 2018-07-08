from tools.draw import sampleDrawTree

# 给定一棵二叉树的头节点head, 已知其中所有节点的值都不一样, 
# 找到含有节点最多的搜索二叉树, 并返回这棵树的头结点

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Solution:
    def findMaxSearchTree(self, head):
        if head == None:
            return True, head, 0
        isLeft, nodeLeft, heightLeft = self.findMaxSearchTree(head.left)
        isRight, nodeRight, heightRight = self.findMaxSearchTree(head.right)

        if isRight and isLeft:
            #node = nodeLeft if heightLeft >= heightRight else nodeRight
            node = head
            isSelf = True
            # 右子节点为None
            if nodeLeft and not nodeRight:
                if head.value > nodeLeft.value:
                    height = heightLeft + 1
                else:
                    isSelf = False
                    node = nodeLeft
                    height = heightLeft
            # 左子节点为None
            elif not nodeLeft and nodeRight:
                if head.value < nodeRight.value:
                    height = height + 1
                else:
                    isSelf = False
                    node = nodeRight
                    height = heightRight
            # 两个子节点都是None
            elif not nodeLeft and not nodeRight:
                return True, head, 1

            elif nodeLeft.value < head.value and nodeRight.value > head.value:
                height = max(heightLeft, heightRight) + 1
            else:
                height = max(heightLeft, heightRight)
                node = nodeLeft if heightLeft >= heightRight else nodeRight
                isSelf = False
            return isSelf, node, height
        else:
            node = nodeLeft if heightLeft >= heightRight else nodeRight
            height = max(heightLeft, heightRight)
            return False, node, height


if __name__ == '__main__':
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node6 = Node(6)
    node8 = Node(8)
    node10 = Node(10)

    #node8.left = node4
    #node8.right = node10
    #node4.left = node2
    #node4.right = node6
    #node2.left = node0
    #node2.right = node3

    node8.left = node4
    node4.left = node2
    node4.right = node1
    node2.left = node0

    _, node, height = Solution().findMaxSearchTree(node8)
    print(height)
    sampleDrawTree(node)

