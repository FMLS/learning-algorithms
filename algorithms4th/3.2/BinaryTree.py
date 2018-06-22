import random

from tools.draw import DrawTree

class Node(object):
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None
        self.right = None
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
    
class SortBinTree(object):
    def __init__(self):
        self.root = None

    def _insert(self, node, data):
        if node == None:
            node = Node()
            node.value = data

        elif data < node.value:
            node.left = self._insert(node.left, data)
        
        elif data > node.value:
            node.right = self._insert(node.right, data)
        
        return node

    
    def createFromList(self, data=[]):
        for item in data:
            self.root = self._insert(self.root, item)
    
    def _preOrderPrint(self, node):
        if node == None:
            return
        self._preOrderPrint(node.left)
        print(node.value) 
        self._preOrderPrint(node.right)

    def preOrderPrint(self):
        print('前序遍历:')
        self._preOrderPrint(self.root)
    
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
    
    def get(self, node, key):
        if node == None:
            return None
        elif key > node.value:
            return self.get(node.right, key)
        elif key < node.value:
            return self.get(node.left, key)
        else:
            return node.value


if '__main__' == __name__:

    bin_tree = SortBinTree()
    bin_tree.createFromList(random.sample(range(100), 50))
    bin_tree.preOrderPrint()

    print(f'tree hight: {bin_tree.hight}')
    print(f'tree size: {bin_tree.size}')

    #drawTree = DrawTree()
    #drawTree.drawTree(bin_tree)
