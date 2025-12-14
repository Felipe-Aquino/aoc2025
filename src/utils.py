import array

def read_file_lines(filename: str, rstrip: bool = True) -> list[str]:
    lines = []
    with open(filename) as file:
        if rstrip:
            lines = [line.rstrip() for line in file]
        else:
            lines = [line for line in file]

    return lines

class Matrix:
    def __init__(self, data: list[list[int]]):
        self.nrows = len(data)
        self.ncols = len(data[0])

        rows = []
        for r in data:
            rows = rows + r

        self.data = array.array('d', rows)

    def at(self, i, j):
        idx = i * self.ncols + j
        return self.data[idx]

    def print(self):
        for i in range(self.nrows):
            row = ''
            for j in range(self.ncols):
                value = self.at(i, j)
                row += str(value) + ' '

            print(row)

    def row_swap(self, i, j):
        i = i * self.ncols
        j = j * self.ncols

        for _ in range(self.ncols):
            self.data[i], self.data[j] = self.data[j], self.data[i]

            i += 1
            j += 1

    def row_mult(self, i, c):
        i = i * self.ncols

        for _ in range(self.ncols):
            self.data[i] = c * self.data[i]

            i += 1

    def row_mult_n_add(self, i, j, ci = 1, cj = 1):
        i = i * self.ncols
        j = j * self.ncols

        for _ in range(self.ncols):
            aux = ci * self.data[i] + cj * self.data[j]
            self.data[i] = aux

            i += 1
            j += 1

    def row_echelon_reduce(self, reduce_last_column = True):
        # When solving Ax = b, b could added as an addional column
        # to make solution finding easier
        offset = 0 if reduce_last_column else 1

        count = min(self.nrows, self.ncols - offset)
        row_pivot_idx, col_pivot_idx = 0, 0

        while row_pivot_idx < self.nrows and col_pivot_idx < (self.ncols - offset):
            pivot_value = self.at(row_pivot_idx, col_pivot_idx)

            max_pivot_value = abs(pivot_value)
            max_pivot_idx = row_pivot_idx

            for i in range(row_pivot_idx + 1, self.nrows):
                value = abs(self.at(i, col_pivot_idx))

                if max_pivot_value < value:
                    max_pivot_value = value
                    max_pivot_idx = i
                    
            if row_pivot_idx != max_pivot_idx:
                self.row_swap(row_pivot_idx, max_pivot_idx)
                pivot_value = self.at(row_pivot_idx, col_pivot_idx)

            if pivot_value == 0 or abs(pivot_value) < 1e-9:
                col_pivot_idx += 1
                continue

            self.row_mult(row_pivot_idx, 1 / pivot_value)

            for i in range(self.nrows):
                if i != row_pivot_idx:
                    value = self.at(i, col_pivot_idx)
                    self.row_mult_n_add(i, row_pivot_idx, 1, -value)

            row_pivot_idx += 1
            col_pivot_idx += 1

