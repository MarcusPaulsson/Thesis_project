def solve():
    n = int(input())
    s = input()
    
    colors = [0] * n
    
    def check(num_colors):
        
        def is_valid_coloring(color_assignment):
            
            b = []
            for i in range(n):
                b.append((s[i], color_assignment[i]))
            
            
            def can_be_sorted(arr):
                arr_copy = arr[:]
                
                for _ in range(n * (n - 1) // 2):
                    swapped = False
                    for i in range(n - 1):
                        if arr_copy[i][0] > arr_copy[i+1][0] and arr_copy[i][1] != arr_copy[i+1][1]:
                            arr_copy[i], arr_copy[i+1] = arr_copy[i+1], arr_copy[i]
                            swapped = True
                    if not swapped:
                        break
                
                sorted_arr = sorted(arr, key=lambda x: x[0])
                
                
                chars_only_copy = [x[0] for x in arr_copy]
                chars_only_sorted = [x[0] for x in sorted_arr]
                
                return chars_only_copy == chars_only_sorted
            
            return can_be_sorted(b)
        
        import itertools
        
        for color_assignment in itertools.product(range(1, num_colors + 1), repeat=n):
            if is_valid_coloring(list(color_assignment)):
                return True, list(color_assignment)
        return False, None
    
    for num_colors in range(1, n + 1):
        possible, color_assignment = check(num_colors)
        if possible:
            print(num_colors)
            print(*color_assignment)
            return

solve()