# Read ranges from input file
ranges = []
with open("inputs/2.txt", "r") as f:
    for line in f:
        for element in line.strip().split(","):
            start, end = element.split("-")
            ranges.append((int(start), int(end)))


# Count repeated blocks in a number
def repeated_block_count(n):
    """
    Returns the number of times a repeated block occurs in n.
    Leading zeros are ignored.
    """
    s = str(n)
    L = len(s)

    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue
        block = s[:k]
        if block[0] == "0":
            continue
        repetitions = L // k
        if block * repetitions == s:
            return repetitions
    return 0


# List invalid IDs in a range
def list_invalid_ids(start, end):
    """
    Returns a list of tuples (n, repetitions) for numbers with repeated blocks.
    """
    result = []
    for n in range(start, end + 1):
        reps = repeated_block_count(n)
        if reps >= 2:
            result.append((n, reps))
    return result


# Sum invalid IDs for exactly 2 repeats and for ≥2 repeats
sum_exactly_2 = 0
sum_2_or_more = 0

for start, end in ranges:
    for n, reps in list_invalid_ids(start, end):
        if reps == 2:
            sum_exactly_2 += n
        if reps >= 2:
            sum_2_or_more += n

print("Part 1 - sum of invalid IDs (exactly 2 repeats):", sum_exactly_2)
print("Part 2 - sum of invalid IDs (≥2 repeats):", sum_2_or_more)
