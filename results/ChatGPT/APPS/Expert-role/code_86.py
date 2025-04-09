def solve_problems(n, k):
    # Minimum sum of problems solved with constraints
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return

    # Start with the minimum required problems solved each day
    a = list(range(1, k + 1))
    current_sum = min_sum

    # Distribute the remaining problems
    remaining = n - current_sum
    for i in range(k - 1, -1, -1):
        # The maximum number of problems we can add to a[i]
        # We can add at most (2 * a[i]) - a[i] = a[i] to keep the next day's constraints
        max_increase = a[i]  # We can increase a[i] by at most a[i]
        increase = min(remaining, max_increase)
        a[i] += increase
        remaining -= increase
        if remaining == 0:
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