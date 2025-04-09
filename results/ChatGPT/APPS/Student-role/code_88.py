n = int(input())
a = list(map(int, input().split()))

from collections import Counter

count = Counter(a)
matrix = [[0] * n for _ in range(n)]

# Check if it is possible to fill the matrix
odd_count = 0
for value, freq in count.items():
    if freq % 2 == 1:
        odd_count += 1

# For odd n, we can have one odd frequency; for even n, we cannot have any
if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
    print("NO")
else:
    # Fill the matrix
    half_matrix = []
    center_value = None
    
    for value, freq in count.items():
        if freq % 2 == 1:
            center_value = value
        half_matrix.extend([value] * (freq // 2))
    
    half_size = len(half_matrix)
    
    # Arrange values in a palindromic way
    for i in range(n):
        for j in range(n):
            if i < n // 2:
                matrix[i][j] = half_matrix[i] if j < n // 2 else half_matrix[i]
                matrix[n - 1 - i][j] = matrix[i][j]
            elif i == n // 2 and n % 2 == 1:
                if j == n // 2:
                    matrix[i][j] = center_value
                else:
                    matrix[i][j] = half_matrix[i]
                    matrix[i][n - 1 - j] = matrix[i][j]

    print("YES")
    for row in matrix:
        print(' '.join(map(str, row)))