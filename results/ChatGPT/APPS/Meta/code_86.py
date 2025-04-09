def solve_problems(n, k):
    # Minimum sum calculation
    min_sum = k * (k + 1) // 2  # 1 + 2 + ... + k
    if n < min_sum:
        print("NO")
        return

    # We can start with the minimum valid series
    a = list(range(1, k + 1))
    current_sum = sum(a)

    # Distributing the remaining problems
    remaining = n - current_sum

    for i in range(k - 1, -1, -1):
        # The maximum we can add to a[i] while keeping a[i] < a[i + 1]
        max_addable = 2 * a[i] - a[i + 1] if i < k - 1 else float('inf')
        add = min(max_addable, remaining)

        a[i] += add
        remaining -= add

        if remaining <= 0:
            break

    if remaining > 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))

# Example input
n, k = map(int, input().split())
solve_problems(n, k)