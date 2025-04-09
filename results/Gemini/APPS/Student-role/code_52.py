def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    dp = {}

    def row_max_sum(row, max_elements, current_sum, index, chosen_count, cache):
        if (index, chosen_count, current_sum % k) in cache:
            return cache[(index, chosen_count, current_sum % k)]
        
        if index == len(row):
            return current_sum if current_sum % k == 0 else -float('inf')

        if chosen_count == max_elements:
            return row_max_sum(row, max_elements, current_sum, index + 1, chosen_count, cache)

        
        take = row_max_sum(row, max_elements, current_sum + row[index], index + 1, chosen_count+1, cache)
        dont_take = row_max_sum(row, max_elements, current_sum, index + 1, chosen_count, cache)

        cache[(index, chosen_count, current_sum % k)] = max(take, dont_take)
        return cache[(index, chosen_count, current_sum % k)]
    
    
    overall_dp = {}
    
    def overall_max_sum(row_index, current_sum, cache):
        if row_index == n:
            return current_sum if current_sum % k == 0 else -float('inf')
        
        if (row_index, current_sum % k) in cache:
            return cache[(row_index, current_sum % k)]

        row = a[row_index]
        max_elements = m // 2
        
        row_cache = {}
        max_row_sum = row_max_sum(row, max_elements, 0, 0, 0, row_cache)
        
        next_sum = overall_max_sum(row_index + 1, current_sum + max_row_sum, cache)
        
        
        cache[(row_index, current_sum % k)] = next_sum
        
        return cache[(row_index, current_sum % k)]
        
    
    result = overall_max_sum(0, 0, overall_dp)
    print(result)


solve()