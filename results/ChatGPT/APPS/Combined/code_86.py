def can_solve_problems(n, k):
    # Calculate the minimum and maximum sums based on the conditions
    min_required = k * (k + 1) // 2
    max_possible = sum(2 ** i for i in range(k))

    # Check if it's possible to distribute problems
    if n < min_required or n > max_possible:
        print("NO")
        return

    # Start with the minimum configuration
    a = list(range(1, k + 1))
    remaining_problems = n - min_required

    # Distribute the remaining problems from the end of the list
    for i in range(k - 1, -1, -1):
        # Calculate the maximum increase for a[i]
        max_increase = (1 << (k - 1 - i)) - 1
        increase = min(remaining_problems, max_increase)
        a[i] += increase
        remaining_problems -= increase

        if remaining_problems <= 0:
            break

    print("YES")
    print(' '.join(map(str, a)))

# Input reading
n, k = map(int, input().split())
can_solve_problems(n, k)