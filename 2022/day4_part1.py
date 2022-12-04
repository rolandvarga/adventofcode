from typing import List, NamedTuple


def list_sections_from(line):
    sections = []
    for section in line.split(","):
        start, end = [int(x) for x in section.split("-")]
        sections.append(list(range(start, end + 1)))
    return sections


def part_1():
    overlap_count = 0
    with open("2022/day4_input") as f:
        for line in f.read().splitlines():
            section_1, section_2 = list_sections_from(line)

            if (
                section_1[0] <= section_2[0] and section_1[-1] >= section_2[-1]
            ) or (
                section_2[0] <= section_1[0] and section_2[-1] >= section_1[-1]
            ):
                overlap_count += 1

    print(overlap_count)


if __name__ == "__main__":
    part_1()
