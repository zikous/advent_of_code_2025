# Read ranges from input file
ranges = []
with open("inputs/2.txt", "r") as f:
    for line in f:
        for element in line.strip().split(","):
            start, end = element.split("-")
            ranges.append((int(start), int(end)))

sum_part1 = 0  # sum of numbers with exactly 2 repeated blocks
sum_part2 = 0  # sum of numbers with 2 or more repeated blocks

# Go through each range of numbers
for start, end in ranges:
    for n in range(start, end + 1):
        s = str(n)
        L = len(s)

        repeated_exactly_2 = False  # flag for part 1
        repeated_2_or_more = False  # flag for part 2

        # Try all possible block sizes
        for k in range(1, L // 2 + 1):
            if L % k != 0:
                continue  # block size must divide number evenly

            block = s[:k]
            r = L // k  # number of repetitions

            if block[0] == "0":
                continue  # skip blocks starting with zero

            if block * r == s:
                if r == 2:
                    repeated_exactly_2 = True  # part 1 condition
                if r >= 2:
                    repeated_2_or_more = True  # part 2 condition

        # Add to totals if conditions are met
        if repeated_exactly_2:
            sum_part1 += n
        if repeated_2_or_more:
            sum_part2 += n

print("Part 1 - sum of invalid IDs (exactly 2 repeats):", sum_part1)
print("Part 2 - sum of invalid IDs (2 or more repeats):", sum_part2)
