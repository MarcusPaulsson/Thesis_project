def solve_problems(n, k):
    # Minimum sum of problems needed to satisfy the conditions
    min_sum = k * (k + 1) // 2  # 1 + 2 + ... + k
    if n < min_sum:
        print("NO")
        return

    # Start with the minimum valid sequence
    a = list(range(1, k + 1))
    current_sum = min_sum

    # Distribute the remaining problems
    remaining = n - current_sum
    for i in range(k - 1, -1, -1):
        # Maximum we can add to a[i] while respecting the constraints
        max_add = min(remaining, a[i] - 1 + a[i] // 2)
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
solve_problems(26, 6)
solve_problems(8, 3)
solve_problems(1, 1)
solve_problems(9, 4)
solve_problems(7, 2)