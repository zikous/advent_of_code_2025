import math

# Read input lines
with open("inputs/6.txt", "r") as f:
    lines = [line.replace("\n", " ") for line in f]

# The last line contains the operators (+, *)
ops_line = lines[-1]
ops_indexes = [i for i, c in enumerate(ops_line) if c in ("+", "*")]

# Create ranges between operators
ranges = list(zip(ops_indexes, ops_indexes[1:] + [len(lines[0])]))

# Build a grid of numbers and operators
grid = [[line[a : b - 1] for a, b in ranges] for line in lines]

n = len(grid)
m = len(grid[0])

part1_sum = 0
part2_sum = 0

# Process each column
for col in range(m):
    operator = grid[-1][col].strip()  # operator from last row
    raw_data = [grid[row][col] for row in range(n - 1)]  # numbers above

    # Part 1: sum/prod of numbers as integers
    part1_nums = [int(s) for s in raw_data]

    # Part 2: form numbers by column digits
    part2_nums = [
        int("".join(s[idx] for s in raw_data)) for idx in range(len(raw_data[0]))
    ]

    if operator == "+":
        part1_sum += sum(part1_nums)
        part2_sum += sum(part2_nums)
    elif operator == "*":
        part1_sum += math.prod(part1_nums)
        part2_sum += math.prod(part2_nums)

# Nicely formatted output
print(f"Part 1 - total sum using operators: {part1_sum}")
print(f"Part 2 - total sum with column-wise numbers: {part2_sum}")
