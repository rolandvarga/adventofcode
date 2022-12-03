import sys
import string
from typing import Dict, List, NamedTuple


class Rucksack(NamedTuple):
    compartment_one: List[str]
    compartment_two: List[str]


def build_rucksack_from_line(line: str) -> Rucksack:
    return Rucksack(
        list(line[:len(line) // 2]),
        list(line[len(line) // 2:]),
    )

def load_all_rucksacks() -> List[Rucksack]:
    # with open("day3_test_input") as f:
    with open("day3_input") as f:
        for line in f.read().splitlines():
            yield build_rucksack_from_line(line)


def populate_priority_index() -> Dict[str, int]:
    priority_index: Dict[str, int] = {}
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)

    for idx, char in enumerate(lowercase + uppercase):
        priority_index[char] = idx + 1

    return priority_index


def count_item_types_in(compartment: List[str]) -> Dict[str, int]:
    item_count: Dict[str, int] = {}
    for char in compartment:
        item_count[char] = item_count.get(char, 0) + 1

    return item_count


def part_1():
    priority_sum = 0
    priority_index = populate_priority_index()
    rucksacks: List[Rucksack] = list(load_all_rucksacks())

    for rucksack in rucksacks:
        item_count = count_item_types_in(rucksack.compartment_one)

        for item in rucksack.compartment_two:
            if item in item_count:
                priority_sum += priority_index[item]
                break

    print(priority_sum)


if __name__ == '__main__':
    part_1()