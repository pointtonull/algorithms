from random import randint, seed
from itertools import product


class Partition3(object):
    def __init__(self, problem):
        pass

    MAXN = 12
    MAXVALUE = 12

    def generate(self):
        seed(239)

        a = []
        a.append([1, 1, 1])
        a.append([3, 3, 3, 3])
        a.append([4, 1, 3, 2])
        a.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        for n in range(9, self.MAXN - 1):
            a.append([12] * n)
            a.append([self.MAXVALUE] * n)
            a.append([self.MAXVALUE - 1] * n)
            a.append([randint(1, 2) for _ in range(n)])
            a.append([randint(1, 3) for _ in range(n)])
            a.append([randint(1, self.MAXVALUE) for _ in range(n)])
            a.append([i for i in range(1, n)])

        tests = []
        for b in a:
            tests.append("{}\n{}\n".format(len(b), " ".join(map(str, b))))
        return tests

    def solve(self, dataset):
        lines = dataset.splitlines()
        n = int(lines[0])
        assert 1 <= n and n <= self.MAXN
        A = [int(i) for i in lines[1].split()]
        assert len(A) == n and all(1 <= A[i] and A[i] <= self.MAXVALUE for i in range(n))
        S = sum(A)

        if S % 3 != 0:
            return 0

        T = [[[None for _ in range(S + 1)] for _ in range(S + 1)] for _ in range(n + 1)]
        for (s1, s2) in product(range(S // 3 + 1), repeat=2):
            if s1 == 0 and s2 == 0:
                T[0][s1][s2] = 1
            else:
                T[0][s1][s2] = 0

        for i in range(1, n + 1):
            for (s1, s2) in product(range(S // 3 + 1), repeat=2):
                T[i][s1][s2] = T[i - 1][s1][s2]
                if s1 >= A[i - 1]:
                    T[i][s1][s2] = max(T[i - 1][s1][s2], T[i - 1][s1 - A[i - 1]][s2])
                if s2 >= A[i - 1]:
                    T[i][s1][s2] = max(T[i - 1][s1][s2], T[i - 1][s1][s2 - A[i - 1]])

        return T[n][S // 3][S // 3]


    def check(self, reply, solution):
        if int(reply) == int(solution):
            return 1
        return 0