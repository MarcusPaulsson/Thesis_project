def is_palindromic_matrix_possible(n, nums):
    from collections import Counter

    count = Counter(nums)
    
    # Check for the number of odd-count elements
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    # For even n, we should have no odd-count elements
    # For odd n, we can have at most one odd-count element
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return False
    
    return True

def construct_palindromic_matrix(n, nums):
    from collections import Counter

    count = Counter(nums)
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the center of the matrix for odd n if needed
    if n % 2 == 1:
        for num, c in count.items():
            if c % 2 == 1:
                matrix[n // 2][n // 2] = num
                count[num] -= 1
                break

    # Fill the remaining positions
    pairs = []
    for num, c in count.items():
        for _ in range(c // 2):
            pairs.append(num)
    
    # Flatten pairs into coordinates
    pairs = pairs * 4  # Because we will need to place them in 4 quadrants
    
    idx = 0
    for i in range((n + 1) // 2):
        for j in range((n + 1) // 2):
            if idx < len(pairs):
                matrix[i][j] = pairs[idx]
                matrix[i][n - j - 1] = pairs[idx]
                matrix[n - i - 1][j] = pairs[idx]
                matrix[n - i - 1][n - j - 1] = pairs[idx]
                idx += 1
    
    return matrix

n = int(input())
nums = list(map(int, input().split()))

if not is_palindromic_matrix_possible(n, nums):
    print("NO")
else:
    print("YES")
    matrix = construct_palindromic_matrix(n, nums)
    for row in matrix:
        print(" ".join(map(str, row)))