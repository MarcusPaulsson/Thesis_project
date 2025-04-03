def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    dp = {}
    
    def get_max_sum(row_idx, rem):
        if row_idx == n:
            if rem == 0:
                return 0
            else:
                return -float('inf')
            
        if (row_idx, rem) in dp:
            return dp[(row_idx, rem)]
        
        max_elements_per_row = m // 2
        
        max_sum = get_max_sum(row_idx + 1, rem)
        
        for num_elements in range(1, max_elements_per_row + 1):
            for combination in combinations(a[row_idx], num_elements):
                current_sum = sum(combination)
                new_rem = (rem - current_sum) % k
                max_sum = max(max_sum, current_sum + get_max_sum(row_idx + 1, new_rem))
        
        dp[(row_idx, rem)] = max_sum
        return max_sum
        
    from itertools import combinations
    
    print(get_max_sum(0, 0))

solve()