def create_palindromic_matrix(n, values):
    from collections import Counter

    count = Counter(values)
    odd_count = sum(1 for v in count.values() if v % 2 != 0)

    if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
        return "NO"

    matrix = [[0] * n for _ in range(n)]
    half = []

    for value, cnt in count.items():
        half.extend([value] * (cnt // 2))

    if n % 2 == 1:
        center = [value for value, cnt in count.items() if cnt % 2 == 1]
        if center:
            center_value = center[0]
        else:
            center_value = None
    else:
        center_value = None

    if center_value is not None:
        middle_row = n // 2
        matrix[middle_row][middle_row] = center_value
    
    half_size = len(half)
    for i in range(half_size // 2):
        r = i // (n // 2)
        c = i % (n // 2)
        value = half[i]
        matrix[r][c] = value
        matrix[r][n - c - 1] = value
        matrix[n - r - 1][c] = value
        matrix[n - r - 1][n - c - 1] = value

    return "YES", matrix

n = int(input())
values = list(map(int, input().split()))

result = create_palindromic_matrix(n, values)
if result == "NO":
    print(result)
else:
    print(result[0])
    for row in result[1]:
        print(" ".join(map(str, row)))