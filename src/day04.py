from src import utils
import array

def part1():
    # filename = './inputs/day04-example.txt'
    filename = './inputs/day04.txt'

    lines = utils.read_file_lines(filename);
    col_size = len(lines[0])
    lines_size = len(lines)

    accessable_rolls_count = 0

    for i in range(lines_size):
        line = lines[i]

        for j in range(col_size):
            if line[j] == '@':
                roll_count = 0

                if j > 0 and lines[i][j - 1] == '@':
                    roll_count += 1
                if j < col_size - 1 and lines[i][j + 1] == '@':
                    roll_count += 1

                if i > 0:
                    prev = lines[i - 1]
                    if prev[j] == '@':
                        roll_count += 1

                    if j > 0 and prev[j - 1] == '@':
                        roll_count += 1
                    if j < col_size - 1 and prev[j + 1] == '@':
                        roll_count += 1

                if i < lines_size - 1:
                    next = lines[i + 1]
                    if next[j] == '@':
                        roll_count += 1

                    if j > 0 and next[j - 1] == '@':
                        roll_count += 1
                    if j < col_size - 1 and next[j + 1] == '@':
                        roll_count += 1

                if roll_count < 4:
                    accessable_rolls_count += 1

    print('Total accessable rolls:', accessable_rolls_count)

def count_remove_and_accessable_rolls(lines, nlines, ncols):
    accessable_rolls_count = 0

    remove_list = []

    for i in range(nlines):
        line = lines[i]

        for j in range(ncols):
            if line[j] == 1:
                roll_count = 0

                if j > 0 and lines[i][j - 1] == 1:
                    roll_count += 1
                if j < ncols - 1 and lines[i][j + 1] == 1:
                    roll_count += 1

                if i > 0:
                    prev = lines[i - 1]
                    if prev[j] == 1:
                        roll_count += 1

                    if j > 0 and prev[j - 1] == 1:
                        roll_count += 1
                    if j < ncols - 1 and prev[j + 1] == 1:
                        roll_count += 1

                if i < nlines - 1:
                    next = lines[i + 1]
                    if next[j] == 1:
                        roll_count += 1

                    if j > 0 and next[j - 1] == 1:
                        roll_count += 1
                    if j < ncols - 1 and next[j + 1] == 1:
                        roll_count += 1

                if roll_count < 4:
                    accessable_rolls_count += 1
                    remove_list.append((i, j))

    for i, j in remove_list:
        lines[i][j] = 0

    return accessable_rolls_count

def part2():
    # filename = './inputs/day04-example.txt'
    filename = './inputs/day04.txt'

    lines = utils.read_file_lines(filename);
    lines = [array.array('i', [0 if c == '.' else 1 for c in l]) for l in lines]

    col_size = len(lines[0])
    lines_size = len(lines)

    removed_rolls_count = 0

    while True:
        count = count_remove_and_accessable_rolls(lines, lines_size, col_size)
        removed_rolls_count += count

        # print('--', count)
        if count == 0:
            break

    print('Total rolls removed:', removed_rolls_count)

