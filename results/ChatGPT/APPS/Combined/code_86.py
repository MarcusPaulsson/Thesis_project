def solve_polycarp(n, k):
    # Calculate the minimum sum required to satisfy the conditions
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return
    
    # Initialize the array with the minimum required problems
    a = list(range(1, k + 1))
    current_sum = min_sum
    
    # Calculate the remaining problems to distribute
    remaining = n - current_sum
    
    # Distribute the remaining problems from the last day to the first
    for i in range(k - 1, -1, -1):
        # Calculate the maximum we can add to a[i] while respecting the conditions
        max_add = min(remaining, (2 * a[i]) - a[i] - 1)  # Ensure a[i] < a[i+1]
        a[i] += max_add
        remaining -= max_add
        
        if remaining <= 0:
            break
    
    if remaining > 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))

# Example usage:
# n, k = map(int, input().split())
# solve_polycarp(n, k)