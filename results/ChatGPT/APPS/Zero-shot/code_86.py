def solve(n, k):
    # Minimum sum of the first k natural numbers
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return
    
    # Maximum sum if we double the previous day's problems
    max_sum = 0
    a = []
    current = 1
    
    for i in range(k):
        a.append(current)
        max_sum += current
        current = min(2 * current, current + 1 + (k - i - 1))  # Ensure we can still fill the rest
    
    # If the maximum sum we can achieve is less than n, it's impossible
    if max_sum > n:
        print("NO")
        return
    
    # Distribute the remaining problems
    remaining = n - sum(a)
    
    for i in range(k - 1, -1, -1):
        if remaining <= 0:
            break
        # The maximum we can add to a[i] without violating the rules
        max_add = min(remaining, (2 * a[i]) - a[i])
        a[i] += max_add
        remaining -= max_add
    
    if sum(a) == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Read input
n, k = map(int, input().split())
solve(n, k)