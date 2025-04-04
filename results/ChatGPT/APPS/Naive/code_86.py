def solve_problems(n, k):
    # Minimum sum needed if we follow the rules
    min_sum = (k * (k + 1)) // 2
    if n < min_sum:
        print("NO")
        return
    
    # Maximum possible sum following the rules
    # Start with the minimum valid sequence
    a = list(range(1, k + 1))
    current_sum = sum(a)

    # Increment the last element while observing the rules
    for i in range(k - 1, -1, -1):
        # Maximum we can add to a[i] without breaking the rules
        max_increment = min(n - current_sum, 2 * a[i] - a[i - 1] if i > 0 else float('inf'))
        if max_increment > 0:
            a[i] += max_increment
            current_sum += max_increment
        
        if current_sum == n:
            break

    if current_sum == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Input reading
n, k = map(int, input().split())
solve_problems(n, k)