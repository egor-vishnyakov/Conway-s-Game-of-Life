from CicledList import CicledList

class LifeGame:
    """Conway's Game of Life on torus surface"""

    def __init__(self):
        self.matrix = CicledList()
        self.next_matrix = CicledList()

    def append_line(self, line):
        """Expect list of 1 and 0 with equal lengt"""
        self.matrix.append(CicledList(line))
        self.next_matrix.append(CicledList(line))

    def full(self, x, y, cell):
        """Create matrix x*y full of cell(True or False)"""
        self.matrix.clear()
        self.next_matrix.clear()

        for j in range(y):
            line = []
            for i in range(x):
                line.append(cell)
            self.append_line(line)

    def zeros(self, x, y):
        """Create matrix x*y full of dead cells"""
        self.full(x, y, False)

    def ones(self, x, y):
        """Create matrix x*y full of live cells"""
        self.full(x, y, True)

    def vitalize(self, x, y):
        """Set cell[x][y] to live state"""
        self.matrix[x][y] = True

    def kill(self, x, y):
        """Set cell[x][y] to dead state"""
        self.matrix[x][y] = False

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
        """Count live cells around current cell"""

        live = 0
        for ik in range(3):
            for jk in range(3):
                ii = i - 1 + ik
                jj = j - 1 + jk
                if ii == i and jj == j:
                    continue

                if self.matrix[ii][jj]:
                    live += 1

        return live

    def process_cell(self, i, j):
        """Count cells around current cell and change its status"""

        self.next_matrix[i][j] = self.matrix[i][j]

        live = self.count_cell(i, j)
        if not self.matrix[i][j] and live == 3:
            self.next_matrix[i][j] = True
        elif self.matrix[i][j] and (live > 3 or live < 2):
            self.next_matrix[i][j] = False

    def next_step(self):
        """Form next step"""

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.process_cell(i, j)

        self.matrix = self.next_matrix.copy()

    def run(self, count=1):
        """Iterable steps"""
        for _ in range(count):
            self.next_step()
            yield self.print()

    def get_raw(self):
        return self.matrix

    def set_glider(self, x, y):
        """Set position to glider on field x*y"""
        self.zeros(x, y)
        self.vitalize(0, 1)
        self.vitalize(1, 2)
        self.vitalize(2, 0)
        self.vitalize(2, 1)
        self.vitalize(2, 2)

    def set_r_pentamino(self, x, y):
        """Set position to R-pentamino on field x*y"""
        self.zeros(x, y)
        hx = x // 2
        hy = y // 2
        self.vitalize(hx + 3, hy + 2)
        self.vitalize(hx + 3, hy + 3)
        self.vitalize(hx + 4, hy + 1)
        self.vitalize(hx + 4, hy + 2)
        self.vitalize(hx + 5, hy + 2)

    def read_file(self, filename):
        """Read configuration from file where 'X' or 'x' for live cell and '0' for dead"""
        self.matrix.clear()
        self.next_matrix.clear()

        with open(filename) as file:
            for line in file:
                added_line = []
                for i in line:
                    if i == 'X' or i == 'x':
                        added_line.append(True)
                    elif i == '0':
                        added_line.append(False)
                self.append_line(added_line)
