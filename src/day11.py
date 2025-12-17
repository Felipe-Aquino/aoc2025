from src import utils

class Device:
    def __init__(self, name, outputs = []):
        self.name = name
        self.outputs = outputs

        self.path_number = 1 if self.name == 'out' else None

        self.path_number_with_dac_and_fft = None

    def set_outputs(self, outputs):
        self.outputs = outputs

    def print(self, depth = 0):
        count = self.path_number or 0
        print(depth * '  ' + self.name + f' ({count})')

        for o in self.outputs:
            o.print(depth + 1)

    def path_count(self):
        if self.path_number != None:
            return self.path_number

        total = 0
        for o in self.outputs:
            n = o.path_count()

            total += n

        self.path_number = total

        return total

    def path_count_to(self, to: str) -> int:
        if self.path_number != None:
            return self.path_number

        if self.name == to:
            return 1

        total = 0
        for o in self.outputs:
            n = o.path_count_to(to)

            total += n

        self.path_number = total

        return total

def read_devices(lines: list[str]) -> list[Device]:
    devices = []

    for line in lines:
        [name, output_names] = line.split(': ')

        outputs = []

        for output_name in output_names.split(' '):
            out, _ = utils.list_find(devices, lambda d: d.name == output_name)

            if out == None:
                out = Device(output_name)
                devices.append(out)

            outputs.append(out)

        device, _ = utils.list_find(devices, lambda d: d.name == name)

        if device == None:
            device = Device(name, outputs)
            devices.append(device)
        else:
            device.set_outputs(outputs)

    return devices

def part1():
    # file = './inputs/day11-example.txt'
    file = './inputs/day11.txt'

    lines = utils.read_file_lines(file)

    devices = read_devices(lines);
    root, _ = utils.list_find(devices, lambda d: d.name == 'you')

    root.path_count()
    root.print()

    print('Path count:', root.path_number)

def part2():
    # file = './inputs/day11-example2.txt'
    file = './inputs/day11.txt'

    lines = utils.read_file_lines(file)

    devices = read_devices(lines);

    svr, _ = utils.list_find(devices, lambda d: d.name == 'svr')
    fft, _ = utils.list_find(devices, lambda d: d.name == 'fft')
    dac, _ = utils.list_find(devices, lambda d: d.name == 'dac')

    dac_to_out_count = dac.path_count_to('out')

    for d in devices: d.path_number = None
    fft_to_dac_count = fft.path_count_to('dac')

    for d in devices: d.path_number = None
    svr_to_fft_count = svr.path_count_to('fft')

    # print('svr_to_fft_count:', svr_to_fft_count)
    # print('fft_to_dac_count:', fft_to_dac_count)
    # print('dac_to_out_count:', dac_to_out_count)

    result = svr_to_fft_count * fft_to_dac_count * dac_to_out_count
    print('Path count:', result)

