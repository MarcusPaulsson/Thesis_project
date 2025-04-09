def solve():
    n = int(input())
    s = input()

    def check(coloring):
        temp_s = list(s)
        
        for _ in range(n * (n - 1) // 2):
            swapped = False
            for i in range(n - 1):
                if temp_s[i] > temp_s[i+1] and coloring[i] != coloring[i+1]:
                    temp_s[i], temp_s[i+1] = temp_s[i+1], temp_s[i]
                    swapped = True
            if not swapped:
                break
        return "".join(temp_s) == "".join(sorted(s))
    
    def find_coloring(num_colors):
        for i in range(num_colors**n):
            coloring = []
            temp = i
            for _ in range(n):
                coloring.append(temp % num_colors + 1)
                temp //= num_colors
            
            if check(coloring):
                return coloring
        return None

    for num_colors in range(1, n + 1):
        coloring = find_coloring(num_colors)
        if coloring:
            print(num_colors)
            print(*coloring)
            return

solve()