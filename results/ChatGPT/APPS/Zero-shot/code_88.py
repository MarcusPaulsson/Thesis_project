n = int(input())
a = list(map(int, input().split()))

from collections import Counter

count = Counter(a)
matrix = [[0] * n for _ in range(n)]

# Check for the possibility of forming a palindromic matrix
odd_count = 0
for value, freq in count.items():
    if freq % 2 != 0:
        odd_count += 1

if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
    print("NO")
else:
    # Fill the matrix
    half_matrix = []
    for value, freq in count.items():
        half_matrix.extend([value] * (freq // 2))
    
    half_size = len(half_matrix)
    # Fill the top half of the matrix
    for i in range(n // 2):
        for j in range(n // 2):
            matrix[i][j] = half_matrix[i * (n // 2) + j]
            matrix[i][n - j - 1] = half_matrix[i * (n // 2) + j]
            matrix[n - i - 1][j] = half_matrix[i * (n // 2) + j]
            matrix[n - i - 1][n - j - 1] = half_matrix[i * (n // 2) + j]

    # Fill the center if n is odd
    if n % 2 == 1:
        center_value = None
        for value, freq in count.items():
            if freq % 2 == 1:
                center_value = value
                break
        for i in range(n):
            matrix[i][n // 2] = center_value
            matrix[n // 2][i] = center_value

    print("YES")
    for row in matrix:
        print(" ".join(map(str, row)))