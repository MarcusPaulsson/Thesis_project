def solve():
    n = int(input())
    s = input()
    
    def check(k):
        colors = [0] * n
        
        def backtrack(index):
            if index == n:
                return True
            
            for color in range(1, k + 1):
                colors[index] = color
                
                temp_s = list(s)
                temp_colors = list(colors)
                
                swaps = True
                
                for i in range(n):
                    for j in range(n - 1):
                        if temp_s[j] > temp_s[j+1] and temp_colors[j] != temp_colors[j+1]:
                            temp_s[j], temp_s[j+1] = temp_s[j+1], temp_s[j]
                            temp_colors[j], temp_colors[j+1] = temp_colors[j+1], temp_colors[j]
                            
                if "".join(temp_s) == "".join(sorted(s)):
                    return True
                
            return False

    
    for k in range(1, n + 1):
        colors = [0] * n
        
        def can_sort(coloring):
            temp_s = list(s)
            
            for i in range(n):
                for j in range(n - 1):
                    if temp_s[j] > temp_s[j+1] and coloring[j] != coloring[j+1]:
                        temp_s[j], temp_s[j+1] = temp_s[j+1], temp_s[j]
            
            return "".join(temp_s) == "".join(sorted(s))

        
        
        
        
        import itertools
        
        for coloring in itertools.product(range(1, k + 1), repeat=n):
            if can_sort(coloring):
                print(k)
                print(*coloring)
                return

solve()