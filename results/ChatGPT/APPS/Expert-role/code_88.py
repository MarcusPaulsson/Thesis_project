def construct_palindromic_matrix(n, numbers):
    from collections import Counter
    
    # Count occurrences of each number
    count = Counter(numbers)
    
    # Check for impossible conditions
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    # For an n x n matrix, we can have at most one odd-count number if n is odd
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO"
    
    # Create a list of half of the palindromic matrix
    half_matrix = []
    center_row = [0] * n if n % 2 == 1 else None
    
    # Fill the half matrix and center row if needed
    for value, cnt in count.items():
        pairs = cnt // 2
        for _ in range(pairs):
            half_matrix.append(value)
        
        if cnt % 2 == 1:
            if n % 2 == 1:
                center_row[n // 2] = value  # Place in the center for odd n
            else:
                return "NO"  # Can't have an odd count in even n

    # Prepare the full matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the half matrix into the top-left quadrant
    idx = 0
    for i in range(n):
        for j in range(n):
            if i <= n // 2 and j <= n // 2:
                if i == n - 1 - i and j == n - 1 - j:
                    # Center cell for odd n
                    matrix[i][j] = center_row[j] if center_row else 0
                elif i == n - 1 - i:
                    # Fill the row in the middle
                    matrix[i][j] = half_matrix[idx]
                    matrix[i][n - 1 - j] = half_matrix[idx]
                    idx += 1
                elif j == n - 1 - j:
                    # Fill the column in the middle
                    matrix[i][j] = half_matrix[idx]
                    matrix[n - 1 - i][j] = half_matrix[idx]
                    idx += 1
                else:
                    matrix[i][j] = half_matrix[idx]
                    matrix[n - 1 - i][j] = half_matrix[idx]
                    matrix[i][n - 1 - j] = half_matrix[idx]
                    matrix[n - 1 - i][n - 1 - j] = half_matrix[idx]
                    idx += 1

    return "YES", matrix

n = int(input())
numbers = list(map(int, input().split()))

result = construct_palindromic_matrix(n, numbers)

if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))