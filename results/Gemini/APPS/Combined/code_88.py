def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def can_fill(row, col):
        return row < n // 2 or (row == n // 2 and n % 2 != 0) or col < n // 2 or (col == n // 2 and n % 2 != 0)

    def backtrack(row, col):
        if row == n:
            return True
        
        next_row = row
        next_col = col + 1
        if next_col == n:
            next_row += 1
            next_col = 0
        
        if matrix[row][col] != 0:
            return backtrack(next_row, next_col)
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                needed = 4
                if row == n - 1 - row and col == n - 1 - col:
                    needed = 1
                elif row == n - 1 - row or col == n - 1 - col:
                    needed = 2

                if can_fill(row, col):
                    if counts[num] >= needed:
                        counts[num] -= needed
                        matrix[row][col] = num
                        matrix[n-1-row][col] = num
                        matrix[row][n-1-col] = num
                        matrix[n-1-row][n-1-col] = num

                        if backtrack(next_row, next_col):
                            return True
                    
                        matrix[row][col] = 0
                        matrix[n-1-row][col] = 0
                        matrix[row][n-1-col] = 0
                        matrix[n-1-row][n-1-col] = 0
                        counts[num] += needed
                else:
                    if backtrack(next_row, next_col):
                        return True
        
        return False

    ones = 0
    twos = 0
    for num in counts:
        if counts[num] % 4 == 1:
            ones += 1
        elif counts[num] % 4 == 2:
            twos += 1
        elif counts[num] % 4 == 3:
            print("NO")
            return

    if n % 2 == 0:
        for num in counts:
            if counts[num] % 4 != 0:
                print("NO")
                return
    else:
        if ones > 1:
            print("NO")
            return
        
        center_found = False
        for i in range(len(matrix) // 2):
            for j in range(len(matrix) // 2):
                pass

    if backtrack(0, 0):
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()