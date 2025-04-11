def create_palindromic_matrix(n, numbers):
    from collections import Counter
    
    # Count the frequency of each number
    count = Counter(numbers)
    
    # Check for the possibility of forming a palindromic matrix
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)
    if odd_count > 1:
        return "NO"
    
    # Prepare the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the half list with half of the frequencies
    half = []
    center_value = None
    for value, freq in count.items():
        half.extend([value] * (freq // 2))
        if freq % 2 != 0:
            center_value = value
    
    # Fill the matrix symmetrically
    index = 0
    for i in range(n):
        for j in range(n):
            if i < (n + 1) // 2:  # Fill only the top half and the center row if n is odd
                if j < (n + 1) // 2:  # Fill only the left half and the center column if n is odd
                    matrix[i][j] = half[index]
                    matrix[i][n - j - 1] = half[index]
                    matrix[n - i - 1][j] = half[index]
                    matrix[n - i - 1][n - j - 1] = half[index]
                    index += 1
                elif n % 2 == 1 and j == n // 2:  # Fill the center cell if n is odd
                    matrix[i][j] = center_value
                    matrix[n - i - 1][j] = center_value
    
    return "YES", matrix

# Input reading
n = int(input().strip())
numbers = list(map(int, input().strip().split()))

# Generate the result
result = create_palindromic_matrix(n, numbers)

# Output the result
if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))