def solve_polycarps_problem(n, k):
    # Calculate the minimum and maximum number of problems that can be solved
    min_sum = k * (k + 1) // 2  # Minimum problems: 1 + 2 + ... + k
    max_sum = 0
    current_day_problems = 1

    # Calculate the maximum sum using the doubling strategy
    for _ in range(k):
        max_sum += current_day_problems
        current_day_problems = min(current_day_problems * 2, current_day_problems + 1)

    # Check if the number of problems can be satisfied
    if n < min_sum or n > max_sum:
        print("NO")
        return

    result = [0] * k
    current_day_problems = 1
    remaining_problems = n

    # Assign the minimum required problems for each day
    for i in range(k):
        result[i] = current_day_problems
        remaining_problems -= current_day_problems
        current_day_problems += 1

    # Distribute the remaining problems respecting the constraints
    for i in range(k - 1, -1, -1):
        while remaining_problems > 0:
            if (i < k - 1 and result[i] < result[i + 1] and result[i] * 2 >= result[i + 1]):
                result[i] += 1
                remaining_problems -= 1
            elif i == k - 1:
                result[i] += 1
                remaining_problems -= 1
            else:
                break

        if remaining_problems == 0:
            break

    if remaining_problems > 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

# Read input
n, k = map(int, input().split())
solve_polycarps_problem(n, k)