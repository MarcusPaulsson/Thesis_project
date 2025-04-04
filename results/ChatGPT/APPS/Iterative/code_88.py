def is_possible(n, counts):
    # Check if the counts can form a palindromic matrix
    odd_count = sum(1 for count in counts if count % 2 != 0)
    return not ((n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1))

def fill_matrix(n, counts):
    # Create an empty n x n matrix
    matrix = [[0] * n for _ in range(n)]
    # Create a list of elements to place in the matrix
    elements = []
    
    for number, count in counts.items():
        elements.extend([number] * count)

    # Fill the matrix in a palindromic manner
    idx = 0
    for i in range((n + 1) // 2):
        for j in range((n + 1) // 2):
            if idx < len(elements):  # Prevent index out of range
                matrix[i][j] = elements[idx]
                matrix[i][n - j - 1] = elements[idx]
                matrix[n - i - 1][j] = elements[idx]
                matrix[n - i - 1][n - j - 1] = elements[idx]
                idx += 1

    return matrix

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    from collections import Counter
    counts = Counter(a)
    
    if not is_possible(n, counts.values()):
        print("NO")
        return
    
    matrix = fill_matrix(n, counts)
    print("YES")
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()