def solve():
    n = int(input())
    s = input()
    
    def check(colors):
        colored_string = [(s[i], colors[i]) for i in range(n)]
        
        def can_sort(arr):
            arr = arr[:]
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(arr) - 1):
                    if arr[i][0] > arr[i+1][0] and arr[i][1] != arr[i+1][1]:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        swapped = True
            
            sorted_chars = [x[0] for x in arr]
            return sorted_chars == sorted(s)
        
        return can_sort(colored_string)

    for num_colors in range(1, n + 1):
        for first_color in range(1, num_colors + 1):
            import itertools
            for colors in itertools.product(range(1, num_colors + 1), repeat=n):
                if check(colors):
                    print(num_colors)
                    print(*colors)
                    return

solve()