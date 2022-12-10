from typing import List


def part_1():
    with open("2022/day8_input") as f:
        # with open("2022/day8_test_input") as f:
        contents = f.read().splitlines()

        grid = []

        for line in contents:
            grid.append([int(c) for c in line])

        max_scenic_score = 0

        for (row_idx, row) in enumerate(grid):
            if row_idx == 0 or row_idx == len(grid) - 1:
                continue

            for (col_idx, col) in enumerate(row):
                if col_idx == 0 or col_idx == len(row) - 1:
                    continue

                horizontal_cols = row.copy()

                visible_left = 0
                for i in range(len(horizontal_cols[:col_idx]) - 1, -1, -1):
                    if horizontal_cols[i] < col:
                        visible_left += 1
                    if horizontal_cols[i] == col:
                        visible_left += 1
                        break

                visible_right = 0
                for num in horizontal_cols[col_idx + 1 :]:
                    if num < col:
                        visible_right += 1
                    if num == col:
                        visible_right += 1
                        break

                vertical_cols = [row[col_idx] for row in grid]

                visible_up = 0
                for i in range(len(vertical_cols[:row_idx]) - 1, -1, -1):
                    if vertical_cols[i] < col:
                        visible_up += 1
                    if vertical_cols[i] == col:
                        visible_up += 1
                        break

                visible_down = 0
                for num in vertical_cols[row_idx + 1 :]:
                    if num < col:
                        visible_down += 1
                    if num == col:
                        visible_down += 1
                        break

                scenic_score = (
                    visible_left * visible_right * visible_up * visible_down
                )

                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score

        print(max_scenic_score)


if __name__ == "__main__":
    part_1()
