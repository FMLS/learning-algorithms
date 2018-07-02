class thing(object):
    def __init__(self, num, weight, price, status=0):
        self.num    = num
        self.weight = weight
        self.price  = price
        self.status = status

class package(object):
    def __init__(self, size):
        self.size   = size
        self.remain = size
        self.weight = 0
        self.price  = 0
        self.space  = []
    
    def put(self, s):
        self.space.append(s)
        self.weight += s.weight
        self.remain -= s.weight
        self.price  += s.price

    def clear(self):
        self.space.clear()

class tagKnapsackProblem(object):
    def __init__(self, package, things, policy=0):
        self.package = package
        self.things  = things
        self.policy  = policy
    
    def dp(self, i, v):
        d = [ [0 for i in range(v)] for i in range(len(self.things)) ]
        for i in range(len(self.things) - 1):
            for j in range(v):
                d[i][j] = 0
        
        for i in range(len(self.things) - 1):
            for j in range(v):
                if (j < self.things[i].weight):
                    d[i][j] = d[i - 1][j]
                else:
                    d[i][j] = max(d[i - 1][j], d[i - 1][j - self.things[i].weight] + self.things[i].price)
        
        return d[6][149]
    
    def solve(self, policy):
        if policy == 0:
            self.things.sort(key = lambda x: x.weight, reverse=True)
        if policy == 1:
            self.things.sort(key = lambda x: x.price)
        if policy == 2:
            self.things.sort(key = lambda x: x.price/x.weight)
        if policy == 3:
            res = self.dp(len(self.things) - 1, self.package.size)
            print('policy:{}, totoal weight:{}, totoal price:{}'.format(
                policy,
                '',
                res)
            )
            return

        while min(self.things, key=lambda x: x.weight).weight <= self.package.remain:
            if self.things[-1].weight <= self.package.remain:
                self.package.put(self.things.pop())
            else:
                self.things.pop()
            if len(self.things) == 0:
                break

        print('policy:{}, totoal weight:{}, totoal price:{}'.format(
            policy,
            self.package.weight,
            self.package.price
        ))
        for x in self.package.space:
            print(x.num, ' ')


things = [
    thing(1, 35, 10),
    thing(2, 30, 40),
    thing(3, 60, 30),
    thing(4, 50, 50),
    thing(5, 40, 35),
    thing(6, 10, 40),
    thing(7, 25, 30)
]

pack = package(150)
problem = tagKnapsackProblem(pack, things[:])
problem.solve(0)

pack = package(150)
problem = tagKnapsackProblem(pack, things[:])
problem.solve(1)

pack = package(150)
problem = tagKnapsackProblem(pack, things[:])
problem.solve(2)

pack = package(150)
problem = tagKnapsackProblem(pack, things[:])
problem.solve(3)
