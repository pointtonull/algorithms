class LCS3(object):
    def __init__(self, problem):
        pass

    def generate(self):
        tests = []
        tests.append("3\n1 2 3\n3\n2 1 3\n3\n1 3 5\n")
        tests.append("3\n1 2 3\n3\n4 5 6\n3\n1 3 5\n")
        tests.append("3\n1 2 3\n3\n1 3 2\n3\n2 1 3\n")
        tests.append("3\n1 2 3\n3\n4 5 6\n3\n1 3 5\n")
        tests.append("17\n64 20 40 -49 -88 -64 -99 -44 38 9 -32 -86 94 54 -100 -58 -48\n15\n-71 -88 38 72 9 -67 -15 9 -32 8 5 78 -86 94 -100\n13\n-88 29 -19 71 -69 38 9 -32 -86 94 1 -100 -37\n")
        tests.append("100\n1 1 2 2 2 1 2 1 2 1 1 2 1 2 1 2 2 2 1 2 1 2 2 1 2 1 1 1 2 1 2 2 2 1 1 1 1 2 2 2 1 2 2 1 1 1 1 1 2 2 2 2 2 1 2 2 2 2 2 2 2 2 2 2 1 2 2 1 2 2 2 1 1 1 2 2 1 1 1 2 2 1 2 1 1 2 2 2 1 1 2 1 1 2 1 1 1 2 1 1\n100\n1 2 1 2 1 1 2 1 2 1 2 1 2 1 2 2 2 2 2 2 2 1 2 1 2 2 1 2 1 1 1 2 1 1 2 1 2 2 1 2 1 2 2 1 2 2 2 2 2 1 2 2 1 1 2 1 1 2 2 2 2 1 2 1 2 1 1 1 2 1 2 2 2 2 2 1 2 1 2 1 1 1 2 2 1 1 2 1 1 2 1 1 2 2 2 2 2 2 1 1\n100\n2 1 1 2 2 2 2 2 2 2 2 1 1 1 2 1 1 2 1 1 1 1 1 1 2 2 2 1 1 1 1 1 1 1 2 1 1 2 1 1 2 2 1 1 2 2 1 1 1 1 2 2 2 1 1 1 2 2 1 1 2 1 1 2 2 2 2 1 1 2 2 2 2 1 1 1 1 2 1 1 2 2 1 2 2 1 2 2 1 2 1 2 2 1 1 2 1 1 2 2\n")
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
        data = data[m:]
        k = data[0]
        data = data[1:]
        c = data[0:k] 
        dp = [0] * (n + 1) * (m + 1) * (k + 1)
        for i in range(n + 1):
            for j in range(m + 1):
                for l in range(k + 1):
                    v = (i * (m + 1) + j) * (k + 1) + l
                    if i < n and j < m and l < k and a[i] == b[j] == c[l]:
                        u = ((i + 1) * (m + 1) + j + 1) * (k + 1) + l + 1
                        dp[u] = max(dp[u], dp[v] + 1)
                    if i < n:
                        dp[v + (m + 1) * (k + 1)] = max(dp[v + (m + 1) * (k + 1)], dp[v])
                    if j < m:
                        dp[v + (k + 1)] = max(dp[v + (k + 1)], dp[v])

                    if l < k:
                        dp[v + 1] = max(dp[v + 1], dp[v])

        return str(dp[(n + 1) * (m + 1) * (k + 1) - 1])

    def check(self, clue, reply):
        if int(clue) == int(reply):
            return 1
        return 0
