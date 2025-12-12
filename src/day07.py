from src import utils

import array
from enum import IntEnum

class Cell(IntEnum):
    Empty = 0
    Beam = 1
    Splitter = 2
    UsedSplitter = 3


def read_diagram(lines: list[str]):
    diagram = []

    for line in lines:
        values = []
        for i, c in enumerate(line):
            value = Cell.Empty.value

            if c == 'S':
                value = Cell.Beam.value
            elif c == '^':
                value = Cell.Splitter.value

            values.append(value)

        diagram.append(values)

    return diagram


def part1():
    # file = './inputs/day07-example.txt'
    file = './inputs/day07.txt'

    lines = utils.read_file_lines(file)

    diagram = read_diagram(lines)

    split_count = 0

    for i in range(0, len(diagram) - 1):
        row = diagram[i]
        next_row = diagram[i + 1]

        for j, col in enumerate(row):
            if Cell.Beam == col:
                next_row_col = next_row[j]

                if Cell.Empty == next_row_col:
                    next_row[j] = Cell.Beam.value
                elif Cell.Splitter == next_row_col:
                    if j > 1 and Cell.Empty == next_row[j - 1]:
                        next_row[j - 1] = Cell.Beam.value
                    if j < len(next_row) - 1 and Cell.Empty == next_row[j + 1]:
                        next_row[j + 1] = Cell.Beam.value

                    next_row[j] = Cell.UsedSplitter.value
                    split_count += 1

    print('Split count:', split_count)

class Node:
    def __init__(self, row, col, id):
        self.id = id
        self.row = row
        self.col = col

        self.lhs = None
        self.rhs = None

        self.print_count = 0
        self.num_branches = 0

    def is_leaf(self):
        return self.lhs == None and self.rhs == None

    def eql(self, row, col):
        return self.row == row and self.col == col

    def print(self, depth = 0):
        pad = depth * ' '

        if self.is_leaf():
            print(f'{pad}Node({self.row}, {self.col}) ({self.num_branches}) - (Leaf)')
        else:
            print(f'{pad}Node({self.row}, {self.col}) ({self.num_branches})')

            if self.print_count > 1:
                print(pad + '...')
                return

            self.print_count += 1

            if self.lhs:
                self.lhs.print(depth + 2)
            else:
                print((depth + 2) * ' ' + 'Leaf')

            if self.rhs:
                self.rhs.print(depth + 2)
            else:
                print((depth + 2) * ' ' + 'Leaf')

    def branch_count(self):
        if self.num_branches:
            return self.num_branches

        if self.is_leaf():
            self.num_branches = 1
            return 1
        else:
            total = 0
            if self.lhs:
                total += self.lhs.branch_count()

            if self.rhs:
                total += self.rhs.branch_count()

            self.num_branches = total
            return total

def part2():
    # file = './inputs/day07-example.txt'
    file = './inputs/day07.txt'

    lines = utils.read_file_lines(file)

    diagram = read_diagram(lines)

    root = None
    nodes = []

    for i in range(0, len(diagram) - 1):
        row = diagram[i]
        next_row = diagram[i + 1]

        for j, col in enumerate(row):
            if Cell.Beam == col:
                if root == None:
                    root = Node(i, j, len(nodes))
                    nodes.append(root)

                next_row_col = next_row[j]

                if Cell.Empty == next_row_col:
                    next_row[j] = Cell.Beam.value
                elif Cell.Beam == next_row_col:
                    for node in nodes:
                        if node.eql(i + 1, j):
                            lhs = node
                            break

                    if lhs == None:
                        for node in nodes:
                            if node.col == j - 1:
                                lhs = node

                    last_node = None
                    for node in nodes:
                        if node.col == j and node.row <= i:
                            last_node = node

                    last_node.lhs = lhs

                elif Cell.Splitter == next_row_col:
                    lhs = None
                    rhs = None

                    if j >= 1:
                        if Cell.Empty == next_row[j - 1]:
                            next_row[j - 1] = Cell.Beam.value
                            lhs = Node(i + 1, j - 1, len(nodes))
                            nodes.append(lhs)
                        elif Cell.Beam == next_row[j - 1]:
                            for node in nodes:
                                if node.eql(i + 1, j - 1):
                                    lhs = node
                                    break

                            if lhs == None:
                                for node in nodes:
                                    if node.col == j - 1:
                                        lhs = node
                                

                    if j <= len(next_row) - 1:
                        if Cell.Empty == next_row[j + 1]:
                            next_row[j + 1] = Cell.Beam.value
                            rhs = Node(i + 1, j + 1, len(nodes))
                            nodes.append(rhs)
                        elif Cell.Beam == next_row[j + 1]:
                            for node in nodes:
                                if node.eql(i + 1, j + 1):
                                    rhs = node
                                    break

                            if rhs == None:
                                for node in nodes:
                                    if node.col == j + 1:
                                        rhs = node

                    next_row[j] = Cell.UsedSplitter.value

                    last_node = None
                    for node in nodes:
                        if node.col == j and node.row <= i:
                            last_node = node

                    last_node.lhs = lhs
                    last_node.rhs = rhs


    total = root.branch_count()
    print('Total:', total)
    # root.print()
