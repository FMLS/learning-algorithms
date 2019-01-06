from tools.leetcode import deserialize, drawtree


class Solution:
    def LevelWalkTree(self, root):
        queue = []
        queue.append(root)
        curLevelCount = 1
        nextLevelCount = 0

        for node in queue:
            print(node.val, end='')
            curLevelCount -= 1

            if node.left:
                queue.append(node.left)
                nextLevelCount +=1
            if node.right:
                queue.append(node.right)
                nextLevelCount +=1

            if curLevelCount == 0:
                print('#')
                curLevelCount = nextLevelCount
                nextLevelCount = 0


if __name__ == '__main__':
    nodes = '[1,2,3,4,5,6,7]'
    nroot = deserialize(nodes)
    drawtree(nroot)
    Solution().LevelWalkTree(nroot)

