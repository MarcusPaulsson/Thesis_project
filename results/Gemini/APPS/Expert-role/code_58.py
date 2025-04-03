def solve():
    n, m, k = map(int, input().split())
    
    dp = {}
    
    def calculate_cost(rows, cols, target_squares):
        if (rows, cols, target_squares) in dp:
            return dp[(rows, cols, target_squares)]
        
        if target_squares == 0:
            return 0
        
        if rows * cols == target_squares:
            return 0
            
        if rows * cols < target_squares:
            return float('inf')
        
        if rows == 0 or cols == 0:
            return float('inf')
            
        if target_squares < 0:
            return float('inf')

        min_cost = float('inf')
        
        # Horizontal cuts
        for i in range(1, rows):
            for j in range(target_squares + 1):
                cost = cols * cols + calculate_cost(i, cols, j) + calculate_cost(rows - i, cols, target_squares - j)
                min_cost = min(min_cost, cost)
        
        # Vertical cuts
        for i in range(1, cols):
            for j in range(target_squares + 1):
                cost = rows * rows + calculate_cost(rows, i, j) + calculate_cost(rows, cols - i, target_squares - j)
                min_cost = min(min_cost, cost)
        
        dp[(rows, cols, target_squares)] = min_cost
        return min_cost
    
    result = calculate_cost(n, m, k)
    print(result)

t = int(input())
for _ in range(t):
    solve()