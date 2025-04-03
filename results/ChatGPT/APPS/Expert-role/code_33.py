def minimize_final_number(t, test_cases):
    results = []
    
    for n in test_cases:
        final_number = (n + 1) // 2  # The minimum possible number left on the board
        results.append(str(final_number))
        
        # Generate operations
        operations = []
        # We can simulate the process of combining the numbers
        # We will keep combining the largest number with the smallest until we reach the final number
        numbers = list(range(1, n + 1))
        
        while len(numbers) > 1:
            a = numbers.pop()
            b = numbers.pop(0)
            new_number = (a + b + 1) // 2  # Round up
            operations.append(f"{a} {b}")
            numbers.insert(0, new_number)  # Insert the new number back
        
        results.extend(operations)

    return '\n'.join(results)

# Read input
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Print output
print(minimize_final_number(t, test_cases))