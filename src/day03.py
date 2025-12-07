from src import utils

def part1():
    # filename = './inputs/day03-example.txt'
    filename = './inputs/day03.txt'

    lines = utils.read_file_lines(filename);

    total_joltage = 0

    for line in lines:
        battery1_idx = 0
        battery2_idx = 0

        max_value = 0 # battery value is from 1 to 9

        for i in range(0, len(line) - 1):
            value = int(line[i])

            if value > max_value:
                max_value = value
                battery1_idx = i

        max_value = 0

        for i in range(battery1_idx + 1, len(line)):
            value = int(line[i])

            if value > max_value:
                max_value = value
                battery2_idx = i

        bank_joltage = line[battery1_idx] + line[battery2_idx]
        
        total_joltage += int(bank_joltage)

        # print('--', bank_joltage)

    print('Total joltage:', total_joltage)

def part2():
    # filename = './inputs/day03-example.txt'
    filename = './inputs/day03.txt'

    lines = utils.read_file_lines(filename);

    total_joltage = 0

    for line in lines:
        if len(line) >= 12:
            bank_joltage = ''
            count = 0

            idx = 0

            while count < 12:
                max_value = 0 # battery value is from 1 to 9

                for i in range(idx, len(line) - 11 + count):
                    value = int(line[i])

                    if value > max_value:
                        max_value = value
                        idx = i

                bank_joltage = bank_joltage + line[idx]
                count += 1
                idx += 1

            # print('--', bank_joltage)
            total_joltage += int(bank_joltage)


    print('Total joltage:', total_joltage)

