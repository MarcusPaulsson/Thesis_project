def solve():
    n = int(input())
    s = input()
    
    colors = [0] * n
    
    def check(num_colors):
        
        def possible(coloring):
            temp_s = list(s)
            
            for _ in range(n * (n - 1) // 2):
                swapped = False
                for i in range(n - 1):
                    if temp_s[i] > temp_s[i+1] and coloring[i] != coloring[i+1]:
                        temp_s[i], temp_s[i+1] = temp_s[i+1], temp_s[i]
                        swapped = True
                if not swapped:
                    break
            
            return "".join(temp_s) == "".join(sorted(s))

        
        
        import itertools
        
        for coloring in itertools.product(range(1, num_colors + 1), repeat=n):
            if possible(coloring):
                return True, list(coloring)
        
        return False, None
    
    for num_colors in range(1, n + 1):
        possible, coloring = check(num_colors)
        if possible:
            print(num_colors)
            print(*coloring)
            return

solve()