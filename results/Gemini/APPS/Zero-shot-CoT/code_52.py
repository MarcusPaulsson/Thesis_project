def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}
    def get_dp(row_idx, rem):
        if row_idx == n:
            return 0 if rem == 0 else -float('inf')
        
        if (row_idx, rem) in dp:
            return dp[(row_idx, rem)]

        max_sum = -float('inf')
        
        # Option 1: Don't choose any element from the current row
        max_sum = max(max_sum, get_dp(row_idx + 1, rem))

        # Option 2: Choose some elements from the current row
        row = a[row_idx]
        max_elements = m // 2
        
        row_dp = {}
        def get_row_dp(col_idx, count, row_rem):
            if col_idx == m:
                return 0 if count <= max_elements else -float('inf')
            
            if (col_idx, count, row_rem) in row_dp:
                return row_dp[(col_idx, count, row_rem)]
            
            # Option 1: Don't choose the current element
            current_max = get_row_dp(col_idx + 1, count, row_rem)
            
            # Option 2: Choose the current element
            current_max = max(current_max, row[col_idx] + get_row_dp(col_idx + 1, count + 1, (row_rem - row[col_idx]) % k))
            
            row_dp[(col_idx, count, row_rem)] = current_max
            return current_max
        
        row_result = get_row_dp(0, 0, rem)
        max_sum = max(max_sum, row_result + get_dp(row_idx + 1, rem))

        dp[(row_idx, rem)] = max_sum
        return max_sum

    print(get_dp(0, 0))

solve()