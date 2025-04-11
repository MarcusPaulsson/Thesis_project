def solve():
    n = int(input())
    s = input()
    
    colors = [0] * n
    
    def check(num_colors):
        coloring = [0] * n
        
        def is_sortable(coloring):
            arr = list(s)
            
            swapped = True
            while swapped:
                swapped = False
                for i in range(n - 1):
                    if arr[i] > arr[i+1] and coloring[i] != coloring[i+1]:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        swapped = True
            
            return "".join(arr) == "".join(sorted(s))
        
        
        def find_coloring(index):
            if index == n:
                if is_sortable(coloring):
                    return True
                else:
                    return False
            
            for color in range(1, num_colors + 1):
                coloring[index] = color
                if find_coloring(index + 1):
                    return True
                coloring[index] = 0
            
            return False

        if find_coloring(0):
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