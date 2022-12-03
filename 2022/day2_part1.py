points = {
    # draw
    "A X": 3,
    "B Y": 3,
    "C Z": 3,
    # win
    "A Y": 6,
    "B Z": 6,
    "C X": 6,
    # lost
    "A Z": 0,
    "B X": 0,
    "C Y": 0,
}

hand = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def part_1():
    score = 0
    with open("2022/day2_input") as f:
        contents = f.read().splitlines()

        for line in contents:
            score += points[line] + hand[line[-1]]

    print(score)

if __name__ == '__main__':
    part_1()