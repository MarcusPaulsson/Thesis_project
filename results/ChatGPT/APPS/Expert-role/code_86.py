def solve_polycarp(n, k):
    # Minimum sum of problems that can be solved in k days
    min_sum = k * (k + 1) // 2
    # Maximum sum of problems that can be solved in k days
    max_sum = k * (2 * k + 1) // 2

    if n < min_sum or n > max_sum:
        print("NO")
        return

    # Start with the minimum required problems for each day
    a = list(range(1, k + 1))
    current_sum = sum(a)

    # Distribute the remaining problems
    remaining = n - current_sum

    for i in range(k - 1, -1, -1):
        # Maximum we can add to a[i] while respecting the constraints
        max_add = min(remaining, (2 * a[i]) - a[i])
        remaining -= max_add
        a[i] += max_add

        if remaining <= 0:
            break

    print("YES")
    print(" ".join(map(str, a)))

# Example inputs
inputs = [
    (26, 6),
    (8, 3),
    (1, 1),
    (9, 4),
    (7, 2)
]

for n, k in inputs:
    solve_polycarp(n, k)