def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_dp(row_idx, total_sum_mod_k):
        if row_idx == n:
            return 0 if total_sum_mod_k == 0 else float('-inf')
        
        if (row_idx, total_sum_mod_k) in dp:
            return dp[(row_idx, total_sum_mod_k)]

        max_sum = float('-inf')

        for count in range(min(m // 2 + 1, m + 1)):
            for mask in range(1 << m):
                selected_count = 0
                current_sum = 0
                for j in range(m):
                    if (mask >> j) & 1:
                        selected_count += 1
                        current_sum += a[row_idx][j]
                
                if selected_count == count:
                    max_sum = max(max_sum, current_sum + get_dp(row_idx + 1, (total_sum_mod_k + current_sum) % k))
        
        dp[(row_idx, total_sum_mod_k)] = max_sum
        return max_sum

    print(get_dp(0, 0))

solve()