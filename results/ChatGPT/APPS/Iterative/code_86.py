def solve_problems(n, k):
    # Minimum sum of first k increasing numbers: 1 + 2 + ... + k
    min_sum = k * (k + 1) // 2
    # Maximum sum if we double each day: 1 + 2 + ... + k
    # The maximum achievable sum is when we double each previous day's problems
    max_sum = sum(2**i for i in range(k))

    if n < min_sum or n > max_sum:
        print("NO")
        return
    
    # Start with the minimum array
    a = list(range(1, k + 1))
    current_sum = min_sum
    
    # Adjust the last day to fit the requirements
    for i in range(k - 1, -1, -1):
        while current_sum < n and a[i] < 2 * (a[i - 1] if i > 0 else 0) and current_sum + 1 <= n:
            current_sum += 1
            a[i] += 1
        
    print("YES")
    print(" ".join(map(str, a)))

# Example usage:
n, k = map(int, input().split())
solve_problems(n, k)