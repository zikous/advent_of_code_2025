# read battery banks
batteries = []
with open("inputs/3.txt", "r") as f:
    for line in f:
        batteries.append([int(x) for x in line.strip() if x.isdigit()])


# function to get largest number from digits in order
def max_number(bank, k):
    stack = []
    n = len(bank)
    for i, d in enumerate(bank):
        remaining = n - i
        while stack and stack[-1] < d and len(stack) + remaining > k:
            stack.pop()
        if len(stack) < k:
            stack.append(d)
    return int("".join(map(str, stack)))


# Part 1: pick 2 digits
total_1 = sum(max_number(bank, 2) for bank in batteries)
print("Part 1 total:", total_1)

# Part 2: pick 12 digits
total_2 = sum(max_number(bank, 12) for bank in batteries)
print("Part 2 total:", total_2)
