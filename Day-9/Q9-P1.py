filename = "input.txt"

data = open(filename).read().strip().split("\n")

sequence = data[0]
configurations = []
arrangement = []
current_file = 0
for index, character in enumerate(sequence):
    block_length = int(character)
    if index % 2 == 0:
        arrangement.extend([str(current_file)] * block_length)
        current_file += 1
    else:
        arrangement.extend(["."] * block_length)

while True:
    try:
        empty_position = arrangement.index(".")
    except ValueError:
        break

    right_side_empty = any(ch != "." for ch in arrangement[empty_position + 1 :])
    if not right_side_empty:
        break

    for reverse_index in range(len(arrangement) - 1, -1, -1):
        if arrangement[reverse_index] != ".":
            arrangement[empty_position], arrangement[reverse_index] = arrangement[reverse_index], "."
            break

total_score = 0
for index, file_marker in enumerate(arrangement):
    if file_marker != ".":
        total_score += index * int(file_marker)

print(total_score)