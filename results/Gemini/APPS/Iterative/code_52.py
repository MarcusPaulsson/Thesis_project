def solve():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = {}

    def calculate_max_sum(row_index, current_sum):
        if (row_index, current_sum) in dp:
            return dp[(row_index, current_sum)]

        if row_index == n:
            if current_sum % k == 0:
                return 0
            else:
                return -float('inf')

        max_sum = -float('inf')

        for num_chosen in range(min(m // 2 + 1, m + 1)):
            for mask in range(1 << m):
                chosen_elements = []
                for j in range(m):
                    if (mask >> j) & 1:
                        chosen_elements.append(a[row_index][j])

                if len(chosen_elements) == num_chosen:
                    new_sum = sum(chosen_elements)
                    max_sum = max(max_sum, calculate_max_sum(row_index + 1, (current_sum + new_sum) % k))

        dp[(row_index, current_sum)] = max_sum
        return max_sum

    result = calculate_max_sum(0, 0)
    print(result)

solve()