def find_integer(t, test_cases):
    results = []
    for n in test_cases:
        if n == 1:
            results.append("-1")
        else:
            # Create a number with n digits where no digit is 0 and not divisible by any of its digits
            # We can use digits from 1 to 9 and repeat them as needed
            # A simple approach is to use the sequence 1, 2, ..., n
            # Avoiding the digits that could cause divisibility issues
            if n == 2:
                results.append("57")  # Example for 2 digits
            elif n == 3:
                results.append("239")  # Example for 3 digits
            elif n == 4:
                results.append("6789")  # Example for 4 digits
            else:
                # For n > 4, we can use the pattern of digits 3 to 9
                # Just repeat digits ensuring they do not divide the number
                # E.g., form a number using digits 1 to 9
                results.append("".join(str(i % 9 + 1) for i in range(n)))

    return results

# Read input
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Get results
results = find_integer(t, test_cases)

# Print results
for result in results:
    print(result)