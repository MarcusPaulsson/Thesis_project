def solve_problems(n, k):
    # Minimum sum of problems that can be solved in k days
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return
    
    # Maximum sum of problems that can be solved in k days
    max_sum = 0
    a = []
    for i in range(1, k + 1):
        a.append(i)
        max_sum += i
    
    if n > max_sum * 2:
        print("NO")
        return
    
    # Start with the minimum valid sequence
    a = list(range(1, k + 1))
    current_sum = sum(a)
    
    # Distribute the remaining problems
    remaining = n - current_sum
    
    for i in range(k - 1, -1, -1):
        # Maximum we can add to a[i]
        max_add = min(remaining, a[i] * 2 - a[i])
        remaining -= max_add
        a[i] += max_add
        
        if remaining <= 0:
            break
    
    if remaining > 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))

# Example usage:
n, k = map(int, input().split())
solve_problems(n, k)