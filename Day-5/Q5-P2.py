from collections import defaultdict, deque

def get_middle_index(length):
    """Returns the middle index for a list of given length."""
    return length // 2

def is_update_correct(rules, update):
    """Check if the update follows all the rules."""
    for rule in rules:
        x, y = rule
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def correct_update_order(rules, update):
    """Correct the order of an update based on the rules."""
    # Build a graph based on the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    pages_in_update = set(update)
    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Perform topological sort
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []
    
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def process_incorrect_updates(file_path):
    """Process and correct the incorrectly-ordered updates, then calculate the sum of their middle page numbers."""
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    # Separate rules and updates
    rules = []
    updates = []
    is_rules_section = True

    for line in lines:
        if "|" in line and is_rules_section:
            x, y = map(int, line.split("|"))
            rules.append((x, y))
        else:
            is_rules_section = False
            updates.append(list(map(int, line.split(","))))

    # Identify and correct incorrect updates
    middle_page_sum = 0
    for update in updates:
        if not is_update_correct(rules, update):
            corrected_update = correct_update_order(rules, update)
            middle_index = get_middle_index(len(corrected_update))
            middle_page_sum += corrected_update[middle_index]
    
    return middle_page_sum

# Example usage
file_path = "ordering_rules.txt"  # Replace with the actual path to your input file
result = process_incorrect_updates(file_path)
print("Sum of middle page numbers for corrected updates:", result)
