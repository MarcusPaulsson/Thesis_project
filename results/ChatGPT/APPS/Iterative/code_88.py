from collections import Counter

n = int(input())
a = list(map(int, input().split()))

count = Counter(a)
matrix = [[0] * n for _ in range(n)]

# Check for the number of odd counts
odd_count = 0
odd_value = None

for value, cnt in count.items():
    if cnt % 2 != 0:
        odd_count += 1
        odd_value = value

# If n is odd, we can have one odd count, if n is even, we can't have any
if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
    print("NO")
    exit()

# Fill the matrix
half = []
for value, cnt in count.items():
    half.extend([value] * (cnt // 2))

# Create the palindromic structure
for i in range(n // 2):
    for j in range(n // 2):
        matrix[i][j] = half.pop()
        matrix[i][n - j - 1] = matrix[i][j]
        matrix[n - i - 1][j] = matrix[i][j]
        matrix[n - i - 1][n - j - 1] = matrix[i][j]

# If n is odd, place the odd value in the center
if n % 2 == 1:
    matrix[n // 2][n // 2] = odd_value

print("YES")
for row in matrix:
    print(" ".join(map(str, row)))