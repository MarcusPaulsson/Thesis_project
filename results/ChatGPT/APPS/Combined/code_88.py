def is_palindromic_matrix_possible(n, numbers):
    from collections import Counter

    # Count the frequency of each number
    count = Counter(numbers)

    # Check for the number of odd occurrences
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)

    # For a palindromic matrix:
    # - If n is even, all numbers must have even frequencies.
    # - If n is odd, at most one number can have an odd frequency.
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return False, None

    # Initialize the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix with numbers
    half_matrix = [[0] * (n // 2) for _ in range(n // 2)]
    middle_value = None

    # Fill half of the matrix with pairs
    index = 0
    for number, freq in count.items():
        while freq > 0:
            if freq % 2 == 1:
                middle_value = number  # Store the middle value for odd n
            half_matrix[index // (n // 2)][index % (n // 2)] = number
            freq -= 2
            index += 1

    # Fill the complete matrix by mirroring the half
    for i in range(n // 2):
        for j in range(n // 2):
            matrix[i][j] = half_matrix[i][j]
            matrix[i][n - j - 1] = half_matrix[i][j]
            matrix[n - i - 1][j] = half_matrix[i][j]
            matrix[n - i - 1][n - j - 1] = half_matrix[i][j]

    # Fill the middle row/column if n is odd
    if n % 2 == 1 and middle_value is not None:
        mid_index = n // 2
        for j in range(n):
            matrix[mid_index][j] = middle_value
            matrix[j][mid_index] = middle_value
            
    return True, matrix

# Input reading
n = int(input().strip())
numbers = list(map(int, input().strip().split()))

# Check if it's possible to create a palindromic matrix
possible, result = is_palindromic_matrix_possible(n, numbers)

if possible:
    print("YES")
    for row in result:
        print(" ".join(map(str, row)))
else:
    print("NO")