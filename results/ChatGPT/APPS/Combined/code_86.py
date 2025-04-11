def solve_polycarp(n, k):
    # Calculate the minimum and maximum sums of problems that can be solved in k days
    min_sum = k * (k + 1) // 2
    max_sum = k * (2 * k + 1) // 2

    # Check if n is within the possible range
    if n < min_sum or n > max_sum:
        print("NO")
        return

    # Initialize the array with the minimum required problems for each day
    a = list(range(1, k + 1))
    current_sum = sum(a)

    # Calculate the remaining problems to distribute
    remaining = n - current_sum

    # Distribute the remaining problems while respecting the constraints
    for i in range(k - 1, -1, -1):
        # Calculate the maximum increase possible for a[i]
        max_increase = min(remaining, a[i] - 1 + a[i] // 2)
        a[i] += max_increase
        remaining -= max_increase

        if remaining <= 0:
            break

    print("YES")
    print(" ".join(map(str, a)))

# Read input
n, k = map(int, input().split())
solve_polycarp(n, k)