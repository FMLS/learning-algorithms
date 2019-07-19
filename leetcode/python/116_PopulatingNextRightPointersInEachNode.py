# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from tools.leetcode import deserialize


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return None

        if root.left and root.right:
            root.left.next = root.right

        connLeft = root.right if root.right is not None else root.left
        if connLeft and root.next:
            connRight = root.next.left if root.next.left else root.next.right
            connLeft.next = connRight

        self.connect(root.left)
        self.connect(root.right)



if __name__ == '__main__':
    tree = deserialize('[1,2,3,4,5,6,7]')
    Solution().connect(tree)
    print(tree)
