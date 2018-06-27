import random

from tools.draw import DrawTree

class Node(object):
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None
        self.right = None
        self.n = None
        #self._left = None
        #self._right = None
    
    #@property
    #def left(self):
    #    return self._left
    
    #@left.setter
    #def left(self, val):
    #    self._right = val

    
    #@property
    #def right(self):
    #    return self._right
    
    #@right.setter
    #def right(self, val):
    #    self._right = val

class KV(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
class SortBinTree(object):
    def __init__(self):
        self.root = None

    def _insert(self, node, data):
        if node == None:
            node = Node()
            node.key = data.key
            node.value = data.value
            node.n = 1
            return node

        elif data.key < node.key:
            node.left = self._insert(node.left, data)
        
        elif data.key > node.key:
            node.right = self._insert(node.right, data)
        
        node.n = self._getSize(node.left) + self._getSize(node.right) + 1
        
        return node

    def createFromList(self, data=[]):
        for item in data:
            self.root = self._insert(self.root, KV(item, item))
    
    def _preOrderPrint(self, node):
        if node == None:
            return
        self._preOrderPrint(node.left)
        print(f'key: {node.key}  value: {node.value}  size: {node.n}') 
        self._preOrderPrint(node.right)

    def preOrderPrintRe(self):
        print('前序遍历:')
        self._preOrderPrint(self.root)
    
    def preOrderPrint(self):
        print('非递归前序遍历')
        stack = []
        stack.append(self.root)
        while stack:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    def inOrderPrint(self):
        print('非递归中序遍历')
        stack = []
        head = self.root

        while stack or head != None:
            #压左边界
            if head != None:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                print(head.value)
                head = head.right
    
    def postOrderPrint(self):
        print('非递归后续遍历')
        stack1 = []
        stack2 = []
        stack1.append(self.root) 
        #栈中有内容
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            print(node.value)

    
    def _getHigth(self, node):
        if node == None:
            return 0

        return max(self._getHigth(node.left), self._getHigth(node.right)) + 1

    @property
    def hight(self):
        return self._getHigth(self.root)
    
    def _getSize(self, node):
        if node == None:
            return 0

        return self._getSize(node.left) + self._getSize(node.right) + 1

    @property
    def size(self):
        return self._getSize(self.root)
    
    def _get(self, node, key):
        if node == None:
            return None
        elif key > node.key:
            return self._get(node.right, key)
        elif key < node.key:
            return self._get(node.left, key)
        else:
            return node.value
    
    def getByKey(self, key):
        return self._get(self.root, key)
    
    def _getMin(self, node):
        if node.left == None:
            return node
        else:
            return self._getMin(node.left)

    @property
    def min(self):
        return self._getMin(self.root)

    #向下取整
    def _getFloor(self, node, key):
        if node == None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._getFloor(node.left, key)
        t = self._getFloor(node.right, key)
        if t != None:
            return t
        else:
            return node
    
    def floor(self, key):
        res = self._getFloor(self.root, key)
        return None if res == None else res.key


if '__main__' == __name__:

    bin_tree = SortBinTree()
    bin_tree.createFromList(random.sample(range(100), 10))
    #bin_tree.preOrderPrintRe()
    bin_tree.preOrderPrint()
    bin_tree.inOrderPrint()
    bin_tree.postOrderPrint()
    DrawTree().drawTree(bin_tree)

    print(f'tree hight: {bin_tree.hight}')
    print(f'tree size: {bin_tree.size}')

    print(bin_tree.getByKey(50))
    print(f'minimum node: key: {bin_tree.min.key}, value:{bin_tree.min.value}')

    #drawTree = DrawTree()
    #drawTree.drawTree(bin_tree)
