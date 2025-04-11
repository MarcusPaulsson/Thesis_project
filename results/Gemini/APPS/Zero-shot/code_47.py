def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            temp_a = a[:]
            for k in range(i, j):
                temp_a[k] *= x

            curr_max = 0
            max_so_far = 0
            for k in range(n):
                curr_max += temp_a[k]
                if curr_max < 0:
                    curr_max = 0
                max_so_far = max(max_so_far, curr_max)
            ans = max(ans, max_so_far)
    print(ans)

solve()