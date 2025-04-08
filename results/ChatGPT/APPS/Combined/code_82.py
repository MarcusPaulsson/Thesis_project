def max_problems_solved(n, k, problems):
    left_count = 0
    
    # Count solvable problems from the left
    while left_count < n and problems[left_count] <= k:
        left_count += 1
    
    right_count = 0
    # Count solvable problems from the right
    while right_count < n - left_count and problems[n - 1 - right_count] <= k:
        right_count += 1
    
    # Ensure we don't double count the middle problems if left and right counts overlap
    return left_count + right_count - (left_count + right_count > n)

# Input reading
n, k = map(int, input().split())
problems = list(map(int, input().split()))

# Output the result
print(max_problems_solved(n, k, problems))