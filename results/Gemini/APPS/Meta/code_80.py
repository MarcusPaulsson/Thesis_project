def solve():
    n = int(input())
    s = input()
    
    def check(num_colors, coloring):
        colored_chars = [[] for _ in range(num_colors)]
        for i in range(n):
            colored_chars[coloring[i] - 1].append(s[i])
        
        colored_chars = [''.join(sorted(chars)) for chars in colored_chars]
        
        merged_string = ""
        for chars in colored_chars:
            merged_string += chars
        
        if "".join(sorted(s)) == merged_string:
            return True
        else:
            return False

    for num_colors in range(1, n + 1):
        
        import itertools
        
        for coloring in itertools.product(range(1, num_colors + 1), repeat=n):
            
            if check(num_colors, list(coloring)):
                print(num_colors)
                print(*list(coloring))
                return

solve()