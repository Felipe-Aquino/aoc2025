from src import utils

def part1():
    # file = './inputs/day09-example.txt'
    file = './inputs/day09.txt'

    lines = utils.read_file_lines(file)

    red_tiles = list(map(
        lambda x: (int(x[0]), int(x[1])),
        [l.split(',') for l in lines]
    ))

    max_area = 0

    tiles_count = len(red_tiles)

    for i in range(tiles_count):
        x1, y1 = red_tiles[i]

        for j in range(i + 1, tiles_count):
            x2, y2 = red_tiles[j]

            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

            if area > max_area:
                max_area = area

    print('Largest area:', max_area);

class Rect:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x = min(x1, x2)
        self.y = min(y1, y2)
        self.w = abs(x1 - x2) + 1
        self.h = abs(y1 - y2) + 1

    def contains(self, x: int, y: int) -> bool:
        """Test if point is inside the rectangle but not in borders"""

        return (0 < (x - self.x) < (self.w - 1)) and (0 < (y - self.y) < (self.h - 1))

    def area(self):
        return self.w * self.h

def part2():
    # file = './inputs/day09-example.txt'
    file = './inputs/day09.txt'

    lines = utils.read_file_lines(file)

    red_tiles = list(map(
        lambda x: (int(x[0]), int(x[1])),
        [l.split(',') for l in lines]
    ))

    max_area = 0

    tiles_count = len(red_tiles)

    gone = []
    values = []

    polygon = [red_tiles[0]]
    tiles = red_tiles[1:]

    vertical = False
    while len(tiles) > 0:
        x, y = polygon[-1]

        ok = False
        for k in range(len(tiles)):
            x0, y0 = tiles[k]
            found = (not vertical and x == x0) or (vertical and y == y0)

            if found:
                ok = True
                vertical = not vertical
                polygon.append(tiles[k])
                tiles.remove(tiles[k])
                break

        if not ok:
            print('Incomplete polygon', polygon)
            return

    polygon.append(polygon[0])

    for i in range(tiles_count):
        x1, y1 = red_tiles[i]

        for j in range(i + 1, tiles_count):
            x2, y2 = red_tiles[j]

            rect = Rect(x1, y1, x2, y2)

            # Testing if mid point of a segment in polygon is inside rectangle
            is_valid = True
            for k in range(len(polygon) - 1):
                xp1, yp1 = polygon[k]
                xp2, yp2 = polygon[k + 1]
                x = (xp1 + xp2) / 2
                y = (yp1 + yp2) / 2
                
                if rect.contains(x, y):
                    is_valid = False
                    break


            if is_valid:
                area = rect.area()

                if area > max_area:
                    max_area = area

    print('Largest area:', max_area);

