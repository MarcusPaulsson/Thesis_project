def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def calculate_max_sum(row_idx, rem):
        if row_idx == n:
            if rem == 0:
                return 0
            else:
                return float('-inf')

        if (row_idx, rem) in dp:
            return dp[(row_idx, rem)]

        max_elements = m // 2
        row = a[row_idx]
        
        max_sum = calculate_max_sum(row_idx + 1, rem)

        for i in range(1 << m):
            count = 0
            current_sum = 0
            for j in range(m):
                if (i >> j) & 1:
                    count += 1
                    current_sum += row[j]

            if count <= max_elements:
                new_rem = (rem - (current_sum % k)) % k
                if new_rem < 0:
                    new_rem += k
                
                max_sum = max(max_sum, current_sum + calculate_max_sum(row_idx + 1, new_rem))

        dp[(row_idx, rem)] = max_sum
        return max_sum

    result = calculate_max_sum(0, 0)
    print(result)

solve()