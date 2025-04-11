def is_valid_flag(n, m, field):
    # Check if the number of rows is divisible by 3
    if n % 3 != 0:
        return "NO"
    
    stripe_height = n // 3
    colors = set()
    
    # Check horizontal stripes
    for i in range(3):
        stripe = field[i * stripe_height:(i + 1) * stripe_height]
        first_row = stripe[0]
        
        # Check if all rows in the stripe are the same
        if any(row != first_row for row in stripe):
            return "NO"
        
        # Check if all characters in the stripe are the same
        if len(set(first_row)) != 1:
            return "NO"
        
        colors.add(first_row[0])
    
    # Check if we have exactly 3 different colors
    if len(colors) != 3:
        return "NO"
    
    return "YES"

# Input reading
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output the result
print(is_valid_flag(n, m, field))