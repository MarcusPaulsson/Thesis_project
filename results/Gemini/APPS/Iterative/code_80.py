def solve():
    n = int(input())
    s = input()
    
    def check(num_colors):
        colors = [0] * n
        
        def solve_recursive(index, current_colors):
            if index == n:
                return current_colors
            
            for color in range(1, num_colors + 1):
                new_colors = current_colors[:]
                new_colors[index] = color
                
                
                groups = [[] for _ in range(num_colors + 1)]
                for i in range(n):
                    groups[new_colors[i]].append(s[i])
                
                
                sorted_groups = []
                for i in range(1, num_colors+1):
                    sorted_groups.extend(sorted(groups[i]))
                
                
                is_sortable = True
                sorted_s = sorted(list(s))
                
                if sorted_groups != sorted_s:
                    is_sortable = False
                
                if is_sortable:
                    return new_colors
            
            return None
        
        result = solve_recursive(0, [0] * n)
        if result:
            return result
        else:
            return None
    
    for num_colors in range(1, n + 1):
        coloring = check(num_colors)
        if coloring:
            print(num_colors)
            print(*coloring)
            return

solve()