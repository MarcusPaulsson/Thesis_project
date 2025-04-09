def solve():
    n = int(input())
    s = input()
    
    colors = [0] * n
    
    def check(num_colors):
        
        def possible_to_sort(coloring):
            arr = list(s)
            
            for _ in range(n * (n - 1) // 2):
                swapped = False
                for i in range(n - 1):
                    if arr[i] > arr[i+1] and coloring[i] != coloring[i+1]:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        swapped = True
                if not swapped:
                    break

            return arr == sorted(list(s))

        
        import itertools
        
        for coloring in itertools.product(range(1, num_colors + 1), repeat=n):
            if possible_to_sort(list(coloring)):
                return True, list(coloring)
        return False, None
    
    for num_colors in range(1, n + 1):
        possible, coloring = check(num_colors)
        if possible:
            print(num_colors)
            print(*coloring)
            return

solve()