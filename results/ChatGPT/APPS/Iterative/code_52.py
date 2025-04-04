def max_sum_divisible_by_k(n, m, k, matrix):
    from itertools import combinations

    max_elements = m // 2
    total_sum = 0

    # Process each row to get the best possible sums modulo k
    for row in matrix:
        best_mod_sums = [0] * k  # Array to keep track of max sums for each modulo k

        # Consider all combinations of choosing up to max_elements from the row
        for count in range(max_elements + 1):
            for combo in combinations(row, count):
                current_sum = sum(combo)
                mod = current_sum % k
                best_mod_sums[mod] = max(best_mod_sums[mod], current_sum)

        # Add the best found sum to the total sum
        total_sum += max(best_mod_sums)

    return total_sum

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)