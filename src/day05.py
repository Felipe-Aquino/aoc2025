from src import utils

from functools import reduce

def parse_range(s: str) -> tuple[int, int]:
    [start, end] = s.split('-')

    return int(start), int(end)

def read_input_lines(filename: str) -> tuple[list[int], tuple[int, int]]:
    lines = utils.read_file_lines(filename);
    idx = lines.index('')

    ranges = [parse_range(e) for e in lines[:idx]]
    ids = [int(e) for e in lines[idx + 1:]]

    return ids, ranges

def part1():
    # filename = './inputs/day05-example.txt'
    filename = './inputs/day05.txt'

    ids, ranges = read_input_lines(filename)

    fresh_count = 0

    for id in ids:
        for (start, end) in ranges:
            if start <= id <= end:
                fresh_count += 1
                break

    print('Fresh count:', fresh_count)

def part2():
    # filename = './inputs/day05-example.txt'
    filename = './inputs/day05.txt'

    _, ranges = read_input_lines(filename)

    ranges.sort() # it sorts by the first element of the tuple

    new_ranges = []
    
    new_ranges.append(ranges[0])

    for (s1, e1) in ranges:
        s2, e2 = new_ranges[-1]

        if s2 <= s1 <= e2:
            new_ranges[-1] = min(s1, s2), max(e1, e2)
        else:
            new_ranges.append((s1, e1))

    # print(ranges)
    # print(new_ranges)
    fresh_count = reduce(lambda total, r: total + r[1] - r[0] + 1, new_ranges, 0)

    print('Fresh count:', fresh_count)
