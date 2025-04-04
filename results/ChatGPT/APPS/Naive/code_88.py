def can_form_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    # For odd n, we can have at most one odd count of elements
    if n % 2 == 1 and odd_count > 1:
        return False
    
    # For even n, we cannot have any odd count of elements
    if n % 2 == 0 and odd_count > 0:
        return False
    
    return True

def fill_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix
    half_n = (n + 1) // 2  # This is the number of rows/columns we need to fill
    
    idx = 0
    for number, freq in count.items():
        while freq > 0:
            if freq >= 4:
                # Place in corners
                matrix[idx][idx] = number
                matrix[idx][n - idx - 1] = number
                matrix[n - idx - 1][idx] = number
                matrix[n - idx - 1][n - idx - 1] = number
                freq -= 4
            elif freq == 3:
                # Place in corners and center (only valid if n is odd)
                if n % 2 == 1:
                    matrix[idx][idx] = number
                    matrix[idx][n - idx - 1] = number
                    matrix[n - idx - 1][idx] = number
                    matrix[half_n - 1][half_n - 1] = number
                    freq -= 3
                else:
                    break  # Cannot place with 3 in even n
            elif freq == 2:
                # Place in one row and one column
                matrix[idx][idx] = number
                matrix[idx][n - idx - 1] = number
                freq -= 2
            elif freq == 1:
                # Place in the center if it's an odd n
                if n % 2 == 1:
                    matrix[half_n - 1][half_n - 1] = number
                    freq -= 1
                break
            else:
                break
        if freq > 0:
            return False
        idx += 1
        if idx == half_n:
            break

    # Fill remaining spots symmetrically
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[n - i - 1][j]
                matrix[i][n - j - 1] = matrix[n - i - 1][n - j - 1]

    return True, matrix

n = int(input().strip())
numbers = list(map(int, input().strip().split()))

if can_form_palindromic_matrix(n, numbers):
    success, matrix = fill_palindromic_matrix(n, numbers)
    if success:
        print("YES")
        for row in matrix:
            print(" ".join(map(str, row)))
    else:
        print("NO")
else:
    print("NO")