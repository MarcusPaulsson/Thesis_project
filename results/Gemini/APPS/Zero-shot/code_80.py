def solve():
    n = int(input())
    s = input()
    
    def check(colors):
        colored_string = [(s[i], colors[i]) for i in range(n)]
        
        def can_sort(arr):
            arr = arr[:]
            for i in range(n):
                for j in range(n - i - 1):
                    if arr[j][0] > arr[j+1][0] and arr[j][1] != arr[j+1][1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            
            sorted_chars = [arr[i][0] for i in range(n)]
            return sorted_chars == sorted(s)
        
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