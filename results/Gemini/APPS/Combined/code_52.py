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

        def get_row_dp(col_idx, count, current_rem):
            if (col_idx, count, current_rem) in row_dp:
                return row_dp[(col_idx, count, current_rem)]

            if col_idx == m:
                if current_rem == 0:
                    return 0
                else:
                    return float('-inf')

            res = get_row_dp(col_idx + 1, count, current_rem)

            if count < max_elements:
                new_rem = (current_rem + row[col_idx]) % k
                res = max(res, row[col_idx] + get_row_dp(col_idx + 1, count + 1, new_rem))

            row_dp[(col_idx, count, current_rem)] = res
            return res

        max_row_sum = get_row_dp(0, 0, 0)

        ans = float('-inf')
        for row_rem in range(k):
            row_sum = get_row_dp(0, 0, row_rem)
            next_rem = (rem - row_rem) % k
            next_sum = get_dp(row_idx + 1, next_rem)
            if next_sum != float('-inf') and row_sum != float('-inf'):
                ans = max(ans, next_sum + row_sum)

        dp[(row_idx, rem)] = ans
        return ans

    print(get_dp(0, 0))


solve()