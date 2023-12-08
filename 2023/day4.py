import re

# Update this value to path to your input file
inputpath = "input/day4input.txt"

day4 = open(inputpath, "r").readlines()


def part1(lines):
    res = 0
    for line in lines:
        split = re.split('[:|]', line)
        winners = split[1].split()
        nums = split[2].split()
        winningnums = len(set(nums) & set(winners))
        if winningnums > 0:
            res += pow(2, winningnums - 1)
    return res


def part2(lines):
    cards = {}
    for idx, line in enumerate(lines):
        if idx not in cards:
            cards[idx] = 1
        split = re.split('[:|]', line)
        winners = split[1].split()
        nums = split[2].split()
        winningnums = len(set(nums) & set(winners))
        for remaining in range(idx + 1, idx + winningnums + 1):
            cards[remaining] = cards.get(remaining, 1) + cards[idx]
    return sum(cards.values())


print("Solution for Part 1: " + str(part1(day4)))
print("Solution for Part 2: " + str(part2(day4)))
