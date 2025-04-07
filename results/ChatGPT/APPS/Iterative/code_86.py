def solve_problems(n, k):
    # Minimum sum of problems needed is the sum of first k natural numbers
    min_sum = k * (k + 1) // 2
    # Maximum sum possible with the constraints
    max_sum = sum(2 ** i for i in range(k))  # 1, 2, 4, ..., 2^(k-1)

    if n < min_sum or n > max_sum:
        print("NO")
        return
    
    # Now we need to construct a valid solution
    a = []
    current = 1
    remaining = n - min_sum  # how much we can distribute to meet n
    
    for i in range(k):
        a.append(current)
        if remaining > 0:
            # Max we can add to current while keeping the rules
            max_add = min(remaining, (2 * current) - current)  # must remain positive and <= 2 * current
            current += max_add
            remaining -= max_add
        current += 1  # increment for next day need

    print("YES")
    print(" ".join(map(str, a)))

# Read input
n, k = map(int, input().split())
solve_problems(n, k)