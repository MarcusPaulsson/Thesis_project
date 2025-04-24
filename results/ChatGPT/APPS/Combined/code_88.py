def create_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    matrix = [[0] * n for _ in range(n)]
    
    # Check for the number of odd occurrences
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)
    
    # Validate the possibility of creating a palindromic matrix
    if (n % 2 == 1 and odd_count > 1) or (n % 2 == 0 and odd_count > 0):
        return "NO"
    
    # Fill the half matrix with half of the frequencies
    half_matrix = []
    for num, freq in count.items():
        half_matrix.extend([num] * (freq // 2))
    
    # Create the top half of the matrix
    for i in range(n // 2):
        for j in range(n // 2):
            if half_matrix:
                value = half_matrix.pop()
                matrix[i][j] = value
                matrix[i][n - j - 1] = value
                matrix[n - i - 1][j] = value
                matrix[n - i - 1][n - j - 1] = value
    
    # If n is odd, place the center element
    if n % 2 == 1:
        center_row = n // 2
        center_col = n // 2
        for num, freq in count.items():
            if freq % 2 == 1:
                matrix[center_row][center_col] = num
                break
    
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