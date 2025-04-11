def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def calculate_max_sum(row_index, current_sum_mod):
        if row_index == n:
            if current_sum_mod == 0:
                return 0
            else:
                return -float('inf')

        if (row_index, current_sum_mod) in dp:
            return dp[(row_index, current_sum_mod)]

        max_elements = m // 2
        row = a[row_index]

        row_dp = {}

        def calculate_row_max_sum(col_index, elements_chosen, current_row_sum_mod):
            if col_index == m:
                if elements_chosen <= max_elements:
                    return 0 if current_row_sum_mod == 0 else -float('inf')
                else:
                    return -float('inf')

            if (col_index, elements_chosen, current_row_sum_mod) in row_dp:
                return row_dp[(col_index, elements_chosen, current_row_sum_mod)]

            choose = -float('inf')
            if elements_chosen < max_elements:
                new_row_sum_mod = (current_row_sum_mod + row[col_index]) % k
                choose = row[col_index] + calculate_row_max_sum(col_index + 1, elements_chosen + 1, new_row_sum_mod)

            skip = calculate_row_max_sum(col_index + 1, elements_chosen, current_row_sum_mod)

            row_dp[(col_index, elements_chosen, current_row_sum_mod)] = max(choose, skip)
            return row_dp[(col_index, elements_chosen, current_row_sum_mod)]

        max_row_sum = calculate_row_max_sum(0, 0, 0)
        
        max_val = -float('inf')
        for row_sum_mod in range(k):
            row_dp_mod = {}

            def calculate_row_max_sum_with_sum(col_index, elements_chosen, current_row_sum, current_row_sum_mod):
                if col_index == m:
                    if elements_chosen <= max_elements:
                        return current_row_sum if current_row_sum_mod == 0 else -float('inf')
                    else:
                        return -float('inf')

                if (col_index, elements_chosen, current_row_sum_mod) in row_dp_mod:
                    return row_dp_mod[(col_index, elements_chosen, current_row_sum_mod)]

                choose = -float('inf')
                if elements_chosen < max_elements:
                    new_row_sum_mod = (current_row_sum_mod + row[col_index]) % k
                    choose = calculate_row_max_sum_with_sum(col_index + 1, elements_chosen + 1, current_row_sum + row[col_index], new_row_sum_mod)

                skip = calculate_row_max_sum_with_sum(col_index + 1, elements_chosen, current_row_sum, current_row_sum_mod)

                row_dp_mod[(col_index, elements_chosen, current_row_sum_mod)] = max(choose, skip)
                return row_dp_mod[(col_index, elements_chosen, current_row_sum_mod)]

            row_max_sum_val = calculate_row_max_sum_with_sum(0, 0, 0, row_sum_mod)
            
            max_val = max(max_val, row_max_sum_val + calculate_max_sum(row_index + 1, (current_sum_mod + row_sum_mod) % k))

        dp[(row_index, current_sum_mod)] = max_val
        return max_val

    result = calculate_max_sum(0, 0)
    print(result)

solve()