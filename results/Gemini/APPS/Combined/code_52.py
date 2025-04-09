def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_max_sum(row_idx, current_sum):
        if row_idx == n:
            if current_sum % k == 0:
                return current_sum
            else:
                return -float('inf')

        if (row_idx, current_sum % k) in dp:
            return dp[(row_idx, current_sum % k)]

        max_elements = m // 2
        max_sum_for_row = -float('inf')

        for i in range(1 << m):
            count = 0
            row_sum = 0
            for j in range(m):
                if (i >> j) & 1:
                    count += 1
                    row_sum += a[row_idx][j]

            if count <= max_elements:
                max_sum_for_row = max(max_sum_for_row, get_max_sum(row_idx + 1, current_sum + row_sum))

        dp[(row_idx, current_sum % k)] = max_sum_for_row
        return max_sum_for_row

    result = get_max_sum(0, 0)
    print(result)

solve()