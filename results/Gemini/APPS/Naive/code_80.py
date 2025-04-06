def solve():
    n = int(input())
    s = input()
    
    def is_sortable(colors):
        colored_chars = []
        for i in range(n):
            colored_chars.append((s[i], colors[i]))
        
        def perform_swaps(arr):
            swaps = []
            for i in range(len(arr) - 1):
                if arr[i][0] > arr[i+1][0] and arr[i][1] != arr[i+1][1]:
                    swaps.append(i)
            return swaps

        
        arr = colored_chars[:]
        
        for _ in range(n * (n - 1) // 2):
          swaps = perform_swaps(arr)
          if not swaps:
            break
          
          for i in swaps:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        
        sorted_flag = True
        for i in range(len(arr) - 1):
            if arr[i][0] > arr[i+1][0]:
                sorted_flag = False
                break
        
        return sorted_flag
    
    for num_colors in range(1, n + 1):
        for colors in find_all_colorings(n, num_colors):
            if is_sortable(colors):
                print(num_colors)
                print(*colors)
                return

def find_all_colorings(n, num_colors):
    if n == 0:
        return [[]]
    
    all_colorings = []
    for color in range(1, num_colors + 1):
        for sub_coloring in find_all_colorings(n - 1, num_colors):
            all_colorings.append([color] + sub_coloring)
    
    return all_colorings

solve()