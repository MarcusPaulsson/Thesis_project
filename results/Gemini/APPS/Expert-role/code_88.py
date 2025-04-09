def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def can_place(row, col):
        return row >= 0 and row < n and col >= 0 and col < n and matrix[row][col] == 0
    
    def find_number_with_count(count):
        for num, cnt in counts.items():
            if cnt >= count:
                return num
        return None
    
    for i in range((n + 1) // 2):
        for j in range((n + 1) // 2):
            if matrix[i][j] == 0:
                required_count = 1
                if i != n - 1 - i:
                    required_count += 1
                if j != n - 1 - j:
                    required_count += 1
                if i != n - 1 - i and j != n - 1 - j:
                    required_count += 1
                    
                num = find_number_with_count(required_count)
                if num is None:
                    print("NO")
                    return
                
                matrix[i][j] = num
                counts[num] -= 1
                if counts[num] == 0:
                    del counts[num]
                
                if i != n - 1 - i:
                    matrix[n - 1 - i][j] = num
                    counts[num] -= 1
                    if counts[num] == 0:
                        del counts[num]
                
                if j != n - 1 - j:
                    matrix[i][n - 1 - j] = num
                    counts[num] -= 1
                    if counts[num] == 0:
                        del counts[num]
                
                if i != n - 1 - i and j != n - 1 - j:
                    matrix[n - 1 - i][n - 1 - j] = num
                    counts[num] -= 1
                    if counts[num] == 0:
                        del counts[num]
    
    print("YES")
    for row in matrix:
        print(*row)
        
solve()