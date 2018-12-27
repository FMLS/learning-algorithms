from tools.leetcode import TreeNode
from tools.leetcode import deserialize
from tools.leetcode import drawtree

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.doSymmetricRecursive(root.left, root.right)

    def doSymmetricRecursive(self, nodeLeft, nodeRight):
        if nodeLeft is None and nodeRight is None:
            return True
        if nodeLeft is None or nodeRight is None:
            return False

        if nodeLeft.val == nodeRight.val:
            outPair = self.doSymmetricRecursive(nodeLeft.left, nodeRight.right)
            inPair = self.doSymmetricRecursive(nodeLeft.right, nodeRight.left)
            return inPair and outPair

        return False

if __name__ == '__main__':
    nodes = '[1,2,2,3,4,4,3]'
    nodes = '[1,2,2,null,3,null,3]'
    root = deserialize(nodes)
    res = Solution().isSymmetric(root)
    print(res)
