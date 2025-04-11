def solve():
    n = int(input())
    s = input()
    
    def check(colors):
        colored_chars = []
        for i in range(n):
            colored_chars.append((s[i], colors[i]))
        
        
        def is_sortable(arr):
            
            def swap(arr, i, j):
                arr[i], arr[j] = arr[j], arr[i]
            
            
            arr_copy = arr[:]
            
            for _ in range(n):
                swapped = False
                for i in range(n - 1):
                    if arr_copy[i][0] > arr_copy[i+1][0] and arr_copy[i][1] != arr_copy[i+1][1]:
                        swap(arr_copy, i, i+1)
                        swapped = True
                if not swapped:
                    break
            
            sorted_arr = sorted(arr)
            
            
            chars_only_copy = [x[0] for x in arr_copy]
            chars_only_sorted = [x[0] for x in sorted_arr]
            
            return chars_only_copy == chars_only_sorted
            
        return is_sortable(colored_chars)

    
    for num_colors in range(1, n + 1):
        for i in range(num_colors**n):
            colors = []
            temp = i
            for _ in range(n):
                colors.append(temp % num_colors + 1)
                temp //= num_colors
            
            if check(colors):
                print(num_colors)
                print(*colors)
                return

solve()