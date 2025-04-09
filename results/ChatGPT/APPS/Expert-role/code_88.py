def create_palindromic_matrix(n, numbers):
    from collections import Counter

    count = Counter(numbers)
    matrix = [[0] * n for _ in range(n)]
    
    # Check if it's possible to create a palindromic matrix
    odd_count = 0
    center_value = None
    
    for value, cnt in count.items():
        if cnt % 2 != 0:
            odd_count += 1
            center_value = value
        if odd_count > 1:
            return "NO"
    
    # Fill the matrix
    # Half the matrix (the upper half and the left half)
    for i in range((n + 1) // 2):
        for j in range((n + 1) // 2):
            if i == j and n % 2 == 1 and odd_count == 1:
                # Place center value in the middle for odd sizes
                matrix[i][j] = center_value
                count[center_value] -= 1
            else:
                for value in list(count.keys()):
                    if count[value] >= 4:
                        matrix[i][j] = value
                        matrix[i][n - j - 1] = value
                        matrix[n - i - 1][j] = value
                        matrix[n - i - 1][n - j - 1] = value
                        count[value] -= 4
                        break
    
    # Fill any remaining values if necessary
    for value, cnt in count.items():
        while cnt > 0:
            placed = False
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == 0:
                        matrix[i][j] = value
                        cnt -= 1
                        placed = True
                        if cnt == 0:
                            break
                if not placed:
                    break
            if cnt == 0:
                break
    
    return "YES", matrix

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Get result
result = create_palindromic_matrix(n, numbers)

# Output
if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))