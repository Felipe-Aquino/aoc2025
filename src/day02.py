from src import utils

def parse_ranges(line: str) -> list[tuple[int, int]]:
    ranges = []

    splits = line.split(',')

    for s in splits:
        [start, end] = s.split('-')

        ranges.append((int(start), int(end)))

    return ranges

def part1():
    file = './inputs/day02.txt'
    # file = './inputs/day02-example.txt'

    lines = utils.read_file_lines(file)
    ranges = parse_ranges(lines[0])

    invalid_list = []
    total = 0

    for (s, e) in ranges:
        for n in range(s, e + 1):
            v = str(n)

            size = len(v)
            if size % 2 == 0:
                idx = size // 2
                v1 = v[:idx]
                v2 = v[idx:]

                if v1 == v2:
                    invalid_list.append(n)
                    total += n

    # print(invalid_list)
    print('Result:', total)

def part2():
    file = './inputs/day02.txt'
    # file = './inputs/day02-example.txt'

    lines = utils.read_file_lines(file)
    ranges = parse_ranges(lines[0])

    invalid_list = []
    total = 0

    for (s, e) in ranges:
        for n in range(s, e + 1):
            v = str(n)

            total_size = len(v)
            for window_size in range(1, 1 + total_size // 2):
                found = False

                if total_size % window_size == 0:
                    window_str = v[0: window_size]

                    idx = window_size
                    found = True

                    while idx < total_size:
                        test_str = v[idx: idx + window_size]
                        if test_str != window_str:
                            found = False
                            break

                        idx += window_size

                if found:
                    invalid_list.append(n)
                    total += n
                    break

    # print(invalid_list)
    print('Result:', total)

