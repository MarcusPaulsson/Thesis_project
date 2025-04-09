def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    solved_count = 0
    left = 0
    right = n - 1

    while left <= right:
        if a[left] <= k:
            solved_count += 1
            left += 1
        elif a[right] <= k:
            solved_count += 1
            right -= 1
        else:
            break

    print(solved_count)

solve()