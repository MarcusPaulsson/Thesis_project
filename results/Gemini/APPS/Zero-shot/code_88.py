def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def can_place(r, c, val):
        if matrix[r][c] != 0:
            return False
        return True
    
    def place(r, c, val):
        matrix[r][c] = val
        matrix[n-1-r][c] = val
        matrix[r][n-1-c] = val
        matrix[n-1-r][n-1-c] = val
        counts[val] -= 4
        
    def unplace(r, c, val):
        matrix[r][c] = 0
        matrix[n-1-r][c] = 0
        matrix[r][n-1-c] = 0
        matrix[n-1-r][n-1-c] = 0
        counts[val] += 4

    def can_place_2(r, c, val):
        if matrix[r][c] != 0:
            return False
        return True
    
    def place_2(r, c, val):
        matrix[r][c] = val
        matrix[n-1-r][c] = val
        counts[val] -= 2
        
    def unplace_2(r, c, val):
        matrix[r][c] = 0
        matrix[n-1-r][c] = 0
        counts[val] += 2
        
    def can_place_2_2(r, c, val):
        if matrix[r][c] != 0:
            return False
        return True
    
    def place_2_2(r, c, val):
        matrix[r][c] = val
        matrix[r][n-1-c] = val
        counts[val] -= 2
        
    def unplace_2_2(r, c, val):
        matrix[r][c] = 0
        matrix[r][n-1-c] = 0
        counts[val] += 2

    def can_place_1(r, c, val):
        if matrix[r][c] != 0:
            return False
        return True
    
    def place_1(r, c, val):
        matrix[r][c] = val
        counts[val] -= 1
        
    def unplace_1(r, c, val):
        matrix[r][c] = 0
        counts[val] += 1

    def solve_recursive(r, c):
        if r == (n + 1) // 2:
            return True
        
        next_r = r
        next_c = c + 1
        if next_c == (n + 1) // 2:
            next_r = r + 1
            next_c = 0
            
        for val in sorted(counts.keys()):
            if counts[val] > 0:
                if r < n // 2 and c < n // 2:
                    if counts[val] >= 4 and can_place(r, c, val) :
                        place(r, c, val)
                        if solve_recursive(next_r, next_c):
                            return True
                        unplace(r, c, val)
                elif r < n // 2 and c == n // 2 and n % 2 != 0:
                    if counts[val] >= 2 and can_place_2(r, c, val):
                        place_2(r, c, val)
                        if solve_recursive(next_r, next_c):
                            return True
                        unplace_2(r, c, val)
                elif r == n // 2 and c < n // 2 and n % 2 != 0:
                    if counts[val] >= 2 and can_place_2_2(r, c, val):
                        place_2_2(r, c, val)
                        if solve_recursive(next_r, next_c):
                            return True
                        unplace_2_2(r, c, val)
                elif r == n // 2 and c == n // 2 and n % 2 != 0:
                     if counts[val] >= 1 and can_place_1(r, c, val):
                        place_1(r, c, val)
                        if solve_recursive(next_r, next_c):
                            return True
                        unplace_1(r, c, val)
        return False
    
    if solve_recursive(0, 0):
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()