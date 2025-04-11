def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def get_dp(row_idx, current_sum, num_chosen):
        if (row_idx, current_sum, num_chosen) in dp:
            return dp[(row_idx, current_sum, num_chosen)]
        return None

    def set_dp(row_idx, current_sum, num_chosen, value):
        dp[(row_idx, current_sum, num_chosen)] = value

    def calculate_max_sum(row_idx, current_sum):
        if row_idx == n:
            if current_sum % k == 0:
                return current_sum
            else:
                return -1
        
        dp_val = get_dp(row_idx, current_sum % k, 0)
        if dp_val is not None:
            return dp_val

        max_elements = m // 2
        
        row = a[row_idx]
        
        row_dp = {}

        def get_row_dp(col_idx, row_sum, num_chosen):
            if (col_idx, row_sum, num_chosen) in row_dp:
                return row_dp[(col_idx, row_sum, num_chosen)]
            return None

        def set_row_dp(col_idx, row_sum, num_chosen, value):
            row_dp[(col_idx, row_sum, num_chosen)] = value

        def calculate_max_row_sum(col_idx, row_sum, num_chosen):
            if col_idx == m:
                return row_sum
            
            row_dp_val = get_row_dp(col_idx, row_sum, num_chosen)
            if row_dp_val is not None:
                return row_dp_val

            max_sum = calculate_max_row_sum(col_idx + 1, row_sum, num_chosen)
            
            if num_chosen < max_elements:
                max_sum = max(max_sum, calculate_max_row_sum(col_idx + 1, row_sum + row[col_idx], num_chosen + 1))
            
            set_row_dp(col_idx, row_sum, num_chosen, max_sum)
            return max_sum
        
        max_row_sum = calculate_max_row_sum(0, 0, 0)

        max_val = -1
        for row_sum_rem in range(k):
            row_sum = -1
            
            row_dp_rem = {}

            def get_row_dp_rem(col_idx, row_sum, num_chosen):
                if (col_idx, row_sum, num_chosen) in row_dp_rem:
                    return row_dp_rem[(col_idx, row_sum, num_chosen)]
                return None

            def set_row_dp_rem(col_idx, row_sum, num_chosen, value):
                row_dp_rem[(col_idx, row_sum, num_chosen)] = value

            def calculate_max_row_sum_rem(col_idx, row_sum, num_chosen):
                if col_idx == m:
                    if row_sum % k == row_sum_rem:
                        return row_sum
                    else:
                        return -1
                
                row_dp_val = get_row_dp_rem(col_idx, row_sum, num_chosen)
                if row_dp_val is not None:
                    return row_dp_val

                max_sum = calculate_max_row_sum_rem(col_idx + 1, row_sum, num_chosen)
                
                if num_chosen < max_elements:
                    max_sum = max(max_sum, calculate_max_row_sum_rem(col_idx + 1, row_sum + row[col_idx], num_chosen + 1))
                
                set_row_dp_rem(col_idx, row_sum, num_chosen, max_sum)
                return max_sum
            
            row_sum = calculate_max_row_sum_rem(0, 0, 0)

            if row_sum != -1:
                next_sum = calculate_max_sum(row_idx + 1, current_sum + row_sum)
                max_val = max(max_val, next_sum)
        
        set_dp(row_idx, current_sum % k, 0, max_val)
        return max_val

    result = calculate_max_sum(0, 0)
    print(result)

solve()