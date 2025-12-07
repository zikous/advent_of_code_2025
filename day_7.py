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

# Part 1: count how many times a beam hits a splitter (^)
active1 = {s_j}  # set of columns where the beam is active in the current row
res1 = 0  # total number of splitter hits

# Part 2: count total quantum timelines
active2 = {s_j: 1}  # dict mapping column -> number of timelines reaching this column

# Process the grid row by row, starting just below 'S'
for r in range(s_i + 1, n):

    # --- Part 1 logic ---
    new_active1 = set()
    for c in active1:
        if grid[r][c] == "^":  # beam hits a splitter
            res1 += 1
            # beam splits left and right
            if c - 1 >= 0:
                new_active1.add(c - 1)
            if c + 1 < m:
                new_active1.add(c + 1)
        else:  # beam continues straight down
            new_active1.add(c)
    active1 = new_active1  # update active columns for next row

    # --- Part 2 logic ---
    new_active2 = {}
    for c, count in active2.items():
        if grid[r][c] == "^":  # quantum particle hits a splitter
            # split into two timelines: left and right
            if c - 1 >= 0:
                new_active2[c - 1] = new_active2.get(c - 1, 0) + count
            if c + 1 < m:
                new_active2[c + 1] = new_active2.get(c + 1, 0) + count
        else:  # timeline continues straight down
            new_active2[c] = new_active2.get(c, 0) + count
    active2 = new_active2  # update timelines for next row

# Sum all remaining timelines at the bottom for Part 2
res2 = sum(active2.values())

print("Part 1:", res1)  # total number of splitter hits
print("Part 2:", res2)  # total number of quantum timelines
