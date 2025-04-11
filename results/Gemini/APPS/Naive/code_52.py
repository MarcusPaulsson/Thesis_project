def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}
    def get_dp(row_idx, rem):
        if (row_idx, rem) in dp:
            return dp[(row_idx, rem)]
        return None

    def set_dp(row_idx, rem, val):
        dp[(row_idx, rem)] = val

    def calculate_max_sum(row_idx, rem):
        if row_idx == n:
            if rem == 0:
                return 0
            else:
                return float('-inf')

        cached_result = get_dp(row_idx, rem)
        if cached_result is not None:
            return cached_result

        max_elements = m // 2
        row = a[row_idx]
        
        max_sum = float('-inf')
        
        for i in range(1 << m):
            chosen_elements = []
            count = 0
            current_sum = 0
            
            for j in range(m):
                if (i >> j) & 1:
                    chosen_elements.append(row[j])
                    count += 1
                    current_sum += row[j]
            
            if count <= max_elements:
                next_rem = (rem - (current_sum % k)) % k
                if next_rem < 0:
                    next_rem += k
                
                next_sum = calculate_max_sum(row_idx + 1, next_rem)
                if next_sum != float('-inf'):
                    max_sum = max(max_sum, current_sum + next_sum)
        
        set_dp(row_idx, rem, max_sum)
        return max_sum

    result = calculate_max_sum(0, 0)
    print(result)

solve()