from src import utils

import math

def combine(l, k):
    if k == 0:
        return [[]]

    if len(l) < k:
        return []

    result = []

    while len(l) > 0:
        e = l.pop()
        sub = combine(list(l), k - 1)
        for s in sub:
            s.insert(0, e)
            result.append(s)

    return result
        
def gen_ranges(values):
    stack = [-1]

    while True:
        v = stack.pop()
        depth = len(stack)

        if v > values[depth] - 1:
            if depth == 0:
                break
            else:
                continue

        else:
            v += 1
            stack.append(v)
            if depth != len(values) - 1:
                stack.append(-1)

        if depth == len(values) - 1:
            yield list(stack)

class Machine:
    def __init__(self, data: str):
        parts = data.split()
        light_diagram = 0
        buttons_wiring = []
        joltage_levels = []

        v = parts[0][1:-1]
        for i in range(len(v) - 1, -1, -1):
            c = v[i]
            value = 1 if c == '#' else 0
            light_diagram = (light_diagram << 1) | value

        for item in parts[1:-1]:
            b = 0

            for n in item[1:-1].split(','):
                b = b | 1 << int(n)

            buttons_wiring.append(b)

        for level in parts[-1][1:-1].split(','):
            joltage_levels.append(int(level))

        self.light_diagram = light_diagram
        self.buttons_wiring = buttons_wiring
        self.joltage_levels = joltage_levels

    def print(self):
        print(self.light_diagram, self.buttons_wiring, self.joltage_levels)

    def fewest_total_presses_for_light(self):
        presses = 1

        while presses < len(self.buttons_wiring):
            combinations = combine(list(self.buttons_wiring), presses)

            found = False
            for c in combinations:
                diagram = 0
                for wiring in c:
                    diagram = diagram ^ wiring

                if diagram == self.light_diagram:
                    found = True
                    break

            if found:
                break

            presses += 1

        return presses

    def fewest_total_presses_for_joltage(self):
        epsilon = 1e-9
        data = []

        unknowns_count = len(self.buttons_wiring)

        max_joltage = 0

        for eqn_idx, level in enumerate(self.joltage_levels):
            cols = [0 for i in range(unknowns_count + 1)]

            for j, btns in enumerate(self.buttons_wiring):
                if (1 << eqn_idx) & btns != 0:
                    cols[j] = 1

            cols[unknowns_count] = level

            max_joltage = max(max_joltage, level)

            data.append(cols)

        mtx = utils.Matrix(data)

        # mtx.print()
        mtx.row_echelon_reduce(False)
        # print('after')
        # mtx.print()
        # print('----')

        free_columns = []
        free_columns_max_value = []
        first_empty_row_idx = mtx.nrows
        
        for j in range(mtx.ncols - 1):
            count = 0

            for i in range(mtx.nrows):
                if abs(mtx.at(i, j)) > epsilon:
                    count += 1
                    if count > 1:
                        free_columns.append(j)
                        break

        for i in range(mtx.nrows):
            found = -1

            for j in range(mtx.ncols - 1):
                if abs(mtx.at(i, j)) > epsilon:
                    found = i
                    break

            if found == -1:
                first_empty_row_idx = i
                break

        for col in free_columns:
            max_value = max_joltage

            for i in range(mtx.nrows):
                coef = mtx.at(i, col)

                if coef > 0:
                    value = mtx.at(i, mtx.ncols - 1)

                    v2 = math.ceil(value / coef)
                    max_value = min(v2, max_value)

                # print(i, col, max_value)
            max_value = max(0, max_value)

            # Adding 20 just to be sure
            free_columns_max_value.append(max_value + 20)

        # print(free_columns, free_columns_max_value)

        min_presses = 1e9

        if len(free_columns) > 0:
            for values in gen_ranges(free_columns_max_value):
                presses = 0
                for i, v in enumerate(values):
                    presses += v

                for i in range(first_empty_row_idx):
                    v = mtx.at(i, mtx.ncols - 1)

                    for k, col in enumerate(free_columns):
                        v -= values[k] * mtx.at(i, col)

                    if v < 0 and abs(v) > epsilon:
                        presses = 1e9
                        break
                    
                    v2 = round(v + epsilon)
                    if abs(v - v2) > 0.0001:
                        presses = 1e9
                        break

                    presses += v2

                min_presses = min(min_presses, presses)

                # print(values, presses)

            # print(min_presses, free_columns)
        else:
            presses = 0

            for i in range(first_empty_row_idx):
                v = mtx.at(i, mtx.ncols - 1)
                v2 = round(v)
                presses += v2

                # print(v, v2);

            # print('exact', presses)
            min_presses = presses
                
        return min_presses

    def print_stats(self):
        eqns = len(self.joltage_levels)
        vars = len(self.buttons_wiring)

        if vars > eqns:
            print(f'Equations = {eqns}, variables = {vars}')

def part1():
    # file = './inputs/day10-example.txt'
    file = './inputs/day10.txt'

    lines = utils.read_file_lines(file)

    machines = [Machine(l) for l in lines]

    total_presses = 0
    for m in machines:
        presses = m.fewest_total_presses_for_light()
        total_presses += presses
        # m.print()
        # print(presses)

    print('Fewest presses:', total_presses)

def part2():
    # file = './inputs/day10-example.txt'
    file = './inputs/day10.txt'

    lines = utils.read_file_lines(file)

    machines = [Machine(l) for l in lines]

    total_presses = 0
    for m in machines:
        presses = m.fewest_total_presses_for_joltage()
        total_presses += presses

    print('Fewest presses:', total_presses)

