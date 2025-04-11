def solve_polycarp(n, k):
    # Minimum sum of problems that can be solved in k days
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return

    # Start with the minimum valid sequence
    a = list(range(1, k + 1))
    current_sum = sum(a)

    # We need to distribute the remaining problems
    remaining = n - current_sum

    for i in range(k - 1, -1, -1):
        # Maximum we can add to a[i] while respecting the constraints
        max_add = min(remaining, (2 * a[i]) - a[i])
        if i < k - 1:
            max_add = min(max_add, (2 * a[i] - a[i + 1]) - 1)

        a[i] += max_add
        remaining -= max_add

        if remaining <= 0:
            break

    if sum(a) == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Example usage:
n, k = map(int, input().split())
solve_polycarp(n, k)