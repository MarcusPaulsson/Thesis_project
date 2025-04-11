def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_dp(row_idx, current_sum):
        if (row_idx, current_sum) in dp:
            return dp[(row_idx, current_sum)]

        if row_idx == n:
            if current_sum % k == 0:
                return 0
            else:
                return float('-inf')

        max_sum_for_row = float('-inf')
        
        # Iterate through all possible combinations of elements in the current row
        for count in range(min(m // 2 + 1, m + 1)):
            for mask in range(1 << m):
                if bin(mask).count('1') == count:
                    row_sum = 0
                    for j in range(m):
                        if (mask >> j) & 1:
                            row_sum += a[row_idx][j]

                    max_sum_for_row = max(max_sum_for_row, row_sum + get_dp(row_idx + 1, (current_sum + row_sum) % k))

        dp[(row_idx, current_sum)] = max_sum_for_row
        return max_sum_for_row

    result = get_dp(0, 0)
    print(result)

solve()