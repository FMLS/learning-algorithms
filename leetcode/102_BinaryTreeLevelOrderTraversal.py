from tools.leetcode import deserialize, drawtree
import queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return [[]]
        que = queue.Queue()
        level = []
        ans = []
        que.put(root)
        total = 1

        while not que.empty():
            count = total
            minus = 0
            while count and not que.empty():
                node = que.get()
                level.append(node.val)                    
                if node.left:
                    que.put(node.left)
                else:
                    minus += 1
                    
                if node.right:
                    que.put(node.right)
                else:
                    minus += 1

                count -= 1
            
            ans.append(level[:])
            level.clear()
            total = total * 2 - minus
        
        return ans

if __name__ == '__main__':
    tree = '[3,9,20,null,null,15,7]'
    root = deserialize(tree)
    drawtree(root)
    ans = Solution().levelOrder(root)
    print(ans)
