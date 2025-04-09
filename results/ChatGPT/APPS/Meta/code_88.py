def is_palindromic_matrix_possible(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    
    # Check the conditions for creating a palindromic matrix
    odd_count = 0
    for freq in count.values():
        if freq % 2 != 0:
            odd_count += 1
            
    # If n is odd, we can have one number with an odd count in the center
    if n % 2 == 0 and odd_count > 0:
        return "NO"
    # If n is odd, we can have at most one number with an odd count
    if n % 2 == 1 and odd_count > 1:
        return "NO"
    
    # Create the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix
    num_list = []
    for num, freq in count.items():
        num_list.extend([num] * freq)
    
    # Place numbers in the matrix
    idx = 0
    for i in range((n + 1) // 2):
        for j in range((n + 1) // 2):
            if idx < len(num_list):
                matrix[i][j] = num_list[idx]
                matrix[i][n - j - 1] = num_list[idx]
                matrix[n - i - 1][j] = num_list[idx]
                matrix[n - i - 1][n - j - 1] = num_list[idx]
                idx += 1
    
    return "YES", matrix

n = int(input())
numbers = list(map(int, input().split()))

result = is_palindromic_matrix_possible(n, numbers)

if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))