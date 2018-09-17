class CicledList(list):
    """If index put of range -> go to other side of list"""
    def __init__(self, seq=()):
        super().__init__(seq)

    def __getitem__(self, item):
        # print('item: ', item, 'Res: ', len(self) % (item + 1))
        return list.__getitem__(self, item % len(self))


class LifeGame:
    """Conway's Game of Life on torus surface"""

    def __init__(self): #, height):
        # self.height = height
        self.matrix = CicledList()
        self.next_matrix = CicledList()
        # for _ in range(height):
        #     self.matrix.append(CicledList())

    def append_line(self, line):
        """Expect list of 1 and 0 with equal lengt"""
        self.matrix.append(CicledList(line))
        self.next_matrix.append(CicledList(line))

    def __str__(self):
        return 'Game position:\n' + self.print()

    def print(self, live='1', dead='0'):
        """Return string representation"""
        out = ''
        for i in range(len(self.matrix)):
            out += ''.join([live if x else dead for x in self.matrix[i]])
            out += '\n'
        return out

    def count_cell(self, i, j):
        """Count live and dead cells around current cell
        Return dict('live': X, 'dead': Y)"""

        result = {'live': 0, 'dead': 0}
        for ik in range(3):
            for jk in range(3):
                ii = i - 1 + ik
                jj = j - 1 + jk
                if ii == i and jj == j:
                    continue

                if self.matrix[ii][jj]:
                    result['live'] += 1
                else:
                    result['dead'] += 1
        return result

    def process_cell(self, i, j):
        """Count cells around current cell and change its status"""

        self.next_matrix[i][j] = self.matrix[i][j]

        state = self.count_cell(i, j)
        if not self.matrix[i][j] and state['live'] == 3:
            self.next_matrix[i][j] = True
        elif self.matrix[i][j] and (state['live'] > 3 or state['live'] < 2):
            self.next_matrix[i][j] = False

    def next_step(self):
        """Form next step"""

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                # print(i, j)
                self.process_cell(i, j)

        self.matrix = self.next_matrix.copy()

lg = LifeGame()
h, w = [int(x) for x in input().split()]
# print(h, w)

for i in range(h):
    lg.append_line([x != '.' for x in input()])

# print(lg)

lg.next_step()

# print(lg)
print(lg.print('X', '.'))
