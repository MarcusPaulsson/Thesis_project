def is_palindromic_possible(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    
    # Check odd frequency count
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)
    
    # Validate the possibility of forming a palindromic matrix
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO", []
    
    # Create the matrix
    matrix = [[0] * n for _ in range(n)]
    half = n // 2
    idx = 0
    
    # Fill the matrix
    for num, freq in count.items():
        while freq > 0:
            if freq >= 4:
                # Place in corners
                matrix[idx][idx] = num
                matrix[idx][n - 1 - idx] = num
                matrix[n - 1 - idx][idx] = num
                matrix[n - 1 - idx][n - 1 - idx] = num
                freq -= 4
            elif freq == 2:
                # Place in middle sides if even size
                if n % 2 == 0:
                    matrix[idx][half] = num
                    matrix[half][idx] = num
                    matrix[n - 1 - idx][half] = num
                    matrix[half][n - 1 - idx] = num
                freq -= 2
            elif freq == 1:
                # Place in center if odd size
                if n % 2 == 1 and odd_count == 1:
                    matrix[half][half] = num
                freq -= 1
            
            if freq == 0:
                idx += 1
                if idx >= half:
                    idx = half if n % 2 == 1 else half - 1
    
    # Fill remaining spots
    last_num = num
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = last_num
    
    return "YES", matrix

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Get result
result, matrix = is_palindromic_possible(n, numbers)

# Print output
print(result)
if result == "YES":
    for row in matrix:
        print(" ".join(map(str, row)))