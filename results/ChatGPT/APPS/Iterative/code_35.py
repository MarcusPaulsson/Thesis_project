def is_valid_flag(n, m, field):
    colors = set()
    stripe_height = None
    current_color = None
    current_height = 0

    for i in range(n):
        row = field[i]
        if len(set(row)) != 1 or row[0] not in {'R', 'G', 'B'}:
            return "NO"
        
        if current_color is None:
            current_color = row[0]
            current_height = 1
        elif row[0] == current_color:
            current_height += 1
        else:
            colors.add(current_color)
            if stripe_height is None:
                stripe_height = current_height
            elif current_height != stripe_height:
                return "NO"
            current_color = row[0]
            current_height = 1

    colors.add(current_color)
    if current_height != stripe_height:
        return "NO"

    return "YES" if len(colors) == 3 else "NO"

n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]
print(is_valid_flag(n, m, field))