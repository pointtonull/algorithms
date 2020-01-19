# Uses python3
import sys

COINS = (10, 5, 1)

def get_change(money):
    coins = list(COINS)
    used_coins = 0
    while money:
        coin_value = coins.pop(0)
        used_here = money // coin_value
        paid_here = used_here * coin_value
        money -= paid_here
        used_coins += used_here
    return used_coins

def test(case, expected):
    obtained = get_change(case)
    if expected != obtained:
        raise ValueError("for case %d, result %d was expected, got %d" % (case,
            expected, obtained))

def tests():
    for case, result in ((2, 2), (28, 6)):
        test(case, result)

def stdin():
    m = int(sys.stdin.read())
    print(get_change(m))

if __name__ == '__main__':
#     tests()
    stdin()
