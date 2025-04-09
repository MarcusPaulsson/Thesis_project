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

        max_sum = float('-inf')
        
        # Option 1: Don't pick any element from the current row
        max_sum = max(max_sum, get_dp(row_idx + 1, rem))
        
        # Option 2: Pick elements from the current row
        max_elements = m // 2
        
        for i in range(1 << m):
            count = 0
            current_sum = 0
            elements = []
            for j in range(m):
                if (i >> j) & 1:
                    count += 1
                    current_sum += a[row_idx][j]
                    elements.append(a[row_idx][j])

            if count <= max_elements:
                new_rem = (rem - (current_sum % k)) % k
                if new_rem < 0:
                    new_rem += k
                max_sum = max(max_sum, current_sum + get_dp(row_idx + 1, new_rem))

        dp[(row_idx, rem)] = max_sum
        return max_sum

    print(get_dp(0, 0))

solve()