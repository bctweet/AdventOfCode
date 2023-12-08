# Update this value to path to your input file
day1 = open("input/day1input.txt", "r").readlines()


# Solution for first part:
def p1first(line):
    for char in line:
        if char.isnumeric():
            return int(char)
    return 0


def p1second(line):
    return p1first(reversed(line))


# Solution for second part:
def p2first(line):
    text = ""
    for char in line:
        text += char  # Iterates forward to back, returns first instance of either string num or int char
        if "one" in text:
            return 1
        elif "two" in text:
            return 2
        elif "three" in text:
            return 3
        elif "four" in text:
            return 4
        elif "five" in text:
            return 5
        elif "six" in text:
            return 6
        elif "seven" in text:
            return 7
        elif "eight" in text:
            return 8
        elif "nine" in text:
            return 9
        elif char.isnumeric():
            return int(char)
    return 0


def p2second(line):
    text = ""
    for char in reversed(line):
        text = char + text  # Begin building string in reverse, returns either first instance of string num or int char
        if "one" in text:
            return 1
        elif "two" in text:
            return 2
        elif "three" in text:
            return 3
        elif "four" in text:
            return 4
        elif "five" in text:
            return 5
        elif "six" in text:
            return 6
        elif "seven" in text:
            return 7
        elif "eight" in text:
            return 8
        elif "nine" in text:
            return 9
        elif char.isnumeric():
            return int(char)
    return 0


def part1(lines):
    total = 0
    for line in lines:
        total += (10 * p1first(line) + p1second(line))
    return total


def part2(lines):
    total = 0
    for line in lines:
        total += (10 * p2first(line)) + p2second(line)
    return total


print("The solution for Part 1 is: " + str(part1(day1)))
print("The solution for Part 2 is: " + str(part2(day1)))
