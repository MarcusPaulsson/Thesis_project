def create_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    matrix = [[0] * n for _ in range(n)]
    
    # Check for the number of odd occurrences
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    # For odd n, we can have one center element, for even n, we can't have any
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO"
    
    # Fill the matrix
    half_n = (n + 1) // 2
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
                matrix[idx][idx] = num
                matrix[idx][n - 1 - idx] = num
                freq -= 2
            else:
                # Place in the center if odd
                if n % 2 == 1 and idx == half_n - 1 and freq == 1:
                    matrix[half_n - 1][half_n - 1] = num
                    freq -= 1
                else:
                    break
            if freq == 0:
                break
            if idx < half_n - 1:
                idx += 1
            else:
                idx = 0
    
    # Fill the remaining cells
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[n - 1 - i][j]
    
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