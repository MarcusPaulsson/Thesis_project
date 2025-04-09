def solve():
    n = int(input())
    s = input()
    
    def check(num_colors):
        coloring = [0] * n
        
        def is_sortable(coloring):
            temp_s = list(s)
            
            swaps = True
            while swaps:
                swaps = False
                for i in range(n - 1):
                    if temp_s[i] > temp_s[i+1] and coloring[i] != coloring[i+1]:
                        temp_s[i], temp_s[i+1] = temp_s[i+1], temp_s[i]
                        swaps = True
            
            return "".join(temp_s) == "".join(sorted(s))
        
        
        def find_coloring():
            import itertools
            for coloring_tuple in itertools.product(range(1, num_colors + 1), repeat=n):
                coloring = list(coloring_tuple)
                if is_sortable(coloring):
                    return coloring
            return None
        
        coloring = find_coloring()
        if coloring:
            return True, coloring
        else:
            return False, None
            
    
    for num_colors in range(1, n + 1):
        possible, coloring = check(num_colors)
        if possible:
            print(num_colors)
            print(*coloring)
            return

solve()