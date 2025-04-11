def can_form_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    
    # Check for the number of odd counts
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    # For an n x n matrix, we can have at most one odd count if n is odd
    # and no odd counts if n is even
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO", []
    
    # Create the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix
    half_n = (n + 1) // 2
    idx = 0
    for num, freq in count.items():
        for _ in range(freq // 2):
            matrix[idx // n][idx % n] = num
            matrix[n - 1 - (idx // n)][n - 1 - (idx % n)] = num
            idx += 1
    
    # Fill the center for odd n
    if n % 2 == 1:
        center = n // 2
        for num, freq in count.items():
            if freq % 2 == 1:
                matrix[center][center] = num
                break
    
    # Fill remaining cells for even n
    for i in range(half_n):
        for j in range(half_n):
            if matrix[i][j] == 0:
                for num, freq in count.items():
                    if freq > 0:
                        matrix[i][j] = num
                        matrix[i][n - 1 - j] = num
                        matrix[n - 1 - i][j] = num
                        matrix[n - 1 - i][n - 1 - j] = num
                        count[num] -= 4
                        break
    
    return "YES", matrix

n = int(input())
numbers = list(map(int, input().split()))

result, matrix = can_form_palindromic_matrix(n, numbers)

if result == "NO":
    print("NO")
else:
    print("YES")
    for row in matrix:
        print(" ".join(map(str, row)))