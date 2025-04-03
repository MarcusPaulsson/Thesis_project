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
                    
            if num_colors == 1 and any(c == 2 for c in coloring):
                continue
            
            if num_colors == 1:
                coloring = [1] * n
                
            
            colored_chars = [[] for _ in range(num_colors + 1)]
            for k in range(n):
                colored_chars[coloring[k]].append(s[k])
                
            
            possible = True
            
            sorted_s = sorted(list(s))
            
            temp_s = list(s)
            
            
            
            
            
            
            
            
            
            def can_sort(arr, color_assignment):
                temp_arr = list(arr)
                n = len(arr)
                swapped = True
                while swapped:
                    swapped = False
                    for i in range(n - 1):
                        if arr[i] > arr[i+1] and color_assignment[i] != color_assignment[i+1]:
                            arr[i], arr[i+1] = arr[i+1], arr[i]
                            swapped = True
                return arr
            
            
            final_s = can_sort(list(s), coloring)
            
            
            if final_s == sorted(list(s)):
                return coloring
        return None
    
    for num_colors in range(1, n + 1):
        coloring = check(num_colors)
        if coloring:
            print(num_colors)
            print(*coloring)
            return
            

solve()