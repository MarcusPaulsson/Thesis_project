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

        dp_val = get_dp(row_idx, rem)
        if dp_val is not None:
            return dp_val

        max_choices = m // 2
        row = a[row_idx]
        
        row_dp = {}
        
        def get_row_dp(num_choices, row_rem):
            if (num_choices, row_rem) in row_dp:
                return row_dp[(num_choices, row_rem)]
            return None
        
        def set_row_dp(num_choices, row_rem, val):
            row_dp[(num_choices, row_rem)] = val

        def calculate_row_max_sum(num_choices, row_rem):
            if num_choices == 0:
                if row_rem == 0:
                    return 0
                else:
                    return float('-inf')
            
            if len(row) == 0:
                return float('-inf')
            
            row_dp_val = get_row_dp(num_choices, row_rem)
            if row_dp_val is not None:
                return row_dp_val
            
            include_val = row[0] + calculate_row_max_sum(num_choices - 1, (row_rem - row[0]) % k)
            exclude_val = calculate_row_max_sum(num_choices, row_rem)
            
            max_val = max(include_val, exclude_val)
            set_row_dp(num_choices, row_rem, max_val)
            return max_val

        max_row_sum = calculate_row_max_sum(max_choices, rem)
        
        
        skip_row = calculate_max_sum(row_idx + 1, rem)
        
        max_val = max(max_row_sum, skip_row)
        
        set_dp(row_idx, rem, max_val)
        return max_val

    result = calculate_max_sum(0, 0)
    print(result)

solve()