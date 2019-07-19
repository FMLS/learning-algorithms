# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tools.leetcode import deserialize, TreeNode


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        # return the node that is not none or None
        return left if left is not None else right


if __name__ == '__main__':
    tree = deserialize('[1,2,3,4,5,6,7]')
    res = Solution().lowestCommonAncestor(tree, TreeNode(4), TreeNode(5))
    print(res)


    tree = deserialize('[1,2,null,3,null,4,null,5]')
    res = Solution().lowestCommonAncestor(tree, TreeNode(4), TreeNode(5))
    print(res)
