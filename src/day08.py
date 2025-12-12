from src import utils

from itertools import count

_id = count(0)

def next_id():
    return next(_id)

def dist2(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> int:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2) + (z1 - z2) * (z1 - z2)

class Circuit:
    def __init__(self):
        self.id = next_id()
        self.points = []

    def has(self, p: tuple[int, int, int]) -> bool:
        return p in self.points

    def add(self, p: tuple[int, int, int]):
        self.points.append(p)
    
    def join(self, c):
        for p in c.points:
            self.points.append(p)

        c.points = []

    def count(self):
        return len(self.points)

def part1():
    # file = './inputs/day08-example.txt'
    file = './inputs/day08.txt'

    lines = utils.read_file_lines(file)
    points = [
        tuple(
            map(lambda v: int(v), line.split(','))
        ) for line in lines
    ]

    distances = []

    point_count = len(points)
    for i in range(point_count):
        p1 = points[i]
        for j in range(i + 1, point_count):
            p2 = points[j]
            
            d = dist2(p1, p2)
            distances.append((d, p1, p2))

    distances.sort()

    circuits = []
    c0 = Circuit()
    c0.add(distances[0][1])
    c0.add(distances[0][2])

    circuits.append(c0)

    # print(distances)

    # connections_amount = 1000
    connections_amount = 1000

    for i in range(1, connections_amount):
        _, p1, p2 = distances[i]

        c1 = None
        for c in circuits:
            if c.has(p1):
                c1 = c
                break

        c2 = None
        for c in circuits:
            if c.has(p2):
                c2 = c
                break

        if c1 and c2:
            if c1 != c2:
                c1.join(c2)
                circuits.remove(c2)
        elif c1:
            c1.add(p2)
        elif c2:
            c2.add(p1)
        else:
            c0 = Circuit()
            c0.add(p1)
            c0.add(p2)
            circuits.append(c0)

    circuits.sort(key=lambda c: len(c.points))
    circuits.reverse()

    [c1, c2, c3] = circuits[:3]

    result = c1.count() * c2.count() * c3.count()

    print('Result:', result)

def part2():
    # file = './inputs/day08-example.txt'
    file = './inputs/day08.txt'

    lines = utils.read_file_lines(file)
    points = [
        tuple(
            map(lambda v: int(v), line.split(','))
        ) for line in lines
    ]

    distances = []

    point_count = len(points)
    for i in range(point_count):
        p1 = points[i]
        for j in range(i + 1, point_count):
            p2 = points[j]
            
            d = dist2(p1, p2)
            distances.append((d, p1, p2))

    distances.sort()

    circuits = []
    c0 = Circuit()
    c0.add(distances[0][1])
    c0.add(distances[0][2])

    circuits.append(c0)

    # print(distances)

    result = 0
    i = 0

    while True:
        _, p1, p2 = distances[i]

        c1 = None
        for c in circuits:
            if c.has(p1):
                c1 = c
                break

        c2 = None
        for c in circuits:
            if c.has(p2):
                c2 = c
                break

        if c1 and c2:
            if c1 != c2:
                c1.join(c2)
                circuits.remove(c2)

            c0 = c1
        elif c1:
            c1.add(p2)
            c0 = c1
        elif c2:
            c2.add(p1)
            c0 = c2
        else:
            c0 = Circuit()
            c0.add(p1)
            c0.add(p2)
            circuits.append(c0)
        
        if c0.count() >= point_count:
            print(p1)
            print(p2)
            result = p1[0] * p2[0]
            break

        i += 1

    print('Result:', result)

