from collections import Counter

def is_palindromic_matrix_possible(n, numbers):
    count = Counter(numbers)
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)
    
    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return False
    
    return True

def construct_palindromic_matrix(n, numbers):
    count = Counter(numbers)
    matrix = [[0] * n for _ in range(n)]
    
    half_n = (n + 1) // 2
    idx = 0
    
    for num, freq in count.items():
        for _ in range(freq // 2):
            row, col = divmod(idx, n)
            matrix[row][col] = num
            matrix[n - 1 - row][n - 1 - col] = num
            idx += 1
            
    if n % 2 == 1:
        center = n // 2
        for num, freq in count.items():
            if freq % 2 == 1:
                matrix[center][center] = num
                break
    
    return matrix

def main():
    n = int(input().strip())
    numbers = list(map(int, input().strip().split()))
    
    if not is_palindromic_matrix_possible(n, numbers):
        print("NO")
        return
    
    matrix = construct_palindromic_matrix(n, numbers)
    
    print("YES")
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()