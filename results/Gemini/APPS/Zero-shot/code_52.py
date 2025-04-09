def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_max_sum(row_index, current_sum):
        if row_index == n:
            if current_sum % k == 0:
                return current_sum
            else:
                return -float('inf')

        if (row_index, current_sum) in dp:
            return dp[(row_index, current_sum)]

        max_val = -float('inf')
        
        
        num_elements_to_choose = min(m // 2, m) 
        
        for i in range(1 << m):
            count = 0
            subset_sum = 0
            subset_indices = []
            for j in range(m):
                if (i >> j) & 1:
                    count += 1
                    subset_sum += a[row_index][j]
                    subset_indices.append(j)

            if count <= m // 2:
                max_val = max(max_val, get_max_sum(row_index + 1, current_sum + subset_sum))

        dp[(row_index, current_sum)] = max_val
        return max_val

    result = get_max_sum(0, 0)
    print(result)

solve()