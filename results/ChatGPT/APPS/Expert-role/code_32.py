def is_valid_journey(n, journey):
    position = 0  # Start at the North Pole (0 km from North Pole)
    
    for t, direction in journey:
        if position == 0 and direction != "South":
            return "NO"
        if position == 20000 and direction != "North":
            return "NO"
        
        if direction == "South":
            position += t
        elif direction == "North":
            position -= t
        elif direction == "West" or direction == "East":
            # Moving West or East does not change the position in km from North/South Pole
            continue
        
        if position < 0 or position > 20000:
            return "NO"
    
    if position != 0:
        return "NO"
    
    return "YES"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Output the result
print(is_valid_journey(n, journey))