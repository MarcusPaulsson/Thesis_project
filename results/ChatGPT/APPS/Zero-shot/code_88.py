def create_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    matrix = [[0] * n for _ in range(n)]
    
    # Check for the number of odd occurrences
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO"
    
    # Fill the matrix
    half = n // 2
    center = n // 2 if n % 2 == 1 else None
    
    # Fill corners and edges
    for num, freq in count.items():
        while freq > 0:
            if freq >= 4:
                # Place in corners
                matrix[0][0] = matrix[0][n-1] = matrix[n-1][0] = matrix[n-1][n-1] = num
                freq -= 4
            elif freq >= 2:
                # Place in edges
                if n % 2 == 0:
                    matrix[0][half] = matrix[n-1][half] = num
                    matrix[half][0] = matrix[half][n-1] = num
                else:
                    if center is not None:
                        matrix[center][center] = num
                freq -= 2
            else:
                # Place in the center if odd
                if center is not None and freq == 1:
                    matrix[center][center] = num
                    freq -= 1
                break
    
    # Fill remaining cells
    for i in range(half + 1):
        for j in range(half + 1):
            if matrix[i][j] == 0:
                for num, freq in count.items():
                    if freq > 0:
                        matrix[i][j] = num
                        matrix[i][n-1-j] = num
                        matrix[n-1-i][j] = num
                        matrix[n-1-i][n-1-j] = num
                        count[num] -= 4
                        break
    
    return "YES", matrix

n = int(input())
numbers = list(map(int, input().split()))

result = create_palindromic_matrix(n, numbers)

if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))