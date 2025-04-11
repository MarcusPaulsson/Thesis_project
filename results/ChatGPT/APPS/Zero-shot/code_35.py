def is_valid_flag(n, m, field):
    colors = set()
    stripes = []
    
    # Check for horizontal stripes
    current_color = field[0][0]
    current_height = 0
    
    for i in range(n):
        if field[i][0] != current_color:
            if current_color in colors:
                return "NO"
            colors.add(current_color)
            stripes.append((current_color, current_height))
            current_color = field[i][0]
            current_height = 1
        else:
            current_height += 1
            
    # Add the last stripe
    if current_color in colors:
        return "NO"
    colors.add(current_color)
    stripes.append((current_color, current_height))
    
    if len(colors) != 3 or len(stripes) != 3:
        return "NO"
    
    # Check if all stripes have the same width
    for color, height in stripes:
        if height * m != n:
            return "NO"
    
    return "YES"

# Input reading
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output result
print(is_valid_flag(n, m, field))