def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        row = a[i]
        max_choices = m // 2
        
        row_dp = [[-1] * k for _ in range(max_choices + 1)]
        row_dp[0][0] = 0
        
        for val in row:
            for count in range(max_choices, 0, -1):
                for rem in range(k):
                    if row_dp[count-1][rem] != -1:
                        new_rem = (rem + val) % k
                        row_dp[count][new_rem] = max(row_dp[count][new_rem], row_dp[count-1][rem] + val)
        
        for prev_rem in range(k):
            if dp[i][prev_rem] != -1:
                for count in range(max_choices + 1):
                    for row_rem in range(k):
                        if row_dp[count][row_rem] != -1:
                            new_rem = (prev_rem + row_rem) % k
                            dp[i+1][new_rem] = max(dp[i+1][new_rem], dp[i][prev_rem] + row_dp[count][row_rem])

    print(dp[n][0])

solve()