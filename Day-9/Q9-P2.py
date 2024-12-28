filename = "input.txt"
data = open(filename).read().strip().split("\n")

sequence = data[0]
file_configurations = []
arrangement = []
current_file = 0
for index, character in enumerate(sequence):
    block_length = int(character)
    if index % 2 == 0:
        arrangement.extend([str(current_file)] * block_length)
        current_file += 1
    else:
        arrangement.extend(["."] * block_length)

file_locations = {}
current_file_id = None
current_count = 0
for index, file_marker in enumerate(arrangement):
    if file_marker != ".":
        file_id = int(file_marker)
        if file_id != current_file_id:
            current_file_id = file_id
            current_count = 1
            file_locations[file_id] = [index, 1]
        else:
            current_count += 1
            file_locations[file_id][1] = current_count

maximum_file_identifier = max(file_locations.keys())


def locate_empty_span(arrangement, file_start, file_length):
    if file_start == 0:
        return None
    best_span_start = None
    current_span_start = None
    current_span_count = 0
    for i in range(file_start):
        if arrangement[i] == ".":
            if current_span_start is None:
                current_span_start = i
                current_span_count = 1
            else:
                current_span_count += 1
        else:
            if current_span_count >= file_length:
                return current_span_start
            current_span_start = None
            current_span_count = 0
    if current_span_start is not None and current_span_count >= file_length:
        return current_span_start
    return None


for file_id in sorted(file_locations.keys(), reverse=True):
    start_position, length = file_locations[file_id]
    empty_span_start = locate_empty_span(arrangement, start_position, length)
    if empty_span_start is not None:
        for i in range(start_position, start_position + length):
            arrangement[i] = "."
        for i in range(empty_span_start, empty_span_start + length):
            arrangement[i] = str(file_id)
        file_locations[file_id][0] = empty_span_start

total_score = 0
for index, file_marker in enumerate(arrangement):
    if file_marker != ".":
        total_score += index * int(file_marker)

print(total_score)