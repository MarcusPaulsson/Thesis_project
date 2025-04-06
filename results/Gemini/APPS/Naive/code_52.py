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
        
        max_sum = float('-inf')
        
        # Option 1: Don't pick any element from this row
        max_sum = max(max_sum, get_dp(row_idx + 1, rem))

        # Option 2: Pick elements from this row
        row = a[row_idx]
        max_picks = m // 2

        row_dp = {}
        def get_row_dp(col_idx, picks, row_rem):
            if (col_idx, picks, row_rem) in row_dp:
                return row_dp[(col_idx, picks, row_rem)]

            if col_idx == m:
                if picks == 0:
                    return 0
                else:
                    return float('-inf')

            res = float('-inf')
            
            # Don't pick this element
            res = max(res, get_row_dp(col_idx + 1, picks, row_rem))

            # Pick this element if possible
            if picks > 0:
                res = max(res, row[col_idx] + get_row_dp(col_idx + 1, picks - 1, (row_rem - row[col_idx]) % k))
            
            row_dp[(col_idx, picks, row_rem)] = res
            return res

        for num_picks in range(1, max_picks + 1):
            for row_rem in range(k):
                row_sum = get_row_dp(0, num_picks, row_rem)
                max_sum = max(max_sum, row_sum + get_dp(row_idx + 1, (rem - row_rem) % k))

        dp[(row_idx, rem)] = max_sum
        return max_sum
    
    print(get_dp(0, 0))

solve()