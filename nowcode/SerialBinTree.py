class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class SerialBinTree:

    #以先序遍历方式序列化二叉树
    #下划线便于分割值
    # '#' 用于区分树结构
    @staticmethod
    def serailByPre(node):
        if node == None:
            return '#_'
        res = str(node.value) + '_'
        res += SerialBinTree.serailByPre(node.left)
        res += SerialBinTree.serailByPre(node.right)

        return res
    
    @staticmethod
    def reconByPreString(str_):
        queue = str_.rstrip('_').split('_')
        queue.reverse()
        print(queue)
        return SerialBinTree.unSerailByPre(queue)
    
    @staticmethod
    def unSerailByPre(queue):
        value = queue.pop()
        if value == '#':
            return None
        node = Node(value)
        node.left = SerialBinTree.unSerailByPre(queue)
        node.right = SerialBinTree.unSerailByPre(queue)
        return node

def preOrderPrint(node):
    stack = []
    #first access
    stack.append(node)
    while stack:
        #second access
        node = stack.pop()
        print(node.value)
        if node.right:
            #first
            stack.append(node.right)
        if node.left:
            #first
            stack.append(node.left)

if __name__ == '__main__':
    node4 = Node(4)
    node5 = Node(5)
    node2 = Node(2)
    node2.left = node4
    node2.right = node5
    node6 = Node(6)
    node7 = Node(7)
    node3 = Node(3)
    node3.left = node6
    node3.right = node7
    node1 = Node(1)
    node1.left = node2
    node1.right = node3

    serailStr = SerialBinTree.serailByPre(node1)
    root = SerialBinTree.reconByPreString(serailStr)
    preOrderPrint(root)
