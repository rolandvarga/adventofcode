outcome = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

outcome_points = {
    "lose": 0,
    "draw": 3,
    "win": 6,
}

play = {
    "A": {
        "lose": "C",
        "draw": "A",
        "win": "B",
    },
    "B": {
        "lose": "A",
        "draw": "B",
        "win": "C",
    },
    "C": {
        "lose": "B",
        "draw": "C",
        "win": "A",
    },
}

hand_points = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def part_2():
    score = 0
    with open("day2_input") as f:
        contents = f.read().splitlines()

        for line in contents:
            hand_a, hand_b = line.split(" ")
            hand = play[hand_a][outcome[hand_b]]
            score += outcome_points[outcome[hand_b]] + hand_points[hand]
        
    print(score)

if __name__ == '__main__':
    part_2()