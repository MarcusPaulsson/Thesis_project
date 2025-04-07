def solve():
    n = int(input())
    s = input()
    
    def check(colors):
        arr = list(s)
        for _ in range(n):
            swapped = False
            for i in range(n - 1):
                if arr[i] > arr[i+1] and colors[i] != colors[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True
            if not swapped:
                break
        return "".join(arr) == "".join(sorted(s))

    for num_colors in range(1, n + 1):
        for i in range(num_colors**n):
            colors = []
            temp = i
            for _ in range(n):
                colors.append((temp % num_colors) + 1)
                temp //= num_colors
            
            if check(colors):
                print(num_colors)
                print(*colors)
                return
    
solve()