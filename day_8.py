# Read box coordinates from input file
with open("inputs/8.txt") as f:
    boxes = [list(map(int, line.strip().split(","))) for line in f]

n = len(boxes)

# Build all edges with squared distances
edges = []
for i in range(n):
    x1, y1, z1 = boxes[i]
    for j in range(i + 1, n):
        x2, y2, z2 = boxes[j]
        dist2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        edges.append((dist2, i, j))
edges.sort()

# Union-Find setup
parent = list(range(n))
size = [1] * n


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    parent[rb] = ra
    size[ra] += size[rb]
    return True


# Solution
CONNECTIONS = 1000
part1_answer = None
last_pair = None

for idx, (_, i, j) in enumerate(edges):
    merged = union(i, j)

    # Track Part One answer after 1000 edges
    if part1_answer is None and idx + 1 == CONNECTIONS:
        comps = [0] * n
        for k in range(n):
            comps[find(k)] += 1
        sizes = sorted([c for c in comps if c], reverse=True)
        part1_answer = sizes[0] * sizes[1] * sizes[2]

    # Track Part Two last merged pair
    if merged:
        last_pair = (i, j)
        if size[find(i)] == n:  # all connected
            break

# Part Two answer: multiply X coordinates of last merged pair
x1, x2 = boxes[last_pair[0]][0], boxes[last_pair[1]][0]
part2_answer = x1 * x2

print("Part One:", part1_answer)
print("Part Two:", part2_answer)

print("Part One:", part1_answer)
print("Part Two:", part2_answer)
