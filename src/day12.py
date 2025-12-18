from src import utils

import array

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.data = array.array('b', [0 for _ in range(width * height)])

    def at(self, i: int, j: int) -> int:
        idx = i * self.width + j
        return self.data[idx]

    def set_value(self, i: int, j: int, value: int):
        idx = i * self.width + j
        self.data[idx] = value

    def ones_count(self):
        if self.width != 3 or self.height != 3:
            raise 'cannot rotate'

        count = 0
        for v in self.data:
            count += v

        return count

    def rotate(self):
        if self.width != 3 or self.height != 3:
            raise 'cannot rotate'

        positions = [(0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]

        for _ in range(2):
            aux = self.at(0, 0)
            for p in positions:
                value = self.at(*p)
                self.set_value(*p, aux)
                aux = value

    def flip(self):
        if self.width != 3 or self.height != 3:
            raise 'cannot flip'

        v1 = self.at(0, 0)
        v2 = self.at(0, 2)
        self.set_value(0, 0, v2)
        self.set_value(0, 2, v1)

        v1 = self.at(1, 0)
        v2 = self.at(1, 2)
        self.set_value(1, 0, v2)
        self.set_value(1, 2, v1)

        v1 = self.at(2, 0)
        v2 = self.at(2, 2)
        self.set_value(2, 0, v2)
        self.set_value(2, 2, v1)

    def shrink_to_fit(self):
        max_col = 0
        max_row = 0

        for i in range(self.height):
            for j in range(self.width):
                if self.at(i, j) == 1:
                    max_row = max(i, max_row)
                    max_col = max(i, max_col)

        self.width = max_col + 1
        self.height = max_row + 1

    def print(self):
        line = ''
        for i in range(self.height):
            for j in range(self.width):
                line += str(self.at(i, j))

        print(line)

    def as_id(self) -> int:
        if self.width != 3 or self.height != 3:
            raise 'cannot get id'

        line = ''
        for i in range(self.height):
            for j in range(self.width):
                line += str(self.at(i, j))

        return int(line, 2)

class Region:
    def __init__(self, width: int, height: int, shape_types: list[int]):
        self.width = width
        self.height = height
        self.shape_types = shape_types

        self.grid = None

    def analyze(self, shapes):
        total_space = self.width * self.height
        relaxed_space = (self.width // 3) * 3 * (self.height // 3) * 3
        max_ocupied = 0
        min_ocupied = 0

        for i, t in enumerate(self.shape_types):
            s = shapes[i]
            max_ocupied += 9 * t
            min_ocupied += s.ones_count() * t

        return total_space, relaxed_space, max_ocupied, min_ocupied

def next_grid_shape(g: Grid):
    flipped = False

    for k in range(0, 4):
        yield k, flipped
        g.rotate()

    s.flip()
    flipped = True

    for k in range(4, 8):
        yield k, flipped
        s.rotate()


def part1():
    file = './inputs/day12-example.txt'
    file = './inputs/day12.txt'

    lines = utils.read_file_lines(file)

    shapes = []
    i = 0

    while True:
        i += 1

        k = 0
        shape = Grid(3, 3)
        while k < 3:
            for j, c in enumerate(lines[i]):
                value = 0 if c == '.' else 1
                shape.set_value(k, j, value)
            k += 1
            i += 1

        shapes.append(shape)
        i += 1

        if len(lines[i].split('x')) > 1:
            break

    regions = []
    for j in range(i, len(lines)):
        size, rshapes = lines[j].split(': ')
        w, h= size.split('x')
        rshapes = map(lambda x: int(x), rshapes.split())

        region = Region(int(w), int(h), rshapes)
        regions.append(region)

    # for s in shapes:
    #     for _ in range(4):
    #         s.print()
    #         s.rotate()

    #     s.flip()
    #     for _ in range(4):
    #         s.print()
    #         s.rotate()

    #     print('--')

    exact_fit_count = 0
    impossible_count = 0
    could_fit_count = 0
    for r in regions:
        total_space, relaxed_space, max_ocupied, min_ocupied = r.analyze(shapes)

        print(f'Available: {total_space}, Relax.: {relaxed_space}, min: {min_ocupied}, max: {max_ocupied}, Could Fit: {min_ocupied < total_space}, Exact Fit: {max_ocupied <= relaxed_space}, Cannot Fit: {min_ocupied > total_space}')

        if max_ocupied <= relaxed_space:
            exact_fit_count += 1
        elif min_ocupied > total_space:
            impossible_count += 1
        else:
            could_fit_count += 1

    print()
    print('Could Fit Count:', could_fit_count);
    print('Exact Fit Count:', exact_fit_count);
    print('Impossible Fit Count:', impossible_count);


