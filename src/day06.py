from src import utils

def part1():
    # filename = './inputs/day06-example.txt'
    filename = './inputs/day06.txt'

    lines = utils.read_file_lines(filename);
    lines = [l.split() for l in lines]

    last = lines.pop()
    lines.insert(0, last)

    problems = [[] for _ in lines[0]]

    for i, line in enumerate(lines):
        for j, col in enumerate(line):
            if i > 0:
                problems[j].append(int(col))
            else:
                problems[j].append(col)

    # print(problems)

    add = lambda a, b: a + b
    mul = lambda a, b: a * b

    result = 0

    for problem in problems:
        if problem[0] == '+':
            op = add
            total = 0
        else:
            op = mul
            total = 1

        for i in range(1, len(problem)):
            total = op(total, problem[i])

        result += total

    print('Result:', result)

def split_numbers(line: str) -> list[str]:
    numbers = []

    num = ''
    reading_digits = False
    skip_spaces = False

    for i in range(len(line)):
        c = line[i]
        if c == '\n' or c == '\r':
            if num != '':
                numbers.append(num)
                num = ''

            break

        if skip_spaces:
            if '0' <= c <= '9':
                skip_spaces = False
                numbers.append(num)
                num = ''
            else:
                num += c
                continue

        if reading_digits:
            if c == ' ':
                reading_digits = False
                skip_spaces = True
            else:
                num += c
        else:
            if '0' <= c <= '9':
                reading_digits = True

            num += c
    
    return numbers

def split_numbers2(line: str, col_sizes: list[int]) -> list[str]:
    numbers = []

    idx = 0
    for size in col_sizes:
        num = line[idx: idx + size]
        idx = idx + size + 1

        numbers.append(num)
    
    return numbers

def part2():
    # filename = './inputs/day06-example.txt'
    filename = './inputs/day06.txt'

    lines = utils.read_file_lines(filename, False);

    values = [line.rstrip().split() for line in lines]
    col_sizes = [0 for _ in values[0]]

    for i, v in enumerate(values):
        for j, e in enumerate(v):
            col_sizes[j] = max(len(e), col_sizes[j])

    last = lines.pop()

    lines = [split_numbers2(l, col_sizes) for l in lines]
    lines.insert(0, last.split())

    problems = [[] for _ in lines[0]]

    for i, line in enumerate(lines):
        for j, col in enumerate(line):
            problems[j].append(col)

    # print(lines)
    # print(problems)

    add = lambda a, b: a + b
    mul = lambda a, b: a * b

    result = 0

    for problem in problems:
        numbers = []

        idx = 0
        while True:
            num = ''

            for i in range(1, len(problem)):
                if idx < len(problem[i]):
                    c = problem[i][idx]

                    if c != ' ':
                        num = num + c

            if num == '':
                break

            numbers.append(int(num))
            idx += 1

        if problem[0] == '+':
            op = add
            total = 0
        else:
            op = mul
            total = 1

        # print(problem[0], numbers)
        for n in numbers:
            total = op(total, n)

        result += total

    print('Result:', result)

