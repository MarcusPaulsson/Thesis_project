n = int(input())
a = list(map(int, input().split()))

from collections import Counter

count = Counter(a)
matrix = [[0] * n for _ in range(n)]

# Check for the number of odd occurrences
odd_count = sum(1 for v in count.values() if v % 2 != 0)

# For odd n, we can have at most one odd count, for even n, we can't have any
if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
    print("NO")
else:
    # Fill the matrix
    half = []
    center = None

    for num, freq in count.items():
        if freq % 2 == 1:
            center = num  # For the center of the matrix if n is odd
        half.extend([num] * (freq // 2))

    # Fill the matrix
    idx = 0
    for i in range((n + 1) // 2):
        for j in range((n + 1) // 2):
            if i == j and n % 2 == 1 and i == n // 2:
                matrix[i][j] = center
            else:
                matrix[i][j] = half[idx]
                matrix[i][n - j - 1] = half[idx]
                matrix[n - i - 1][j] = half[idx]
                matrix[n - i - 1][n - j - 1] = half[idx]
                idx += 1

    print("YES")
    for row in matrix:
        print(" ".join(map(str, row)))