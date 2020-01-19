class Knapsack(object):
    def __init__(self, problem):
        pass

    mytests = ['10 3\n1 4 8\n',
               '20 4\n5 7 12 18\n',
               '10 5\n3 5 3 3 5\n',
               '100 5\n72 74 42 68 57\n',
               '500 20\n342 381 230 381 206 393 364 319 279 385 345 263 365 281 298 247 239 201 378 351\n',
               ]
    answers = ['9\n',
               '19\n',
               '10\n',
               '99\n',
               '499\n',
               '946\n',
               '0\n',
               '0\n',
               '2335\n',
               '8423\n',
               '7628\n',
               '7419\n',
               '9850\n',
               '4842\n']

    def generate(self):
        return list(zip(self.mytests, zip(self.answers, self.mytests)))

    def solve(self, dataset):
        s, n = list(map(int, dataset.split("\n")[0].strip().split()))
        a = list(map(int, dataset.split("\n")[1].strip().split()))
        can = [True] + [False] * s
        for x in a:
            for i in range(s - x + 1)[::-1] :
                if can[i]:
                    can[i + x] = True
        while not can[s]:
            s -= 1
        return str(s)

    class Parser:
        def __init__(this, f):
            this.f = f.split()
            this.i = -1
        def read(this):
            this.i += 1
            return this.f[this.i]

    def calc_answer(self, input, output):
        try:
            inf = self.Parser(input)
            ouf = self.Parser(output)
            return int(ouf.read()), ""
        except Exception as e:
            return 0, "wrong output format: " + str(e)

    def check(self, output, clue):
        (answer, input) = clue
        ca = self.calc_answer(input, output)
        ja = self.calc_answer(input, answer)
        if ca[1] != "": return False, ca[1]
        if ja[1] != "": return False, "grader error: " + ja[1]
        if ca[0] != ja[0]: return False, ""#"got: " + str(ca[0]) + " expected: " + str(ja[0])

        return True, ""


