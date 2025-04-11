def is_valid_flag(n, m, field):
    colors = set()
    stripe_height = None
    current_color = None
    current_height = 0
    
    for i in range(n):
        row = field[i]
        if len(set(row)) != 1:
            return "NO"
        
        if current_color is None or row[0] != current_color:
            if current_color is not None:
                colors.add(current_color)
                if stripe_height is None:
                    stripe_height = current_height
                elif current_height != stripe_height:
                    return "NO"
            current_color = row[0]
            current_height = 1
        else:
            current_height += 1
    
    colors.add(current_color)
    
    if len(colors) == 3 and current_height == stripe_height:
        return "YES"
    return "NO"

n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]
print(is_valid_flag(n, m, field))