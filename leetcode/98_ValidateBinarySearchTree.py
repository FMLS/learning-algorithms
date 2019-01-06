# 判断一棵树是否是BST
from tools.leetcode import deserialize, drawtree


class Solution:
    # 前驱节点法

    def isValidBST(self, root):
        self.prev = None
        return self.doValidBST(root)

    def doValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        if not self.doValidBST(root.left):
            return False

        if self.prev is not None and root.val <= self.prev.val:
            return False

        self.prev = root

        return self.doValidBST(root.right)


if __name__ == '__main__':

    root = deserialize('[6,3,8,1,4,7,9]')
    drawtree(root)
    res = Solution().isValidBST(root)
    print(res)
