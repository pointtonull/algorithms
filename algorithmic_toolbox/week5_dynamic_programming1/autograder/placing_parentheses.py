import random

class PlacingParentheses(object):
    maxdigits = 15

    def __init__(self, problem):
        pass

    def generate(self):
        random.seed(547345)
        tests=[]
        tests.append("1+2-3*4-5")
        tests.append("5-8+7*4-8+9")
        tests.append("2+3")
        tests.append("5")

        long="9"
        for _ in range(self.maxdigits - 1):
            long += "*9"
        tests.append(long)

        for d in range(self.maxdigits-1):
            s = str(random.randint(0, 9))
            for _ in range(d):
                op = ["+", "-", "*"]
                s += op[random.randint(0, 2)]
                s += str(random.randint(0, 9))
            tests.append(s)

        return tests

    def check(self, output, clue):
        if int(output) == int(clue):
            return 1
        else:
            return 0

    def solve(self, dataset):
        assert(len(dataset) % 2 == 1)
        n=(len(dataset)+1)//2

        m = [[float('inf')  for _ in range(n+1)] for _ in range(n+1)]
        M = [[-float('inf') for _ in range(n+1)] for _ in range(n+1)]

        def evalt(a, b, op):
            if op == '+':
                return a+b
            elif op == '-':
                return a-b
            elif op == '*':
                return a*b
            else:
                assert True

        for i in range(1, n+1):
            m[i][i] = int(dataset[2*(i-1)])
            M[i][i] = int(dataset[2*(i-1)])

        for s in range(1, n+1):
            for i in range(1, n-s+1):
                j=i+s
                for k in range(i,j):
                    a = evalt(M[i][k], M[k+1][j], dataset[2*k-1])
                    b = evalt(M[i][k], m[k+1][j], dataset[2*k-1])
                    c = evalt(m[i][k], M[k+1][j], dataset[2*k-1])
                    d = evalt(m[i][k], m[k+1][j], dataset[2*k-1])

                    m[i][j]=min(m[i][j],a,b,c,d)
                    M[i][j]=max(M[i][j],a,b,c,d)

        return M[1][n]



