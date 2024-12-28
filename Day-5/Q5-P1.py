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

def process_updates(file_path):
    """Process the updates and calculate the sum of middle page numbers for correctly-ordered updates."""
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

    # Process each update
    middle_page_sum = 0
    for update in updates:
        if is_update_correct(rules, update):
            middle_index = get_middle_index(len(update))
            middle_page_sum += update[middle_index]
    
    return middle_page_sum

# Example usage
file_path = "ordering_rules.txt"  # Replace with the actual path to your input file
result = process_updates(file_path)
print("Sum of middle page numbers for correctly-ordered updates:", result)
