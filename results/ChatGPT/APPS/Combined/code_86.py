def solve_problems(n, k):
    # Calculate the minimum sum of problems needed to satisfy the conditions
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return

    # Initialize the array with the minimum required problems for each day
    a = list(range(1, k + 1))
    current_sum = min_sum

    # Calculate remaining problems to distribute
    remaining = n - current_sum

    # Distribute the remaining problems from the last day to the first
    for i in range(k - 1, -1, -1):
        # Maximum we can add to a[i] while satisfying the conditions
        max_add = a[i]  # We can add at most a[i] to keep the conditions satisfied
        add = min(remaining, max_add)
        a[i] += add
        remaining -= add
        if remaining <= 0:
            break

    if remaining > 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))

# Example usage
n, k = map(int, input().split())
solve_problems(n, k)