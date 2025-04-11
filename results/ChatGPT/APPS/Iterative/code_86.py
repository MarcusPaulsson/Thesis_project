def solve_problems(n, k):
    # Minimum sum of the first k natural numbers
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return
    
    # Start with the minimum valid sequence
    a = list(range(1, k + 1))
    current_sum = min_sum
    
    # Distribute the remaining problems
    remaining = n - current_sum
    for i in range(k - 1, -1, -1):
        # Maximum we can add to a[i] while satisfying the conditions
        max_add = (2 * a[i]) - a[i] - 1  # a[i] < a[i+1] <= 2 * a[i]
        add = min(remaining, max_add)
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