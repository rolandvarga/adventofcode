def solution(start, step):
    with open("2022/day6_input") as f:
        for line in f.read().splitlines():
            for idx in range(start, len(line)):

                chars = set(line[idx - step : idx])
                if len(chars) >= step:
                    print(idx)
                    break


if __name__ == "__main__":
    solution(3, 4)
    solution(13, 14)
