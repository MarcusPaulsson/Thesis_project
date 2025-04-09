def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_dp(row_idx, current_rem):
        if (row_idx, current_rem) in dp:
            return dp[(row_idx, current_rem)]

        if row_idx == n:
            if current_rem == 0:
                return 0
            else:
                return -float('inf')

        max_sum = -float('inf')
        
        for count in range(min(m // 2 + 1, m + 1)):
            
            def find_max_sum(arr, target_count):
                if target_count == 0:
                    return 0
                
                if len(arr) < target_count:
                    return -float('inf')

                if target_count == len(arr):
                    return sum(arr)
                
                
                
                max_s = -float('inf')
                
                
                for i in range(1 << len(arr)):
                    subset_sum = 0
                    subset_count = 0
                    
                    for j in range(len(arr)):
                        if (i >> j) & 1:
                            subset_sum += arr[j]
                            subset_count += 1
                            
                    if subset_count == target_count:
                        max_s = max(max_s, subset_sum)

                
                return max_s

            
            
            row_values = a[row_idx]
            row_max_sum = find_max_sum(row_values, count)
            
            if row_max_sum != -float('inf'):
                max_sum = max(max_sum, row_max_sum + get_dp(row_idx + 1, (current_rem + row_max_sum) % k))
            
            
        dp[(row_idx, current_rem)] = max_sum
        return max_sum

    print(get_dp(0, 0))

solve()