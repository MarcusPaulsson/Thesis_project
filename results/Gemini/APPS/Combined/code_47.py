def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    max_so_far = 0
    current_max = 0
    for i in range(n):
        current_max += a[i]
        if current_max < 0:
            current_max = 0
        max_so_far = max(max_so_far, current_max)

    ans = max_so_far

    for i in range(n):
        for j in range(i, n):
            temp_a = a[:]
            for k in range(i, j + 1):
                temp_a[k] *= x

            max_so_far = 0
            current_max = 0
            for k in range(n):
                current_max += temp_a[k]
                if current_max < 0:
                    current_max = 0
                max_so_far = max(max_so_far, current_max)
            ans = max(ans, max_so_far)

    print(ans)

solve()