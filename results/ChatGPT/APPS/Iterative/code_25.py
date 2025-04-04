def create_symmetric_matrix(n, k):
    if k > n * n or (n % 2 == 0 and k % 2 == 1) or (n % 2 == 1 and k > n * n - n):
        return -1

    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k <= 0:
            break
        for j in range(i, n):
            if k <= 0:
                break
            if i == j:  # Main diagonal
                if k > 0:
                    matrix[i][j] = 1
                    k -= 1
            else:  # Symmetric positions
                if k >= 2:
                    matrix[i][j] = 1
                    matrix[j][i] = 1
                    k -= 2

    return matrix if k == 0 else -1

def main():
    n, k = map(int, input("Enter values for n and k: ").split())
    result = create_symmetric_matrix(n, k)

    if result == -1:
        print(-1)
    else:
        for row in result:
            print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()