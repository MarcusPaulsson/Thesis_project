def solve_polycarp(n, k):
    # Minimum problems needed to satisfy the constraints
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return
    
    # Start with the minimum possible values
    a = list(range(1, k + 1))
    
    # Calculate the remaining problems to distribute
    remaining = n - min_sum
    
    # Distribute the remaining problems
    for i in range(k - 1, -1, -1):
        max_add = remaining  # We can add at most the remaining problems
        a[i] += max_add
        remaining -= max_add
        
        if remaining <= 0:
            break
            
    if remaining > 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))

# Read input
try:
    n, k = map(int, input().split())
    solve_polycarp(n, k)
except ValueError:
    print("Invalid input. Please enter two integers.")