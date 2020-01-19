# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
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


if __name__ == "__main__":
    print(get_maximum_value(input()))
