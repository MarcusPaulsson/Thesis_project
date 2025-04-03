def minimize_final_number(t, cases):
    results = []
    for n in cases:
        # The minimum possible number left on the board after n-1 operations is (n + 1) // 2
        min_number = (n + 1) // 2
        results.append(str(min_number))
        
        # We need to perform n - 1 operations
        operations = []
        
        # We will perform the operations in a way that minimizes the result
        for i in range(1, n // 2 + 1):
            if i == n - i:
                operations.append((i, i))
            else:
                operations.append((i, n - i + 1))
        
        # If n is odd, we will have one extra number remaining
        if n % 2 == 1:
            operations.append((n // 2 + 1, n // 2 + 1))
        
        # Add operations to the results
        for a, b in operations:
            results.append(f"{a} {b}")
    
    return "\n".join(results)

# Input reading
t = int(input())
cases = [int(input()) for _ in range(t)]
output = minimize_final_number(t, cases)
print(output)