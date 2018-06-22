import turtle

class DrawTree(object):

    def __init__(self):
        self.font = ('Arial', 8, 'normal')
        self.t = turtle.Turtle()
        self.t.speed(10)
        self.myWin = turtle.Screen()
        self.myWin.screensize(2560, 1280)
        self.t.left(90)
        self.t.up()
        self.t.forward(300)
        self.t.down()
        self.t.color("red")

    def _doDraw(self, node, branch_len):
        if branch_len < 10 or node == None:
            return
        self.t.backward(branch_len)
        self.t.right(20)
        self._doDraw(node.left, branch_len - 10)
        self.t.left(40)
        self._doDraw(node.right, branch_len - 10)
        self.t.right(20)
        #t.circle(10)
        self.t.write(node.value, align='right', font=self.font)
        self.t.forward(branch_len)

    
    def drawTree(self, tree):
        branch_len = 10 * tree.hight
        self._doDraw(tree.root, branch_len)
        self.t.write('root', font=self.font)
        self.myWin.exitonclick()
