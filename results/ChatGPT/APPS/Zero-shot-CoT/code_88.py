n = int(input())
a = list(map(int, input().split()))

from collections import Counter

count = Counter(a)

# Check if we can form a palindromic matrix
odd_count = 0
for value in count.values():
    if value % 2 != 0:
        odd_count += 1

# For odd n, we can have at most one odd count
# For even n, we cannot have any odd counts
if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
    print("NO")
else:
    # Create the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix
    half = []
    center = None
    
    for value, freq in count.items():
        if freq % 2 == 1:
            center = value  # For odd n, we can have a center element
        half.extend([value] * (freq // 2))
    
    half.sort()
    
    # Fill the top half of the matrix
    for i in range(n // 2):
        for j in range(n // 2):
            matrix[i][j] = half.pop(0)
            matrix[i][n - j - 1] = matrix[i][j]
            matrix[n - i - 1][j] = matrix[i][j]
            matrix[n - i - 1][n - j - 1] = matrix[i][j]
    
    # If n is odd, fill the center row and column
    if n % 2 == 1:
        for j in range(n):
            matrix[n // 2][j] = half.pop(0)
            matrix[j][n // 2] = half.pop(0)
        matrix[n // 2][n // 2] = center
    
    print("YES")
    for row in matrix:
        print(" ".join(map(str, row)))