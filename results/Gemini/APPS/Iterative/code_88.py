def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def can_place(row, col, val):
        return counts.get(val, 0) > 0
    
    def place(row, col, val):
        matrix[row][col] = val
        counts[val] -= 1
        
    def unplace(row, col, val):
        matrix[row][col] = 0
        counts[val] += 1
    
    def solve_recursive(row, col):
        if row == n:
            print("YES")
            for r in matrix:
                print(*r)
            return True
        
        if col == n:
            return solve_recursive(row + 1, 0)
        
        if matrix[row][col] != 0:
            return solve_recursive(row, col + 1)
        
        for val in sorted(counts.keys()):
            if can_place(row, col, val):
                place(row, col, val)
                place(n - 1 - row, col, val)
                place(row, n - 1 - col, val)
                place(n - 1 - row, n - 1 - col, val)
                
                if solve_recursive(row, col + 1):
                    return True
                
                unplace(row, col, val)
                unplace(n - 1 - row, col, val)
                unplace(row, n - 1 - col, val)
                unplace(n - 1 - row, n - 1 - col, val)
        
        return False
    
    if solve_recursive(0, 0):
        return
    else:
        print("NO")

solve()