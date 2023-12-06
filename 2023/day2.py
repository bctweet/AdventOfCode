import re

day2 = open("input/day2input.txt", "r").readlines()


def part1(lines):
    sum = 0
    for line in lines:
        split = re.split('[;:]', line.strip())
        id = int(split.pop(0).split(" ")[1])
        isValid = True
        for handfuls in split:
            for handful in handfuls.split(","):
                cubes = handful.split(" ")
                count = int(cubes[1])
                color = cubes[2]
                if count > 12 and color == "red":
                    isValid = False
                elif count > 13 and color == "green":
                    isValid = False
                elif count > 14 and color == "blue":
                    isValid = False
        if isValid:
            sum += id
    return sum


def part2(lines):
    sum = 0
    for line in lines:
        red, blue, green = 1, 1, 1
        split = re.split('[;:]', line.strip())
        split.pop(0)
        for handfuls in split:
            for handful in handfuls.split(","):
                cubes = handful.split(" ")
                count = int(cubes[1])
                color = cubes[2]
                if color == "red":
                    red = max(red, count)
                elif color == "blue":
                    blue = max(blue, count)
                elif color == "green":
                    green = max(green, count)
        sum += red * blue * green
    return sum


print("Solution for Part 1: " + str(part1(day2)))
print("Solution for Part 2: " + str(part2(day2)))
