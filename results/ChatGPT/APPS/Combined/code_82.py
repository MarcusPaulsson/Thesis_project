def max_problems_solved(n, k, difficulties):
    left, right = 0, n - 1
    solved_count = 0

    while left <= right:
        if difficulties[left] <= k:
            solved_count += 1
            left += 1
        elif difficulties[right] <= k:
            solved_count += 1
            right -= 1
        else:
            break

    return solved_count

# Input reading
n, k = map(int, input().split())
difficulties = list(map(int, input().split()))

# Get and print the result
result = max_problems_solved(n, k, difficulties)
print(result)