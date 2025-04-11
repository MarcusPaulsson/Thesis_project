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

        max_elements = m // 2
        
        row = a[row_idx]
        
        row_dp = {}
        
        def get_row_dp(col_idx, count, row_rem):
            if (col_idx, count, row_rem) in row_dp:
                return row_dp[(col_idx, count, row_rem)]
            
            if col_idx == m:
                return 0
            
            res = get_row_dp(col_idx + 1, count, row_rem)
            
            if count < max_elements:
                res = max(res, row[col_idx] + get_row_dp(col_idx + 1, count + 1, (row_rem + row[col_idx]) % k))
            
            row_dp[(col_idx, count, row_rem)] = res
            return res
        
        row_max = get_row_dp(0, 0, 0)
        
        ans = get_dp(row_idx + 1, rem)
        
        for row_rem in range(k):
            row_dp = {}
            def get_row_dp2(col_idx, count, row_rem):
                if (col_idx, count, row_rem) in row_dp:
                    return row_dp[(col_idx, count, row_rem)]
                
                if col_idx == m:
                    return 0 if row_rem == 0 else float('-inf')
                
                res = get_row_dp2(col_idx + 1, count, row_rem)
                
                if count < max_elements:
                    res = max(res, row[col_idx] + get_row_dp2(col_idx + 1, count + 1, (row_rem - row[col_idx]) % k))
                
                row_dp[(col_idx, count, row_rem)] = res
                return res
            
            row_max_rem = get_row_dp2(0, 0, row_rem)
            ans = max(ans, row_max_rem + get_dp(row_idx + 1, (rem - row_rem) % k))
        
        dp[(row_idx, rem)] = ans
        return ans

    print(get_dp(0, 0))

solve()