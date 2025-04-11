def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_dp(row_idx, rem):
        if (row_idx, rem) in dp:
            return dp[(row_idx, rem)]
        return None

    def set_dp(row_idx, rem, value):
        dp[(row_idx, rem)] = value

    def calculate_max_sum(row_idx, rem):
        if row_idx == n:
            if rem == 0:
                return 0
            else:
                return float('-inf')

        cached_value = get_dp(row_idx, rem)
        if cached_value is not None:
            return cached_value

        max_elements = m // 2
        max_sum = float('-inf')

        # Option 1: Don't choose any element from this row
        max_sum = max(max_sum, calculate_max_sum(row_idx + 1, rem))

        # Option 2: Choose some elements from this row
        for i in range(1 << m):
            chosen_elements = []
            for j in range(m):
                if (i >> j) & 1:
                    chosen_elements.append(a[row_idx][j])

            if len(chosen_elements) <= max_elements:
                current_sum = sum(chosen_elements)
                new_rem = (rem - (current_sum % k)) % k
                if new_rem < 0:
                    new_rem += k
                max_sum = max(max_sum, current_sum + calculate_max_sum(row_idx + 1, new_rem))

        set_dp(row_idx, rem, max_sum)
        return max_sum

    print(calculate_max_sum(0, 0))

solve()