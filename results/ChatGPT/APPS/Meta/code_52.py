def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements = m // 2
    total_sum = 0
    
    # Calculate the maximum possible sum for each row with constraints
    for row in matrix:
        row.sort(reverse=True)  # Sort row in descending order
        current_sum = 0
        current_elements = []
        
        for i in range(min(max_elements, len(row))):
            current_sum += row[i]
            current_elements.append(row[i])
        
        # Try all combinations of taking up to max_elements
        row_sums = {0}  # Start with taking no elements
        
        for value in current_elements:
            new_sums = set()
            for s in row_sums:
                new_sums.add(s + value)
            row_sums.update(new_sums)
        
        # Filter sums to get the maximum sum that is divisible by k
        max_divisible_sum = max((s for s in row_sums if s % k == 0), default=0)
        total_sum += max_divisible_sum
    
    return total_sum

# Input
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output
print(max_sum_divisible_by_k(n, m, k, matrix))