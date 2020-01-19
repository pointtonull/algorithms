from random import randint, seed

class LCS2(object):
    def __init__(self, problem):
        pass

    MAXN = 100
    MAXVALUE = 10 ** 9

    def generate(self):
        seed(239)
        a = []
        a.append(([1, 2, 3], [3, 2, 1]))
        a.append(([2, 3, 9], [2, 9, 7, 8]))
        a.append(([1], [10]))
        a.append(([17], [17]))

        for n in [10, 50, 100]:
            a.append(([1] * n, [1] * n))
            a.append(([self.MAXVALUE] * n, [self.MAXVALUE] * (n // 2)))
            a.append(([i for i in range(n)], [2 * i for i in range(n)]))
            a.append(([i for i in range(n)], [2 * i for i in range(n // 2)]))
            a.append(([0] * n, [i % 3 for i in range(n)]))
            a.append(([i % 2 for i in range(n)], [i % 3 for i in range(n)]))
            a.append(([randint(self.MAXVALUE - 1, self.MAXVALUE) for _ in range(n)], [randint(self.MAXVALUE - 1, self.MAXVALUE) for _ in range(n)]))
            a.append(([239], [239] * n))
            for t in [2, 5, 15]:
                a.append(([randint(0, t) for _ in range(n)], [randint(0, t) for _ in range(n)]))

        tests = []
        for (b, c) in a:
            tests.append("{}\n{}\n{}\n{}\n".format(len(b),
                                                   " ".join(map(str, b)),
                                                   len(c),
                                                   " ".join(map(str, c))
                                                   )
                         )
        return tests

    def solve(self, dataset):
        data = list(map(int, dataset.split()))
        n = data[0]
        data = data[1:]
        a = data[0:n]
        data = data[n:]
        m = data[0]
        data = data[1:]
        b = data[0:m]

        T = [[0] * (m + 1) for _ in range(n + 1)]
        # T[i][j] = lcs(a[:i], b[j])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    T[i][j] = max(T[i - 1][j - 1] + 1, T[i][j - 1], T[i - 1][j])
                else:
                    T[i][j] = max(T[i - 1][j], T[i][j - 1])

        return T[n][m]

    def check(self, clue, reply):
        if int(clue) == int(reply):
            return 1
        return 0
