import unittest

class Q:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def safe(self, other):
        return self.row != other.row and self.col != other.col \
            and abs(self.row-other.row) != abs(self.col-other.col)

    def __str__(self):
        return "(%s,%s)" % (self.row, self.col)


def eight_queen(s, result=[]):
    string_queens = [int(i) for i in str(s)]
    nextRow = len(string_queens)

    if nextRow == 8:
        result.append(s)

    found_queens = []
    for row, col in enumerate(string_queens):
        found_queens.append(Q(row, col))

    for col in range(8):
        q = Q(nextRow, col)
        isSafe = True
        for found in found_queens:
            if not q.safe(found):
                isSafe = False
        if isSafe:
            eight_queen(s+str(col))

    return result


class Test(unittest.TestCase):
    def testSafe(self):
        self.assertFalse(Q(0, 0).safe(Q(0, 0)))
        self.assertFalse(Q(0, 0).safe(Q(0, 1)))
        self.assertFalse(Q(0, 0).safe(Q(1, 0)))
        self.assertFalse(Q(0, 0).safe(Q(1, 1)))
        self.assertFalse(Q(0, 0).safe(Q(7, 7)))
        self.assertFalse(Q(1, 1).safe(Q(2, 2)))
        self.assertFalse(Q(1, 0).safe(Q(0, 1)))
        self.assertFalse(Q(7, 7).safe(Q(6, 6)))


    def testQueen(self):
        print (len(eight_queen("")))
        #for x in eight_queen(""):print x


if __name__ == "__main__":
    unittest.main()
