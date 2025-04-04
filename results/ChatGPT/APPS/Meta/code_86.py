def solve_problems(n, k):
    # The minimum sum to satisfy the conditions
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return
    
    # Start with the minimum required values
    a = list(range(1, k + 1))
    current_sum = sum(a)

    # We need to distribute the remaining problems
    remaining = n - current_sum
    
    # Start from the last element and try to increase it
    for i in range(k - 1, -1, -1):
        # Maximum we can increase a[i] to
        max_increase = 2 * a[i] - a[i]
        # Max we can add without exceeding the next day's limit
        add = min(remaining, max_increase)
        a[i] += add
        remaining -= add
        if remaining <= 0:
            break
    
    if remaining > 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))

# Example usage
n, k = map(int, input().split())
solve_problems(n, k)