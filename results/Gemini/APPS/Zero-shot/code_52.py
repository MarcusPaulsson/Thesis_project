def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}
    def get_dp(row_idx, remaining_rows, current_sum):
        if (row_idx, remaining_rows, current_sum) in dp:
            return dp[(row_idx, remaining_rows, current_sum)]

        if row_idx == n:
            if current_sum % k == 0:
                return 0
            else:
                return float('-inf')

        max_sum = get_dp(row_idx + 1, remaining_rows - 1, current_sum)

        row = a[row_idx]
        max_row_sum = 0

        
        row_dp = {}
        def get_row_dp(col_idx, remaining_cols, current_row_sum):
            if (col_idx, remaining_cols, current_row_sum) in row_dp:
                return row_dp[(col_idx, remaining_cols, current_row_sum)]
            
            if col_idx == m:
                if remaining_cols == 0:
                    return current_row_sum
                else:
                    return float('-inf')

            if remaining_cols == 0:
                return 0
            
            val1 = get_row_dp(col_idx + 1, remaining_cols, current_row_sum)
            val2 = get_row_dp(col_idx + 1, remaining_cols - 1, current_row_sum + row[col_idx])
            
            row_dp[(col_idx, remaining_cols, current_row_sum)] = max(val1, val2)
            return row_dp[(col_idx, remaining_cols, current_row_sum)]
        

        max_row_sum = get_row_dp(0, m // 2, 0)
        
        max_sum = max(max_sum, get_dp(row_idx + 1, remaining_rows - 1, current_sum + max_row_sum))
        dp[(row_idx, remaining_rows, current_sum)] = max_sum
        return max_sum

    print(get_dp(0, n, 0))

solve()