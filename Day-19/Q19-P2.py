def read_input(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")
    patterns = data[0].split(", ")
    designs = data[2:]
    return patterns, designs

def count_arrangements(design, patterns):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to form an empty string

    for i in range(1, n + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[n]

def main():
    patterns, designs = read_input("desi.txt")
    total_arrangements = 0

    for design in designs:
        total_arrangements += count_arrangements(design, patterns)

    print("Total number of arrangements:", total_arrangements)

if __name__ == "__main__":
    main()