def solve():
    n = int(input())
    s = input()
    
    def check(num_colors):
        colors = [0] * n
        
        for i in range(n):
            colors[i] = 0
            
        def is_sortable(coloring):
            temp_s = list(s)
            
            swaps_made = True
            while swaps_made:
                swaps_made = False
                for i in range(n - 1):
                    if temp_s[i] > temp_s[i+1] and coloring[i] != coloring[i+1]:
                        temp_s[i], temp_s[i+1] = temp_s[i+1], temp_s[i]
                        swaps_made = True
            
            return "".join(temp_s) == "".join(sorted(s))
        
        
        def find_coloring(num_colors):
            colors = [0] * n
            
            def backtrack(index):
                if index == n:
                    if is_sortable(colors):
                        return True
                    else:
                        return False

                for color in range(1, num_colors + 1):
                    colors[index] = color
                    if backtrack(index + 1):
                        return True
                    colors[index] = 0 
                return False
            
            if backtrack(0):
                return colors
            else:
                return None
            
        coloring = find_coloring(num_colors)
        
        if coloring:
            return True, coloring
        else:
            return False, None
    
    for num_colors in range(1, n + 1):
        sortable, coloring = check(num_colors)
        if sortable:
            print(num_colors)
            print(*coloring)
            return

solve()