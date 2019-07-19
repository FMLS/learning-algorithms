# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _getDepth(self, node):
        if node == None:
            return 0
        return 1 + max(self._getDepth(node.left), self._getDepth(node.right))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self._getDepth(root)
