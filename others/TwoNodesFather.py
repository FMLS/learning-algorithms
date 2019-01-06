from tools.leetcode import deserialize, drawtree, TreeNode


class Solution:

    def TwoNodesFather(self, head, n1, n2):
        if head is None or head.val == n1 or head.val == n2:
            return head

        left = self.TwoNodesFather(head.left, n1, n2)
        right = self.TwoNodesFather(head.right, n1, n2)

        if left is not None and right is not None:
            return head

        return left if left is not None else right



if __name__ == '__main__':
    tree = deserialize('[1, 2, 3, 4, 5, 6, 7]')
    drawtree(tree)
    print(Solution().TwoNodesFather(tree, 4, 5))

    tree = deserialize('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]')
    #drawtree(tree)
    print(Solution().TwoNodesFather(tree, 4, 5))

    tree = deserialize('[1,2,null,3,null,4]')
    drawtree(tree)
    print(Solution().TwoNodesFather(tree, 4, 3))
