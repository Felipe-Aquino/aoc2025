def read_file_lines(filename: str, rstrip: bool = True) -> list[str]:
    lines = []
    with open(filename) as file:
        if rstrip:
            lines = [line.rstrip() for line in file]
        else:
            lines = [line for line in file]

    return lines
