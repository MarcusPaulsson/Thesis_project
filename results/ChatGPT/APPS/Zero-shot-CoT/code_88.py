def create_palindromic_matrix(n, elements):
    from collections import Counter

    count = Counter(elements)
    odd_count = sum(1 for v in count.values() if v % 2 != 0)

    # Check if it's possible to create a palindromic matrix
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO"

    # Preparing the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix with the elements
    half = n // 2
    center = (n - 1) // 2
    sorted_elements = sorted(count.items(), key=lambda x: -x[1])
    
    for value, freq in sorted_elements:
        while freq > 0:
            if n % 2 == 1 and freq >= 1 and odd_count == 1:
                matrix[center][center] = value
                freq -= 1
                odd_count -= 1
                continue

            # Fill the quadrants
            for i in range(half + 1):
                for j in range(half + 1):
                    if freq > 0:
                        if matrix[i][j] == 0:
                            matrix[i][j] = value
                            matrix[i][n - 1 - j] = value
                            matrix[n - 1 - i][j] = value
                            matrix[n - 1 - i][n - 1 - j] = value
                            freq -= 4
                            if freq < 0:
                                return "NO"
    
    return "YES", matrix

# Input handling
n = int(input().strip())
elements = list(map(int, input().strip().split()))

result = create_palindromic_matrix(n, elements)

if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))