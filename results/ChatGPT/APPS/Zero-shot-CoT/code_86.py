def solve_training(n, k):
    # Minimum sum required to satisfy the condition: 1 + 2 + 3 + ... + k = k * (k + 1) // 2
    min_required_sum = k * (k + 1) // 2
    
    # If n is less than the minimum required sum, it's impossible
    if n < min_required_sum:
        print("NO")
        return
    
    # Start with the minimum required problems for each day
    a = list(range(1, k + 1))
    current_sum = min_required_sum
    
    # We can increase the last element of the array while maintaining the conditions
    for i in range(k - 1, -1, -1):
        while current_sum < n:
            # Maximum allowed for a[i] is 2 * a[i] (but also should not exceed the next day)
            if i < k - 1 and a[i] >= a[i + 1]:
                break
            
            # Increase a[i] while it's valid
            a[i] += 1
            current_sum += 1
            
            if a[i] > 2 * (a[i - 1] if i > 0 else 0):
                break
            
    # Check if we reached the required sum
    if current_sum == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Example usage:
solve_training(26, 6)
solve_training(8, 3)
solve_training(1, 1)
solve_training(9, 4)
solve_training(7, 2)