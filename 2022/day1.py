def part_1():
    with open('day1_input', 'r') as f:
        data = f.read().splitlines()

        max_calories = 0
        last = 0

        for idx, line in enumerate(data):
            if line == "":
                calories = 0
                for i in range(last + 1, idx):
                    calories += int(data[i])

                if calories > max_calories:
                    max_calories = calories

                last = idx

        print(max_calories)


def part_2():
    with open('day1_input', 'r') as f:
        data = f.read().splitlines()

        all_calories = []
        last = 0

        for idx, line in enumerate(data):
            if line == "":
                calories = 0
                for i in range(last + 1, idx):
                    calories += int(data[i])

                all_calories.append(calories)

                last = idx

        print(sum(sorted(all_calories, reverse=True)[:3]))



if __name__ == '__main__':
    part_1()
    part_2()