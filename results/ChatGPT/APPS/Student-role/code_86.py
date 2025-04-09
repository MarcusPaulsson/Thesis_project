def solve_problems(n, k):
    # Minimum problems needed to satisfy the conditions
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return

    # Maximum problems we can solve on the first day with increasing conditions
    max_first_day = n // k + (1 if n % k != 0 else 0)

    a = [0] * k
    for i in range(k):
        # We start with the minimum required problems for each day
        a[i] = i + 1

    # Calculate the current sum of problems solved
    current_sum = sum(a)

    # We need to distribute the remaining problems
    remaining = n - current_sum

    # Start distributing from the last day backwards
    for i in range(k - 1, -1, -1):
        # The maximum we can add to a[i] while respecting the conditions
        max_add = min(remaining, 2 * a[i] - a[i])
        if max_add > 0:
            a[i] += max_add
            remaining -= max_add

        if remaining <= 0:
            break

    # Final check if we managed to distribute all problems
    if sum(a) == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Read input
n, k = map(int, input().split())
solve_problems(n, k)