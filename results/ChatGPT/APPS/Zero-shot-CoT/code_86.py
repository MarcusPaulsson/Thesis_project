def solve_problems(n, k):
    # Minimum problems that need to be solved in k days
    min_problems = k * (k + 1) // 2
    if n < min_problems:
        print("NO")
        return
    
    # Starting array where we will store the problems solved each day
    a = list(range(1, k + 1))
    total = sum(a)
    
    # Distributing the remaining problems
    remaining = n - total
    
    # We can increment the last day until we fulfill the constraints
    for i in range(k - 1, -1, -1):
        # The maximum we can add to a[i] while respecting the constraints
        max_add = 2 * a[i] - a[i] - 1  # a[i] < a[i+1] <= 2 * a[i]
        if i < k - 1:
            max_add = min(max_add, 2 * a[i] - a[i + 1] - 1)
        
        add = min(remaining, max_add)
        a[i] += add
        remaining -= add
        
        if remaining <= 0:
            break

    if remaining > 0:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, a)))

# Example usage
n, k = map(int, input().split())
solve_problems(n, k)