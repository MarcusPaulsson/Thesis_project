def solve_problems(n, k):
    # Minimum problems needed with strictly increasing sequence
    min_needed = k * (k + 1) // 2
    
    if n < min_needed:
        print("NO")
        return
    
    # Start with the minimum valid sequence
    a = list(range(1, k + 1))
    remaining = n - min_needed
    
    # Distribute the remaining problems as optimally as possible
    for i in range(k - 1, -1, -1):
        if remaining == 0:
            break
        
        # Maximum we can add to a[i] while respecting the constraints
        max_possible_increase = min(remaining, 2 * a[i] - a[i + 1] if i < k - 1 else float('inf'))
        
        a[i] += max_possible_increase
        remaining -= max_possible_increase
    
    # Check if we have exactly n problems solved
    if sum(a) == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Read input
n, k = map(int, input().split())
solve_problems(n, k)