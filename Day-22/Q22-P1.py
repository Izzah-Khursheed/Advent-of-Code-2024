# Function to calculate the next secret number in the sequence
def generate_next_secret(secret_number):
    # Step 1: Multiply by 64, mix, prune
    secret_number ^= (secret_number * 64) % 16777216
    secret_number %= 16777216

    # Step 2: Divide by 32 (integer division), mix, prune
    secret_number ^= (secret_number // 32) % 16777216
    secret_number %= 16777216

    # Step 3: Multiply by 2048, mix, prune
    secret_number ^= (secret_number * 2048) % 16777216
    secret_number %= 16777216

    return secret_number

# Function to simulate the sequence and get the 2000th secret number
def simulate_buyer(initial_secret):
    secret = initial_secret
    for _ in range(2000):
        secret = generate_next_secret(secret)
    return secret

# Main function to read input and calculate the result
def main():
    # Read input from file
    with open("secret.txt", "r") as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]

    # Calculate the 2000th secret number for each buyer
    results = [simulate_buyer(secret) for secret in initial_secrets]

    # Calculate the total sum of the 2000th secret numbers
    total_sum = sum(results)

    # Print the result
    print("Sum of the 2000th secret numbers:", total_sum)

# Run the main function
if __name__ == "__main__":
    main()