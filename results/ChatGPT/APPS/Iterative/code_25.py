def create_symmetrical_matrix(n, k):
    # Check if the number of 1s is valid for a symmetric matrix
    if k > n * n or k < 0 or (n % 2 == 0 and k % 2 == 1):
        return -1
    
    # Initialize the matrix with zeroes
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix to be lexicographically maximal
    for i in range(n):
        for j in range(n):
            if i == j:  # Diagonal elements
                if k > 0:
                    matrix[i][j] = 1
                    k -= 1
            elif j > i:  # Upper triangle elements
                if k >= 2:
                    matrix[i][j] = 1
                    matrix[j][i] = 1
                    k -= 2
            
            if k <= 0:
                break
        if k <= 0:
            break
    
    # If there are still ones left to place, return -1
    if k > 0:
        return -1
    
    return matrix

# Read input
n, k = map(int, input().split())

# Create the matrix
result = create_symmetrical_matrix(n, k)

# Print the result
if result == -1:
    print(result)
else:
    for row in result:
        print(' '.join(map(str, row)))