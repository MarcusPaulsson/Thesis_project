def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}
    def get_dp(row_idx, rem):
        if row_idx == n:
            if rem == 0:
                return 0
            else:
                return -float('inf')

        if (row_idx, rem) in dp:
            return dp[(row_idx, rem)]

        max_sum = get_dp(row_idx + 1, rem)

        row = a[row_idx]
        max_elements = m // 2

        row_dp = {}
        def get_row_dp(col_idx, num_elements, row_rem):
            if col_idx == m:
                if num_elements <= max_elements:
                    return 0
                else:
                    return -float('inf')
            
            if (col_idx, num_elements, row_rem) in row_dp:
                return row_dp[(col_idx, num_elements, row_rem)]

            res = get_row_dp(col_idx + 1, num_elements, row_rem)
            if num_elements < max_elements:
                res = max(res, get_row_dp(col_idx + 1, num_elements + 1, (row_rem + row[col_idx]) % k) + row[col_idx])
            
            row_dp[(col_idx, num_elements, row_rem)] = res
            return res
        
        for row_rem in range(k):
            row_max_sum = get_row_dp(0, 0, row_rem)
            max_sum = max(max_sum, get_dp(row_idx + 1, (rem - row_rem) % k) + row_max_sum)
            
        dp[(row_idx, rem)] = max_sum
        return max_sum

    print(get_dp(0, 0))

solve()