def solve_training(n, k):
    # Minimum required problems to satisfy the conditions
    min_problems = (k * (k + 1)) // 2
    max_problems = 0
    a = []

    if n < min_problems:
        print("NO")
        return

    # Start with the minimum possible problems per day
    for i in range(1, k + 1):
        a.append(i)
        max_problems += i

    # Calculate the extra problems we can distribute
    extra_problems = n - max_problems

    # Distribute the extra problems
    for i in range(k - 1, -1, -1):
        if extra_problems <= 0:
            break
        # The maximum we can add to a[i] is capped by the rules
        max_increase = min(extra_problems, (a[i] * 2) - a[i])
        a[i] += max_increase
        extra_problems -= max_increase

    # Check if we have distributed exactly n problems
    if sum(a) == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Read input
n, k = map(int, input().split())
solve_training(n, k)