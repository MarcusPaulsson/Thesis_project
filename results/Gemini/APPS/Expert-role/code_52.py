def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def calculate_max_sum(row_index, current_sum):
        if row_index == n:
            if current_sum % k == 0:
                return current_sum
            else:
                return -float('inf')

        if (row_index, current_sum) in dp:
            return dp[(row_index, current_sum)]
        
        max_sum_for_row = -float('inf')
        
        # Iterate through all possible combinations of elements in the current row
        for i in range(1 << m):
            count = 0
            row_sum = 0
            elements = []
            for j in range(m):
                if (i >> j) & 1:
                    count += 1
                    row_sum += a[row_index][j]
                    elements.append(a[row_index][j])
            
            if count <= m // 2:
                max_sum_for_row = max(max_sum_for_row, calculate_max_sum(row_index + 1, current_sum + row_sum))

        dp[(row_index, current_sum)] = max_sum_for_row
        return max_sum_for_row

    result = calculate_max_sum(0, 0)
    print(result)

solve()