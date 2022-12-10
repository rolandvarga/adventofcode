from typing import List


def part_1():
    with open("2022/day8_input") as f:
        # with open("2022/day8_test_input") as f:
        contents = f.read().splitlines()

        grid = []

        for line in contents:
            grid.append([int(c) for c in line])

        visible_count = 0

        # add trees from perimeter
        visible_count += len(grid[0]) * 2
        visible_count += (len(grid) - 2) * 2

        print(visible_count)

        for (row_idx, row) in enumerate(grid):
            if row_idx == 0 or row_idx == len(grid) - 1:
                continue
            # print("------\n{} {}".format(row_idx, row))

            for (col_idx, col) in enumerate(row):
                if col_idx == 0 or col_idx == len(row) - 1:
                    continue

                horizontal_cols = row.copy()
                if max(horizontal_cols[:col_idx]) < col:
                    visible_count += 1
                    continue

                if max(horizontal_cols[col_idx + 1 :]) < col:
                    visible_count += 1
                    continue

                vertical_cols = [r[col_idx] for r in grid]
                if max(vertical_cols[:row_idx]) < col:
                    visible_count += 1
                    continue

                if max(vertical_cols[row_idx + 1 :]) < col:
                    visible_count += 1
                    continue

                print(
                    "{} {} {} {}".format(
                        col_idx, col, horizontal_cols, vertical_cols
                    )
                )

        print(visible_count)


if __name__ == "__main__":
    part_1()
