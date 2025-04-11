def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def can_place(row, col, val):
        return counts[val] > 0
    
    def place(row, col, val):
        matrix[row][col] = val
        counts[val] -= 1
        
    def unplace(row, col, val):
        matrix[row][col] = 0
        counts[val] += 1
        
    def solve_recursive(row, col):
        if row == n:
            print("YES")
            for r in range(n):
                print(*matrix[r])
            return True
        
        if col == n:
            return solve_recursive(row + 1, 0)
        
        if matrix[row][col] != 0:
            return solve_recursive(row, col + 1)
        
        for val in sorted(counts.keys()):
            if can_place(row, col, val):
                place(row, col, val)
                
                row_sym = n - 1 - row
                col_sym = n - 1 - col
                
                if row == row_sym and col == col_sym:
                    if solve_recursive(row, col + 1):
                        return True
                elif row == row_sym:
                    if can_place(row, col_sym, val):
                        place(row, col_sym, val)
                        if solve_recursive(row, col + 1):
                            return True
                        unplace(row, col_sym, val)
                elif col == col_sym:
                    if can_place(row_sym, col, val):
                        place(row_sym, col, val)
                        if solve_recursive(row, col + 1):
                            return True
                        unplace(row_sym, col, val)
                else:
                    if can_place(row_sym, col, val) and can_place(row, col_sym, val) and can_place(row_sym, col_sym, val):
                        place(row_sym, col, val)
                        place(row, col_sym, val)
                        place(row_sym, col_sym, val)
                        if solve_recursive(row, col + 1):
                            return True
                        unplace(row_sym, col_sym, val)
                        unplace(row, col_sym, val)
                        unplace(row_sym, col, val)
                
                unplace(row, col, val)
                
        return False
    
    total_cells = n * n
    counts_needed = {k: 0 for k in counts}
    
    for row in range(n):
        for col in range(n):
            row_sym = n - 1 - row
            col_sym = n - 1 - col
            
            if row == row_sym and col == col_sym:
                counts_needed[0] = counts_needed.get(0,0) + 1
            elif row == row_sym or col == col_sym:
                counts_needed[1] = counts_needed.get(1,0) + 1
            else:
                counts_needed[3] = counts_needed.get(3,0) + 1
    
    single_count = 0
    double_count = 0
    quad_count = 0
    
    for row in range(n):
        for col in range(n):
            row_sym = n - 1 - row
            col_sym = n - 1 - col
            
            if row == row_sym and col == col_sym:
                single_count += 1
            elif row == row_sym and col != col_sym or row != row_sym and col == col_sym:
                double_count += 1
            elif row != row_sym and col != col_sym:
                quad_count += 1
    
    single_count = single_count
    double_count = double_count // 2
    quad_count = quad_count // 4
    
    single_needed = 0
    double_needed = 0
    quad_needed = 0
    
    if n % 2 == 1:
        single_needed = 1
        double_needed = 2 * (n // 2)
        quad_needed = (n // 2) * (n // 2)
    else:
        quad_needed = (n // 2) * (n // 2)
    
    single_available = 0
    double_available = 0
    quad_available = 0
    
    for k, v in counts.items():
        if v >= 4:
            quad_available += v // 4
            counts[k] %= 4
        if v >= 2:
            double_available += v // 2
            counts[k] %= 2
        if v >= 1:
            single_available += v
    
    
    if n % 2 == 1:
        single_needed = 1
        double_needed = n - 1
        quad_needed = (n * n - (n - 1) - 1) // 4
    else:
        quad_needed = (n * n) // 4
        
    
    single_available = 0
    double_available = 0
    quad_available = 0
    
    for k, v in counts.items():
        quad_available += v // 4
        v %= 4
        double_available += v // 2
        v %= 2
        single_available += v
    
    
    if quad_available < quad_needed:
        print("NO")
        return
    
    quad_available -= quad_needed
    
    if n % 2 == 1:
        if double_available + quad_available * 2 < double_needed:
            print("NO")
            return
        
        temp = min(double_available, double_needed)
        double_available -= temp
        double_needed -= temp
        
        if double_needed > 0:
            single_available += double_needed
        
        if single_available < single_needed:
            print("NO")
            return
    
    if not solve_recursive(0, 0):
        print("NO")

solve()