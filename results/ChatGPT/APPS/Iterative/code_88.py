def create_palindromic_matrix(n, numbers):
    from collections import Counter
    
    # Count the occurrences of each number
    count = Counter(numbers)
    
    # Check the number of odd-count numbers
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    # For an n x n matrix:
    # - If n is odd, we can have at most 1 number with an odd count in the center
    # - If n is even, we cannot have any number with an odd count
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO"

    # Create the empty matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Prepare for filling the matrix
    half = n // 2
    center = n // 2

    # Fill the matrix with pairs
    num_list = []
    for num, cnt in count.items():
        num_list.extend([num] * cnt)
    
    # Fill the 4 quadrants
    idx = 0
    for i in range(half):
        for j in range(half):
            num = num_list[idx]
            matrix[i][j] = num
            matrix[i][n - j - 1] = num
            matrix[n - i - 1][j] = num
            matrix[n - i - 1][n - j - 1] = num
            idx += 1
    
    # If n is odd, fill the center
    if n % 2 == 1:
        for num, cnt in count.items():
            if cnt % 2 != 0:
                matrix[center][center] = num
                break
            
    return "YES", matrix

n = int(input())
numbers = list(map(int, input().split()))

result = create_palindromic_matrix(n, numbers)

if result == "NO":
    print("NO")
else:
    print("YES")
    for row in result[1]:
        print(' '.join(map(str, row)))