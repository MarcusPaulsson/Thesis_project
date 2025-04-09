def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def max_sum_divisible_by_k(row_index, current_sum):
        if row_index == n:
            if current_sum % k == 0:
                return current_sum
            else:
                return -float('inf')
        
        if (row_index, current_sum) in dp:
            return dp[(row_index, current_sum)]
        
        max_val = max_sum_divisible_by_k(row_index + 1, current_sum)
        
        row = a[row_index]
        max_elements = m // 2
        
        for i in range(1 << m):
            count = 0
            subset_sum = 0
            elements = []
            
            for j in range(m):
                if (i >> j) & 1:
                    count += 1
                    subset_sum += row[j]
                    elements.append(row[j])
            
            if count <= max_elements:
                max_val = max(max_val, max_sum_divisible_by_k(row_index + 1, current_sum + subset_sum))

        dp[(row_index, current_sum)] = max_val
        return max_val

    result = max_sum_divisible_by_k(0, 0)
    print(result)

solve()