def max_problems(n, k, problems):
    left = 0
    right = n - 1
    solved = 0

    while left <= right:
        if problems[left] <= k and problems[right] <= k:
            if problems[left] <= problems[right]:
                solved += 1
                left += 1
            else:
                solved += 1
                right -= 1
        elif problems[left] <= k:
            solved += 1
            left += 1
        elif problems[right] <= k:
            solved += 1
            right -= 1
        else:
            break

    return solved

n, k = map(int, input().split())
problems = list(map(int, input().split()))
print(max_problems(n, k, problems))