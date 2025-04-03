n = int(input())
a = list(map(int, input().split()))

from collections import Counter

count = Counter(a)
matrix = [[0] * n for _ in range(n)]

# Check for the number of elements that can be placed in the matrix
odd_count = 0
for value, freq in count.items():
    if freq % 2 == 1:
        odd_count += 1

# For odd n, we can have at most one odd frequency
if n % 2 == 1 and odd_count > 1:
    print("NO")
    exit()

# For even n, we cannot have any odd frequencies
if n % 2 == 0 and odd_count > 0:
    print("NO")
    exit()

# Place the numbers in the palindromic fashion
pairs = []
single = None

for value, freq in count.items():
    pairs.extend([value] * (freq // 2))
    if freq % 2 == 1:
        single = value

# Fill the matrix
half_n = n // 2
idx = 0

for i in range(half_n):
    for j in range(half_n):
        if idx < len(pairs):
            matrix[i][j] = pairs[idx]
            matrix[i][n - j - 1] = pairs[idx]
            matrix[n - i - 1][j] = pairs[idx]
            matrix[n - i - 1][n - j - 1] = pairs[idx]
            idx += 1

# If n is odd, place the single element in the center
if n % 2 == 1:
    matrix[half_n][half_n] = single

print("YES")
for row in matrix:
    print(" ".join(map(str, row)))