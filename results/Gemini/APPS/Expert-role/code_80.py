def solve():
    n = int(input())
    s = input()
    
    def check(num_colors, coloring):
        colored_chars = [[] for _ in range(num_colors)]
        for i in range(n):
            colored_chars[coloring[i] - 1].append(s[i])
        
        combined_chars = []
        for i in range(num_colors):
            combined_chars.extend(colored_chars[i])
        
        if ''.join(sorted(s)) == ''.join(sorted(combined_chars)):
            return True
        else:
            return False

    for num_colors in range(1, n + 1):
        
        import itertools
        for coloring in itertools.product(range(1, num_colors + 1), repeat=n):
            
            if check(num_colors, list(coloring)):
                print(num_colors)
                print(*coloring)
                return

solve()