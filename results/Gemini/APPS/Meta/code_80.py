def solve():
    n = int(input())
    s = input()
    
    def check(colors):
        colored_chars = []
        for i in range(n):
            colored_chars.append((s[i], colors[i]))
        
        def is_sortable(arr):
            arr = arr[:]
            for i in range(len(arr)):
                for j in range(len(arr) - 1):
                    if arr[j][0] > arr[j+1][0] and arr[j][1] != arr[j+1][1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            
            sorted_chars = sorted([char for char, _ in arr])
            current_chars = [char for char, _ in arr]
            return current_chars == sorted_chars
        
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