def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_dp(row_idx, rem):
        if (row_idx, rem) in dp:
            return dp[(row_idx, rem)]

        if row_idx == n:
            if rem == 0:
                return 0
            else:
                return float('-inf')
        
        max_sum_row = [[float('-inf')] * k for _ in range(m // 2 + 1)]
        max_sum_row[0][0] = 0
        
        for col_idx in range(m):
            val = a[row_idx][col_idx]
            for count in range(m // 2, 0, -1):
                for prev_rem in range(k):
                    new_rem = (prev_rem + val) % k
                    max_sum_row[count][new_rem] = max(max_sum_row[count][new_rem], max_sum_row[count-1][prev_rem] + val)
        
        best_row_sum = float('-inf')
        for count in range(m // 2 + 1):
            best_row_sum = max(best_row_sum, max_sum_row[count][rem])

        dp[(row_idx, rem)] = max(get_dp(row_idx + 1, rem), best_row_sum + get_dp(row_idx + 1, 0))
        
        for i in range(1, k):
            
            new_rem = (rem - i + k) %k
            best_row_sum_i = float('-inf')
            for count in range(m // 2 + 1):
                best_row_sum_i = max(best_row_sum_i, max_sum_row[count][i])
                
            dp[(row_idx, rem)] = max(dp[(row_idx, rem)], best_row_sum_i + get_dp(row_idx + 1, new_rem))
        
        return dp[(row_idx, rem)]

    print(get_dp(0, 0))

solve()