import os
import importlib

def print_usage():
    print('python3 run.py <day-number>.<part>')
    print('  day-number: int   which day to run')
    print('  part: int         which part of the day')
    print('  Example: python3 run.py 01.2')

if __name__ == '__main__':
    try:
        day_part = os.sys.argv[1]
        [day, part] = day_part.split('.')

        int(day) # asserting that is an integer
        int(part) # asserting that is an integer

        file = f'src.day{day}'
        filename = f'./src/day{day}.py'
        function_name = f'part{part}'

        if os.path.exists(filename):
            m = importlib.import_module(file)

            if function_name in dir(m):
                function = getattr(m, function_name)
                function()
            else:
                print(f'Function {function_name} does not exists in file {filename}!')
        else:
            print(f'File {filename} does not exists!')
    except e:
        print(e)
        print_usage()

