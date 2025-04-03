def solve():
    n = int(input())
    s = input()
    
    def check(colors):
        colored_string = ""
        color_arr = []
        for i in range(n):
            color_arr.append(0)
        
        for i in range(n):
            color_arr[i] = colors[i]
            colored_string += s[i]
        
        
        
        def can_sort(arr, colors):
            
            n = len(arr)
            
            
            
            def bubble_sort(arr, colors):
                
                
                swapped = True
                while swapped:
                    swapped = False
                    for i in range(n - 1):
                        if arr[i] > arr[i + 1] and colors[i] != colors[i + 1]:
                            arr[i], arr[i + 1] = arr[i + 1], arr[i]
                            colors[i], colors[i + 1] = colors[i + 1], colors[i]
                            swapped = True
                return arr
                
            sorted_arr = bubble_sort(list(arr), list(colors))

            return sorted_arr == sorted(arr)

        return can_sort(list(s), color_arr), color_arr
    
    for num_colors in range(1, n + 1):
        
        import itertools
        
        for colors_tuple in itertools.product(range(1,num_colors+1), repeat=n):
            colors = list(colors_tuple)
            can_be_sorted, color_arr = check(colors)
            
            if can_be_sorted:
                print(num_colors)
                print(*color_arr)
                return

solve()