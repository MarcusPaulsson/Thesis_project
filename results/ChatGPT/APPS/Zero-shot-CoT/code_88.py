def can_form_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    
    # Check for the number of odd occurrences
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    # For an n x n matrix, we can have at most one odd count if n is odd
    # and no odd counts if n is even
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO"
    
    # Prepare the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix
    half = n // 2
    idx = 0
    for value, freq in count.items():
        while freq > 0:
            if freq >= 4:
                # Place in corners
                matrix[idx][idx] = value
                matrix[idx][n - 1 - idx] = value
                matrix[n - 1 - idx][idx] = value
                matrix[n - 1 - idx][n - 1 - idx] = value
                freq -= 4
            elif freq >= 2:
                # Place in sides
                if idx < half:
                    matrix[idx][n - 1 - idx] = value
                    matrix[n - 1 - idx][idx] = value
                    freq -= 2
                else:
                    # If we reach the middle row/column in odd n
                    if n % 2 == 1 and idx == half:
                        matrix[idx][idx] = value
                        freq -= 1
            else:
                break
            idx = (idx + 1) % half
    
    # Fill the center for odd n
    if n % 2 == 1:
        for value, freq in count.items():
            if freq % 2 == 1:
                matrix[half][half] = value
                break
    
    return "YES", matrix

n = int(input())
numbers = list(map(int, input().split()))

result = can_form_palindromic_matrix(n, numbers)

if result == "NO":
    print("NO")
else:
    print("YES")
    for row in result[1]:
        print(" ".join(map(str, row)))