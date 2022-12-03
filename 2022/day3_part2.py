import sys
import string
from typing import Dict, List, NamedTuple, Set


class Group(NamedTuple):
    rucksack_one: Set[str]
    rucksack_two: Set[str]
    rucksack_three: Set[str]


def populate_groups() -> List[Group]:
    with open("2022/day3_input") as f:
        contents = f.read().splitlines()

        for idx in range(0, len(contents), 3):
            yield Group(
                set(contents[idx]),
                set(contents[idx + 1]),
                set(contents[idx + 2]),
            )


def populate_priority_index() -> Dict[str, int]:
    priority_index: Dict[str, int] = {}
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)

    for idx, char in enumerate(lowercase + uppercase):
        priority_index[char] = idx + 1

    return priority_index


def part_2():
    priority_sum = 0
    priority_index = populate_priority_index()
    groups: List[Group] = list(populate_groups())

    for group in groups:
        badge = group.rucksack_one & group.rucksack_two & group.rucksack_three
        priority_sum += priority_index[badge.pop()]

    print(priority_sum)


if __name__ == '__main__':
    part_2()