def solve():
    n = int(input())
    s = input()
    
    def check(k):
        colors = [0] * n
        
        def backtrack(index):
            if index == n:
                return colors
            
            for color in range(1, k + 1):
                colors[index] = color
                
                # Check if valid so far
                valid = True
                for i in range(index):
                    if s[i] > s[index] and colors[i] == colors[index]:
                        valid = False
                        break
                
                if valid:
                    result = backtrack(index + 1)
                    if result:
                        return result
            
            colors[index] = 0  # Reset for backtracking
            return None
        
        return backtrack(0)
    
    for k in range(1, n + 1):
        coloring = check(k)
        if coloring:
            print(k)
            print(*coloring)
            return

solve()