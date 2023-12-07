day3 = open("input/day3input.txt", "r").read().splitlines()


def getcoords(grid):  # Gets and returns a set of coordinates to the first value in every valid number
    coords = set()
    for row, rows in enumerate(grid):
        for column, char in enumerate(rows):  # creates a grid
            if not char.isnumeric() and char != '.':  # Searching for characters
                for currow in [row - 1, row, row + 1]:  # Gets rows surrounding character
                    for currcol in [column - 1, column, column + 1]:
                        if currow < 0 or currow >= len(grid):  # Check for out of bounds row
                            continue
                        elif currcol < 0 or currcol >= len(grid[currow]):  # Check for out of bounds column
                            continue
                        elif not grid[currow][currcol].isnumeric():  # Looking for the number
                            continue
                        while currcol > 0 and grid[currow][currcol - 1].isnumeric():  # Find first coordinate of number
                            currcol -= 1
                        coords.add((currow, currcol))  # Add the coordinates for the first char of a number
    return coords


def part1(grid):
    coords = getcoords(grid)
    nums = []
    for row, col in coords:
        num = ""
        while col < len(grid[row]) and grid[row][col].isnumeric():  # Parse entire number
            num += grid[row][col]
            col += 1
        nums.append(int(num))
    return sum(nums)


def part2(grid):
    ans = 0
    for row, rows in enumerate(grid):
        for column, char in enumerate(rows):  # creates a grid
            if char == '*':  # Now only looking for stars
                coords = set()
                for currow in [row - 1, row, row + 1]:
                    for currcol in [column - 1, column, column + 1]:
                        if currow < 0 or currow >= len(grid):
                            continue
                        elif currcol < 0 or currcol >= len(grid[currow]):
                            continue
                        elif not grid[currow][currcol].isnumeric():
                            continue
                        while currcol > 0 and grid[currow][
                            currcol - 1].isnumeric():
                            currcol -= 1
                        coords.add((currow, currcol))
                if len(coords) == 2:  # Ensures that there are exactly 2 values surrounding the *
                    nums = []
                    for r, c in coords:
                        num = ""
                        while c < len(grid[r]) and grid[r][c].isnumeric():  # Parse entire number
                            num += grid[r][c]
                            c += 1
                        nums.append(int(num))
                    ans += nums[0] * nums[1]
    return ans


print("Solution for Part 1: " + str(part1(day3)))
print("Solution for Part 2: " + str(part2(day3)))
