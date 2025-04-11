from collections import Counter

n = int(input())
a = list(map(int, input().split()))

count = Counter(a)
matrix = [[0] * n for _ in range(n)]

# Check for the number of odd occurrences
odd_count = 0
odd_value = None

for value, freq in count.items():
    if freq % 2 != 0:
        odd_count += 1
        odd_value = value
    if odd_count > 1:
        print("NO")
        exit()

# If n is odd, we can have one odd frequency number in the center
if n % 2 == 1 and odd_count == 0:
    print("NO")
    exit()

# Fill the matrix
half_matrix = []
for value, freq in count.items():
    half_matrix.extend([value] * (freq // 2))

# Create the palindromic structure
half_size = len(half_matrix)
center = [odd_value] * (n % 2)  # Only add the odd value if n is odd

# Fill the top half of the matrix
for i in range(n // 2):
    matrix[i] = half_matrix[i:half_size - i] + center + half_matrix[half_size - i:half_size][::-1]

# Fill the bottom half of the matrix
for i in range(n // 2):
    matrix[n - 1 - i] = matrix[i][:]

# If n is odd, fill the center row
if n % 2 == 1:
    matrix[n // 2] = center + half_matrix + half_matrix[::-1]

print("YES")
for row in matrix:
    print(" ".join(map(str, row)))