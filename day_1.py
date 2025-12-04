# Read rotations from input file
rotations = []
with open("inputs/1.txt", "r") as f:
    for line in f:
        rotations.append(line.strip())

position = 50  # starting position

zero_count_part1 = 0  # count of rotations ending on zero
zero_count_part2 = 0  # count of zeros passed during rotations

for rotation in rotations:
    direction = rotation[0]
    steps = -int(rotation[1:]) if direction == "L" else int(rotation[1:])

    old_circle = position // 100
    new_circle = (position + steps) // 100

    old_position = position
    new_position = (position + steps) % 100

    # Part 1: check if we end on zero
    if new_position == 0:
        zero_count_part1 += 1

    # Part 2: count zeros passed during rotation
    is_old_zero = old_position == 0
    is_new_zero = new_position == 0

    if new_circle == old_circle:
        seen_zeros = 1 if is_new_zero else 0
    elif new_circle > old_circle:
        seen_zeros = new_circle - old_circle
    else:
        if is_old_zero:
            seen_zeros = old_circle - new_circle - 1
        else:
            seen_zeros = old_circle - new_circle + (1 if is_new_zero else 0)

    zero_count_part2 += seen_zeros

    # Debug info
    print(
        f"Moved from {old_position} to {new_position} with {rotation} "
        f"(circle {old_circle} -> {new_circle}), seen zeros: {seen_zeros}"
    )

    position = new_position  # update position

print("\nPart 1 - zeros at end of rotations:", zero_count_part1)
print("Part 2 - zeros passed during rotations:", zero_count_part2)
