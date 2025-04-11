def create_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    matrix = [[0] * n for _ in range(n)]
    
    # Check if we can form a palindromic matrix
    odd_count = 0
    center_value = None
    
    for value, freq in count.items():
        if freq % 2 == 1:
            odd_count += 1
            center_value = value
        if odd_count > 1:
            return "NO"
    
    # Fill the matrix
    half = []
    for value, freq in count.items():
        half.extend([value] * (freq // 2))
    
    if n % 2 == 1 and center_value is not None:
        center_row = n // 2
        center_col = n // 2
        matrix[center_row][center_col] = center_value
    
    # Fill the top half and bottom half
    index = 0
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            if index < len(half):
                matrix[i][j] = half[index]
                matrix[i][n - j - 1] = half[index]
                matrix[n - i - 1][j] = half[index]
                matrix[n - i - 1][n - j - 1] = half[index]
                index += 1
    
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