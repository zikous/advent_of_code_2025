# Read grid of characters from input
grid = []
with open("inputs/4.txt", "r") as f:
    for line in f:
        grid.append([x for x in line.strip()])

# All 8 directions around a cell
directions = [
    (0, 1),  # right
    (1, 0),  # down
    (1, 1),  # down-right
    (-1, -1),  # up-left
    (-1, 0),  # up
    (0, -1),  # left
    (1, -1),  # down-left
    (-1, 1),  # up-right
]

n = len(grid)
m = len(grid[0])

res = []  # stores number of removed cells in each iteration

# Repeatedly prune the grid until stable
while True:
    to_remove = []  # list of coordinates to delete in this round

    # Scan every cell
    for i in range(n):
        for j in range(m):
            # We only care about '@' cells
            if grid[i][j] == "@":
                neighbours = 0

                # Count adjacent '@'s (8-neighbourhood)
                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    # Check bounds and content
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == "@":
                        neighbours += 1

                # If a cell has fewer than 4 '@' neighbours, it gets removed
                if neighbours < 4:
                    to_remove.append((i, j))

    # Apply removals
    for i, j in to_remove:
        grid[i][j] = "."

    # If something was removed, record the count
    if to_remove:
        res.append(len(to_remove))
    else:
        # No removals → process is stable → stop
        break

# Output the required results:
print("Part 1 - removed in the first wave:", res[0])
print("Part 2 - total removed over all waves:", sum(res))
