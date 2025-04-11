def solve_problems(n, k):
    # Minimum sum of problems that can be solved in k days
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return
    
    # Maximum sum of problems that can be solved in k days
    max_sum = 0
    a = []
    current = 1
    
    for i in range(k):
        a.append(current)
        max_sum += current
        current = min(2 * current, current + 1 + (k - i - 1))
    
    if n > max_sum:
        print("NO")
        return
    
    # Now we need to adjust the array to sum to n
    for i in range(k - 1, -1, -1):
        while sum(a) < n and a[i] < (2 * a[i]):
            a[i] += 1
            if sum(a) == n:
                break
    
    if sum(a) == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Read input
n, k = map(int, input().split())
solve_problems(n, k)