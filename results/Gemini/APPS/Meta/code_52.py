def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}
    
    def get_dp(row_idx, total_elements, current_rem):
        if (row_idx, total_elements, current_rem) in dp:
            return dp[(row_idx, total_elements, current_rem)]
        
        if row_idx == n:
            if current_rem == 0:
                return 0
            else:
                return float('-inf')

        max_elements_per_row = m // 2
        
        row = a[row_idx]
        row_dp = {}
        
        def get_row_dp(col_idx, elements_taken, row_rem):
            if (col_idx, elements_taken, row_rem) in row_dp:
                return row_dp[(col_idx, elements_taken, row_rem)]
            
            if col_idx == m:
                if elements_taken <= max_elements_per_row:
                    return 0
                else:
                    return float('-inf')
            
            ans = get_row_dp(col_idx + 1, elements_taken, row_rem)
            
            if elements_taken < max_elements_per_row:
                new_rem = (row_rem + row[col_idx]) % k
                ans = max(ans, row[col_idx] + get_row_dp(col_idx + 1, elements_taken + 1, new_rem))
            
            row_dp[(col_idx, elements_taken, row_rem)] = ans
            return ans

        max_row_sum = float('-inf')
        for row_rem in range(k):
            row_sum = get_row_dp(0, 0, row_rem)
            if row_sum != float('-inf'):
                new_rem = (current_rem + row_rem) % k
                max_row_sum = max(max_row_sum, row_sum + get_dp(row_idx + 1, total_elements, new_rem))
                
        dp[(row_idx, total_elements, current_rem)] = max_row_sum
        return max_row_sum

    print(get_dp(0, 0, 0))

solve()