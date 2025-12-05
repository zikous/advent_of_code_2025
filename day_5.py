# Read intervals and available IDs
intervals = []
ids = []

with open("inputs/5.txt", "r") as f:
    for line in f:
        stripped = line.strip()
        if not stripped:
            continue
        if "-" in stripped:
            a, b = map(int, stripped.split("-"))
            intervals.append([a, b])
        else:
            ids.append(int(stripped))

# Merge intervals
intervals.sort()
merged = []

for start, end in intervals:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

# Part 1 — Count fresh available IDs
import bisect

starts = [a for a, _ in merged]
fresh_count = 0

for x in ids:
    idx = bisect.bisect_right(starts, x) - 1
    if idx >= 0:
        a, b = merged[idx]
        if a <= x <= b:
            fresh_count += 1

print("Part 1 - fresh available ingredients:", fresh_count)

# Part 2 — Count total fresh IDs in merged ranges
total_fresh = sum(b - a + 1 for a, b in merged)
print("Part 2 - total fresh IDs:", total_fresh)
