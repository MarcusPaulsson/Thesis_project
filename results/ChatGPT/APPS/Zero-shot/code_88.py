from collections import Counter

n = int(input())
a = list(map(int, input().split()))

# Count the frequency of each number
count = Counter(a)

# Check if we can form a palindromic matrix
odd_count = 0
for freq in count.values():
    if freq % 2 != 0:
        odd_count += 1

# For an n x n matrix:
# - If n is odd, we can have at most one number with an odd frequency.
# - If n is even, we cannot have any number with an odd frequency.
if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
    print("NO")
else:
    print("YES")
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix
    half = n // 2
    idx = 0
    for num, freq in count.items():
        while freq > 0:
            if freq >= 4:
                # Place in corners
                matrix[idx][idx] = num
                matrix[idx][n - 1 - idx] = num
                matrix[n - 1 - idx][idx] = num
                matrix[n - 1 - idx][n - 1 - idx] = num
                freq -= 4
            elif freq >= 2:
                # Place in sides
                if idx < half:
                    matrix[idx][n - 1 - idx] = num
                    matrix[n - 1 - idx][idx] = num
                    freq -= 2
                else:
                    break
            else:
                # Place in the center if n is odd
                if n % 2 == 1 and freq == 1:
                    matrix[half][half] = num
                    freq -= 1
                break
            idx += 1
            if idx >= half:
                idx = 0
    
    # Fill the remaining spots
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[n - 1 - i][j]
    
    for row in matrix:
        print(" ".join(map(str, row)))