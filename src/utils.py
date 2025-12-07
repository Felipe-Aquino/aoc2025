def read_file_lines(filename: str) -> list[str]:
    lines = []
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    return lines
