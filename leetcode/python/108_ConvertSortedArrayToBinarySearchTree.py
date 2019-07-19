from tools.leetcode import TreeNode, drawtree


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.partation(nums, 0, len(nums) - 1)
        return root

    def partation(self, data, left, right):
        """

        :param node:
        :param data:
        :param left:
        :param right:
        :return:  node
        """

        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(data[mid])
        node.left = self.partation(data, left, mid - 1)
        node.right = self.partation(data, mid + 1, right)

        return node


if __name__ == '__main__':

    data = [-10, -3, 0, 5, 9]
    root = Solution().sortedArrayToBST(data)
    drawtree(root)
