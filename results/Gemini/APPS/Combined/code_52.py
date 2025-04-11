def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_dp(row_idx, total_sum_mod_k):
        if (row_idx, total_sum_mod_k) in dp:
            return dp[(row_idx, total_sum_mod_k)]

        if row_idx == n:
            if total_sum_mod_k == 0:
                return 0
            else:
                return float('-inf')

        max_sum = float('-inf')
        
        # Option 1: Don't pick any elements from the current row
        max_sum = max(max_sum, get_dp(row_idx + 1, total_sum_mod_k))

        # Option 2: Pick some elements from the current row
        row = a[row_idx]
        max_elements = m // 2
        
        for num_elements in range(1, max_elements + 1):
            for combination in combinations(row, num_elements):
                current_sum = sum(combination)
                max_sum = max(max_sum, current_sum + get_dp(row_idx + 1, (total_sum_mod_k + current_sum) % k))

        dp[(row_idx, total_sum_mod_k)] = max_sum
        return max_sum

    from itertools import combinations
    print(get_dp(0, 0))

solve()