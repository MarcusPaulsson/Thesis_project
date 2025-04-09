def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_dp(row_idx, total_sum_rem):
        if (row_idx, total_sum_rem) in dp:
            return dp[(row_idx, total_sum_rem)]

        if row_idx == n:
            if total_sum_rem == 0:
                return 0
            else:
                return -float('inf')

        max_sum = -float('inf')
        
        # Case 1: Don't pick any element from the current row
        max_sum = max(max_sum, get_dp(row_idx + 1, total_sum_rem))

        # Case 2: Pick elements from the current row
        row = a[row_idx]
        max_picks = m // 2
        
        row_dp = {}

        def get_row_dp(col_idx, num_picks, row_sum_rem):
            if (col_idx, num_picks, row_sum_rem) in row_dp:
                return row_dp[(col_idx, num_picks, row_sum_rem)]
            
            if col_idx == m:
                if num_picks <= max_picks:
                    return 0
                else:
                    return -float('inf')
            
            res = -float('inf')
            
            #Don't pick the current element
            res = max(res, get_row_dp(col_idx + 1, num_picks, row_sum_rem))
            
            #Pick the current element
            res = max(res, row[col_idx] + get_row_dp(col_idx + 1, num_picks + 1, (row_sum_rem + row[col_idx]) % k))
            
            row_dp[(col_idx, num_picks, row_sum_rem)] = res
            return res
        
        row_max_sum = get_row_dp(0, 0, 0)
        max_sum = max(max_sum, row_max_sum + get_dp(row_idx + 1, (total_sum_rem + 0) % k))
        
        
        row_max_rem_sums = {}
        
        def get_row_max_rem_sum(col_idx, num_picks, row_sum_rem):
            if (col_idx, num_picks, row_sum_rem) in row_max_rem_sums:
                return row_max_rem_sums[(col_idx, num_picks, row_sum_rem)]

            if col_idx == m:
                if num_picks <= max_picks:
                    return 0
                else:
                    return -float('inf')

            res = -float('inf')

            # Don't pick the current element
            res = max(res, get_row_max_rem_sum(col_idx + 1, num_picks, row_sum_rem))

            # Pick the current element
            res = max(res, row[col_idx] + get_row_max_rem_sum(col_idx + 1, num_picks + 1, (row_sum_rem + row[col_idx]) % k))

            row_max_rem_sums[(col_idx, num_picks, row_sum_rem)] = res
            return res
        
        for rem in range(k):
            row_max_sum_for_rem = get_row_max_rem_sum(0, 0, 0 if rem == 0 else rem)
            max_sum = max(max_sum, row_max_sum_for_rem + get_dp(row_idx + 1, (total_sum_rem) % k))
            
        
        
        row_sums_by_rem = [get_row_max_rem_sum(0, 0, rem) for rem in range(k)]
        for rem in range(k):
            max_sum = max(max_sum, row_sums_by_rem[rem] + get_dp(row_idx + 1, (total_sum_rem + rem) % k))

        dp[(row_idx, total_sum_rem)] = max_sum
        return max_sum

    print(get_dp(0, 0))

solve()