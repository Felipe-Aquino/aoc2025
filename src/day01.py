from src import utils

def parse_rotations(lines: list[str]) -> list[tuple[str, int]]:
    rotations = []

    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        rotations.append((direction, amount))

    return rotations

def part1():
    file = './inputs/day01.txt'
    # file = './inputs/day01-example.txt'

    lines = utils.read_file_lines(file)
    rotations = parse_rotations(lines)

    dial_position = 50

    password = 0

    for r in rotations:
        direction, amount = r

        amount = amount % 100

        if direction == 'L':
            dial_position = (dial_position + 100 - amount) % 100
        else:
            dial_position = (dial_position + amount) % 100

        if dial_position == 0:
            password += 1

    print('Password:', password)

def part2():
    file = './inputs/day01.txt'
    # file = './inputs/day01-example.txt'

    lines = utils.read_file_lines(file)
    rotations = parse_rotations(lines)

    dial_position = 50

    password = 0

    for r in rotations:
        direction, amount = r

        full_rotations = amount // 100
        amount = amount % 100

        password += full_rotations

        if amount == 0:
            continue

        start_position = dial_position

        if direction == 'L':
            dial_position = (dial_position + 100 - amount) % 100

            if 0 < start_position < dial_position:
                password += 1

            if dial_position == 0:
                password += 1
        else:
            dial_position = (dial_position + amount) % 100

            if start_position > dial_position:
                password += 1

        # print(r, start_position, dial_position, password)

    print('Password:', password)

