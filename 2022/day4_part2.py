from typing import List, Set


def list_sections_from(line) -> List[Set[int]]:
    sections: List[Set[int]] = []
    for section in line.split(","):
        start, end = [int(x) for x in section.split("-")]
        sections.append(set(list(range(start, end + 1))))
    return sections


def part_2():
    overlap_count = 0
    with open("2022/day4_input") as f:
        for line in f.read().splitlines():
            section_1, section_2 = list_sections_from(line)

            if len(section_1.intersection(section_2)) > 0:
                overlap_count += 1

    print(overlap_count)


if __name__ == "__main__":
    part_2()
