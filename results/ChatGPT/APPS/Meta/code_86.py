def solve_problems(n, k):
    # Minimum sum of problems needed to satisfy the conditions
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return
    
    # Start with the minimum valid array
    a = list(range(1, k + 1))
    current_sum = sum(a)
    
    # Distribute the remaining problems
    remaining = n - current_sum
    
    for i in range(k - 1, -1, -1):
        # Maximum we can add to a[i] while maintaining the conditions
        max_add = min(remaining, 2 * a[i] - a[i - 1] if i > 0 else remaining)
        a[i] += max_add
        remaining -= max_add
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