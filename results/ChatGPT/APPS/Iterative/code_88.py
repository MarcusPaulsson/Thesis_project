n = int(input())
a = list(map(int, input().split()))

from collections import Counter

counter = Counter(a)
matrix = [[0] * n for _ in range(n)]

# Count how many numbers can fit into the palindrome structure
odd_count = 0
even_pairs = []
for num, count in counter.items():
    if count % 2 == 1:
        odd_count += 1
    even_pairs.append(count // 2)

# For odd n, we can have one odd count; for even n, we can't have any
if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
    print("NO")
else:
    # Prepare half of the matrix and the center element if needed
    half = []
    center_element = None
    
    for num, count in counter.items():
        half.extend([num] * (count // 2))
        if count % 2 == 1:
            center_element = num

    # Fill the matrix
    index = 0
    for i in range(n):
        for j in range(n):
            if i < n // 2:  # Fill top half
                matrix[i][j] = half[index]
                matrix[n - i - 1][n - j - 1] = half[index]
                if j < n // 2:
                    index += 1
            
            elif i == n // 2 and n % 2 == 1:  # Fill the center row
                if j == n // 2:
                    matrix[i][j] = center_element
            
            else:  # Fill bottom half
                matrix[i][j] = matrix[n - i - 1][n - j - 1]

    print("YES")
    for row in matrix:
        print(" ".join(map(str, row)))