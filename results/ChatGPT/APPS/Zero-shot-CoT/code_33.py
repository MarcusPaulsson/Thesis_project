def minimize_final_number(t, test_cases):
    results = []
    
    for n in test_cases:
        results.append(str((n + 1) // 2))  # Minimum final number is (n + 1) // 2
        
        # Create the operations
        current_numbers = list(range(1, n + 1))
        
        while len(current_numbers) > 1:
            # Always pair the largest with the smallest
            a = current_numbers.pop()   # Largest
            b = current_numbers.pop(0)  # Smallest
            new_number = (a + b + 1) // 2  # Rounded up
            results.append(f"{b} {a}")  # Store the operation
            current_numbers.append(new_number)  # Add new number back to list
            current_numbers.sort()  # Maintain order for the next operation
    
    return "\n".join(results)

# Input processing
t = int(input())
test_cases = [int(input().strip()) for _ in range(t)]
result = minimize_final_number(t, test_cases)
print(result)