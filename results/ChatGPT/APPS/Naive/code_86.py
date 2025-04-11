def solve_problems(n, k):
    # Minimum sum of problems needed to satisfy the conditions
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        return "NO"

    # Start with the minimum valid sequence
    a = list(range(1, k + 1))
    current_sum = sum(a)

    # Distribute the remaining problems
    remaining = n - current_sum
    for i in range(k - 1, -1, -1):
        # Maximum we can add to a[i] while satisfying the conditions
        max_add = min(remaining, (2 * a[i]) - a[i])
        a[i] += max_add
        remaining -= max_add
        if remaining <= 0:
            break

    # Check if we have distributed all problems
    if sum(a) == n:
        return "YES\n" + " ".join(map(str, a))
    else:
        return "NO"

# Read input
n, k = map(int, input().split())
result = solve_problems(n, k)
print(result)