def create_palindromic_matrix(n, numbers):
    from collections import Counter

    # Count the occurrences of each number
    count = Counter(numbers)
    
    # Check for the number of odd occurrences
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    # For an n x n matrix, we can have at most one number with an odd count
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO"

    # Prepare the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix with the numbers
    half = []
    center = None
    
    for num, freq in count.items():
        if freq % 2 == 1:
            center = num  # This will be the center element if n is odd
        half.extend([num] * (freq // 2))
    
    # Create the palindromic structure
    half_size = len(half)
    for i in range(n // 2):
        for j in range(n // 2):
            matrix[i][j] = half[i * (n // 2) + j]
            matrix[i][n - j - 1] = matrix[i][j]
            matrix[n - i - 1][j] = matrix[i][j]
            matrix[n - i - 1][n - j - 1] = matrix[i][j]

    # If n is odd, place the center element
    if n % 2 == 1 and center is not None:
        mid = n // 2
        matrix[mid][mid] = center

    return "YES", matrix

# Input reading
n = int(input())
numbers = list(map(int, input().split()))

# Create the palindromic matrix
result = create_palindromic_matrix(n, numbers)

# Output the result
if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))