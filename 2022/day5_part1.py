from typing import List

test_stacks: List[List[str]] = [[], ["Z", "N"], ["M", "C", "D"], ["P"]]

prod_stacks: List[List[str]] = [
    [],
    ["P", "F", "M", "Q", "W", "G", "R", "T"],
    ["H", "F", "R"],
    ["P", "Z", "R", "V", "G", "H", "S", "D"],
    ["Q", "H", "P", "B", "F", "W", "G"],
    ["P", "S", "M", "J", "H"],
    [ "M", "Z", "T", "H", "S", "R", "P", "L", ],
    [ "P", "T", "H", "N", "M", "L", ],
    [ "F", "D", "Q", "R", ],
    [ "D", "S", "C", "N", "L", "P", "H", ],
]


def part_1():
    top_crates = ""
    stacks: List[List[str]] = prod_stacks

    with open("2022/day5_input") as f:
        for line in f.read().splitlines():
            repeat, start, end = [int(x) for x in line.split() if x.isdigit()]

            for _ in range(repeat):
                stacks[end].append(stacks[start].pop())

    for stack in stacks:
        if len(stack) > 0:
            top_crates += stack.pop()
    print(top_crates)


if __name__ == "__main__":
    part_1()
