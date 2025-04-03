def minimize_number(t, test_cases):
    results = []
    
    for n in test_cases:
        # The minimum possible number left on the board
        min_number = (n + 1) // 2
        results.append(str(min_number))
        
        # We need to perform n-1 operations
        operations = []
        # Prepare a list of numbers
        numbers = list(range(1, n + 1))
        
        while len(numbers) > 1:
            # Always take the largest two numbers to minimize the result
            a = numbers.pop()  # largest
            b = numbers.pop()  # second largest
            new_number = (a + b + 1) // 2  # round up
            operations.append(f"{a} {b}")
            numbers.append(new_number)  # add the new number back to the list
            numbers.sort()  # Keep the list sorted for next operation
            
        results.extend(operations)
        
    return results

# Read input
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Get results
results = minimize_number(t, test_cases)

# Print output
print("\n".join(results))