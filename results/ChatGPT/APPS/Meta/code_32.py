def is_valid_journey(n, journey):
    position = 0  # Position starts at the North Pole (0 km)
    
    for t, direction in journey:
        if position == 0 and direction != "South":
            return "NO"  # At North Pole, can only move South
        if position == 20000 and direction != "North":
            return "NO"  # At South Pole, can only move North
        
        if direction == "South":
            position += t
        elif direction == "North":
            position -= t
        elif direction == "West" or direction == "East":
            continue  # No change in position
        
        if position < 0 or position > 20000:
            return "NO"  # Out of bounds
        
    if position != 0:
        return "NO"  # Must end at North Pole
    
    return "YES"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Output result
print(is_valid_journey(n, journey))