def solve():
    n = int(input())
    s = input()
    
    def check(colors):
        colored_string = [(s[i], colors[i]) for i in range(n)]
        
        def can_sort(arr):
            arr = arr[:]
            for _ in range(n):
                swapped = False
                for i in range(n - 1):
                    if arr[i][0] > arr[i+1][0] and arr[i][1] != arr[i+1][1]:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        swapped = True
                if not swapped:
                    break
            
            sorted_flag = True
            for i in range(n - 1):
                if arr[i][0] > arr[i+1][0]:
                    sorted_flag = False
                    break
            return sorted_flag
        
        return can_sort(colored_string)

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