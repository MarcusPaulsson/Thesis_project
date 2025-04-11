def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def can_place(r, c, val):
        if counts[val] == 0:
            return False
        return True
    
    def place(r, c, val):
        matrix[r][c] = val
        counts[val] -= 1
        
    def unplace(r, c, val):
        matrix[r][c] = 0
        counts[val] += 1
    
    def is_valid():
      for i in range(n):
        for j in range(n):
          if matrix[i][j] != matrix[n-1-i][j] or matrix[i][j] != matrix[i][n-1-j]:
            return False
      return True
    
    def solve_recursive(r, c):
        if r == n:
            if is_valid():
              return True
            else:
              return False
        
        if c == n:
            return solve_recursive(r + 1, 0)
        
        if matrix[r][c] != 0:
            return solve_recursive(r, c + 1)
        
        for val in sorted(counts.keys()):
            if can_place(r, c, val):
                place(r, c, val)
                place(n - 1 - r, c, val)
                place(r, n - 1 - c, val)
                place(n - 1 - r, n - 1 - c, val)
                
                if solve_recursive(r, c + 1):
                    return True
                
                unplace(r, c, val)
                unplace(n - 1 - r, c, val)
                unplace(r, n - 1 - c, val)
                unplace(n - 1 - r, n - 1 - c, val)
        
        return False
    
    if solve_recursive(0, 0):
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()