from tools.draw import sampleDrawTree
from tools.leetcode import drawtree, deserialize

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    @property
    def value(self):
        return self.val

# 本题基本思路是利用二叉查找树的中序遍历结果的有序性

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        return self.inOrder(root)
    
    def inOrder(self, root):
        if root == None:
            return 
        leftRes = self.inOrder(root.left)
        self.k -= 1
        if self.k == 0:
            return root.val
        elif self.k < 0:
            res = None if leftRes == None else leftRes
            return res

        rightRes = self.inOrder(root.right)
        # 不能用如下表达式
        # res = leftRes or rightRes
        res = leftRes if leftRes != None else rightRes
        return res

def createListByLevel(arr):
    end = len(arr)
    index = 0
    nodes = [TreeNode(val) if val != None else None for val in arr]
    while index * 2 + 1 < end:
        if nodes[index] != None:
            nodes[index].left = nodes[index * 2 + 1]
            if index * 2 + 2 < end:
                nodes[index].right = nodes[index * 2 + 2]
        index += 1
    return nodes[0]


if __name__ == '__main__':
    #arr = [5, 3, 6, 2, 4, None, None, 1]
    #arr = [31,30,48,3,None,38,49,0,16,35,47,None,None,None,2,15,27,33,37,39,None,1,None,5,None,22,28,32,34,36,None,None,43,None,None,4,11,19,23,None,29,None,None,None,None,None,None,40,46,None,None,7,14,17,21,None,26,None,None,None,41,44,None,6,10,13,None,None,18,20,None,25,None,None,42,None,45,None,None,8,None,12,None,None,None,None,None,24,None,None,None,None,None,None,9]
    # 这个测试用例主要是0的判断, 所以return时不能用 a or b表达式
    root = deserialize('[31,30,48,3,null,38,49,0,16,35,47,null,null,null,2,15,27,33,37,39,null,1,null,5,null,22,28,32,34,36,null,null,43,null,null,4,11,19,23,null,29,null,null,null,null,null,null,40,46,null,null,7,14,17,21,null,26,null,null,null,41,44,null,6,10,13,null,null,18,20,null,25,null,null,42,null,45,null,null,8,null,12,null,null,null,null,null,24,null,null,null,null,null,null,9]')
    ans = Solution().kthSmallest(root, 1)
    print(ans)

