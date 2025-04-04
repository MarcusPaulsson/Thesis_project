def is_palindromic(matrix):
    return matrix == matrix[::-1] and [row[::-1] for row in matrix] == matrix

def construct_palindromic_matrix(n, numbers):
    if n % 2 == 1:
        middle = n // 2
        for i in range(n):
            if i != middle:
                if numbers[i] != numbers[n-1-i]:
                    return "NO"
            else:
                if numbers[i] != numbers[i]:
                    return "NO"
    else:
        if numbers[:n//2] != numbers[n//2:][::-1]:
            return "NO"
        if numbers[n//2:] != numbers[:n//2][::-1]:
            return "NO"
    
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i < n // 2:
                row.append(numbers[i * n + j])
            elif i == n // 2:
                if n % 2 == 1:
                    row.append(numbers[i * n + j])
                else:
                    row.append(numbers[i * n + j])
                    row.append(numbers[i * n + j])
            else:
                row.append(numbers[(n-1-i) * n + j])
        matrix.append(row)
    
    if is_palindromic(matrix):
        return "YES", matrix
    else:
        return "NO"

n = int(input())
numbers = list(map(int, input().split()))

result, matrix = construct_palindromic_matrix(n, numbers)
print(result)
if result == "YES":
    for row in matrix:
        print(" ".join(map(str, row)))