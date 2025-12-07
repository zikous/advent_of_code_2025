from collections import defaultdict

with open("inputs/7.txt") as f:
    grid = [list(line.strip()) for line in f]

n = len(grid)
m = len(grid[0])

# Find the start position 'S'
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            s_i, s_j = i, j
            break

active = defaultdict(int)
active[s_j] = 1  # dict mapping column -> number of timelines reaching this column
res1 = 0  # total splitter hits

# Process the grid row by row
for r in range(s_i + 1, n):
    new_active = defaultdict(int)
    for c, count in active.items():
        if grid[r][c] == "^":
            res1 += 1  # splitter hit

            # split into two timelines: left and right
            if c - 1 >= 0:
                new_active[c - 1] += count
            if c + 1 < m:
                new_active[c + 1] += count
        else:
            # timeline continues straight down
            new_active[c] += count
    active = new_active

res2 = sum(active.values())

print("Part 1:", res1)
print("Part 2:", res2)
