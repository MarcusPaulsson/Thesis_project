def create_palindromic_matrix(n, numbers):
    from collections import Counter
    
    # Count occurrences of each number
    count = Counter(numbers)
    
    # Check if the counts can form a palindromic matrix
    odd_count = 0
    for freq in count.values():
        if freq % 2 == 1:
            odd_count += 1
            
    # For even n, there can be no odd counts, for odd n, there can be at most one odd count
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO"
    
    # Create the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix with numbers
    half_matrix = []
    for num, freq in count.items():
        half_matrix.extend([num] * (freq // 2))
    
    # Create full palindromic matrix
    idx = 0
    for i in range(n):
        for j in range(n):
            if i < n // 2:
                matrix[i][j] = half_matrix[idx]
                matrix[n - 1 - i][j] = half_matrix[idx]
                matrix[i][n - 1 - j] = half_matrix[idx]
                matrix[n - 1 - i][n - 1 - j] = half_matrix[idx]
                idx += 1
            elif n % 2 == 1 and i == n // 2:
                if j == n // 2:
                    # Place the odd count number in the center if needed
                    for num, freq in count.items():
                        if freq % 2 == 1:
                            matrix[i][j] = num
                            break
    
    return "YES", matrix

# Input reading
n = int(input())
numbers = list(map(int, input().split()))

# Function call to create the palindromic matrix
result = create_palindromic_matrix(n, numbers)

# Output result
if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(' '.join(map(str, row)))