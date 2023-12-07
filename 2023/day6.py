import math

day6 = open("input/day6input.txt", "r").readlines()

t = day6[0].strip().split(":")[1].strip().split()
d = day6[1].strip().split(":")[1].strip().split()


def part1(times, distances):
    winners = {}
    for idx, time in enumerate(times):
        winners[idx] = 0
        distancerecord = int(distances[idx])
        for i in range(int(time)):
            distgone = (i * (int(time) - i))
            if distgone > distancerecord:
                winners[idx] += 1
    return math.prod(winners.values())


def part2(times, distances):
    count = 0
    time = int("".join(times))
    distancerecord = int("".join(distances))
    for i in range(time):
        distgone = (i * (time - i))
        if distgone > distancerecord:
            count += 1
    return count


print("Solution for Part 1: " + str(part1(t, d)))
print("Solution for Part 2: " + str(part2(t, d)))
