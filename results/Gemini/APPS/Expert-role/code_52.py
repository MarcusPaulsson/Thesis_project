def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}
    
    def get_dp(row_idx, current_sum):
        if row_idx == n:
            if current_sum % k == 0:
                return 0
            else:
                return float('-inf')
        
        if (row_idx, current_sum) in dp:
            return dp[(row_idx, current_sum)]
        
        max_sum = float('-inf')
        
        # Iterate through all possible combinations of elements in the current row
        max_elements = m // 2
        for i in range(1 << m):
            elements = []
            count = 0
            row_sum = 0
            
            for j in range(m):
                if (i >> j) & 1:
                    elements.append(a[row_idx][j])
                    count += 1
                    row_sum += a[row_idx][j]
                    
            if count <= max_elements:
                max_sum = max(max_sum, row_sum + get_dp(row_idx + 1, current_sum + row_sum))
                
        dp[(row_idx, current_sum)] = max_sum
        return max_sum

    result = get_dp(0, 0)
    print(result)

solve()