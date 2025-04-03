def can_construct_palindromic_matrix(n, nums):
    from collections import Counter
    
    count = Counter(nums)
    matrix = [[0] * n for _ in range(n)]
    
    # Count how many of each number we have
    odd_count = 0
    center_value = None
    
    for value, cnt in count.items():
        if cnt % 4 != 0:
            if cnt % 4 == 2:
                odd_count += 1
            elif cnt % 4 == 1:
                odd_count += 1
                center_value = value
            odd_count += cnt // 4
        else:
            odd_count += cnt // 4
            
    if (n % 2 == 1 and odd_count > 1) or (n % 2 == 0 and odd_count > 0):
        return "NO"

    # Fill the matrix in a palindromic way
    i, j = 0, 0
    for value, cnt in count.items():
        while cnt > 0:
            if i < n // 2:
                matrix[i][j] = value
                matrix[n - 1 - i][j] = value
                matrix[i][n - 1 - j] = value
                matrix[n - 1 - i][n - 1 - j] = value
                cnt -= 4
                if j < n - 1:
                    j += 1
                else:
                    j = 0
                    i += 1
            else:
                if n % 2 == 1 and i == n // 2 and j == n // 2:
                    matrix[i][j] = center_value
                    cnt -= 1
                break

    return "YES", matrix

# Read input
n = int(input())
nums = list(map(int, input().split()))

result = can_construct_palindromic_matrix(n, nums)

if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))