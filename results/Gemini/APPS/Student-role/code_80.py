def solve():
    n = int(input())
    s = input()
    
    colors = [0] * n
    
    def check(num_colors):
        for i in range(1 << n):
            coloring = []
            for j in range(n):
                if (i >> j) & 1:
                    coloring.append(1)
                else:
                    coloring.append(2)
                    
            if num_colors == 3:
                for k in range(n):
                    if colors[k] == 0:
                        colors[k] = 3
                        
            
            
            colored_chars = []
            for k in range(num_colors):
                colored_chars.append([])
            
            for idx in range(n):
                colored_chars[coloring[idx]-1].append(s[idx])

            
            def can_sort(arr, coloring):
                arr_list = list(s)
                
                swaps = []
                
                for _ in range(n * n):
                    swapped = False
                    for i in range(n - 1):
                        if arr_list[i] > arr_list[i + 1] and coloring[i] != coloring[i + 1]:
                            arr_list[i], arr_list[i + 1] = arr_list[i + 1], arr_list[i]
                            
                            
                            coloring[i], coloring[i + 1] = coloring[i + 1], coloring[i]
                            
                            
                            swapped = True
                
                    if not swapped:
                        break
                            
                return "".join(arr_list) == "".join(sorted(s))
            
            if can_sort(list(s), coloring.copy()):
                
                
                return True, coloring
        return False, None

    for num_colors in range(1, n + 1):
        result, coloring = check(num_colors)
        if result:
            print(num_colors)
            print(*coloring)
            return

solve()