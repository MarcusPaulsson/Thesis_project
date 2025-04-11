def create_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    matrix = [[0] * n for _ in range(n)]
    
    # Check if we can form a palindromic matrix
    odd_count = 0
    center_value = None
    
    for value, cnt in count.items():
        if cnt % 2 != 0:
            odd_count += 1
            center_value = value
        if odd_count > 1:
            return "NO"
    
    # Fill the matrix
    half_matrix = []
    for value, cnt in count.items():
        half_matrix.extend([value] * (cnt // 2))
    
    half_size = len(half_matrix)
    if n % 2 == 0:
        # Even size matrix
        for i in range(n // 2):
            for j in range(n // 2):
                matrix[i][j] = half_matrix[i * (n // 2) + j]
                matrix[i][n - j - 1] = matrix[i][j]
                matrix[n - i - 1][j] = matrix[i][j]
                matrix[n - i - 1][n - j - 1] = matrix[i][j]
    else:
        # Odd size matrix
        for i in range(n // 2):
            for j in range(n // 2):
                matrix[i][j] = half_matrix[i * (n // 2) + j]
                matrix[i][n - j - 1] = matrix[i][j]
                matrix[n - i - 1][j] = matrix[i][j]
                matrix[n - i - 1][n - j - 1] = matrix[i][j]
        
        # Place the center value
        matrix[n // 2][n // 2] = center_value
    
    return "YES", matrix

n = int(input())
numbers = list(map(int, input().split()))

result = create_palindromic_matrix(n, numbers)
if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))