def check_journey(n, journey):
    position = 0  # Position on the meridian, starting at the North Pole (0 km)
    
    for t, direction in journey:
        if position == 0 and direction != "South":
            return "NO"  # At North Pole, can only move South
        if position == 20000 and direction != "North":
            return "NO"  # At South Pole, can only move North
        
        if direction == "North":
            position -= t
        elif direction == "South":
            position += t
        elif direction == "East" or direction == "West":
            # East and West do not change the position on the meridian
            continue
        
        # Check if position goes out of bounds
        if position < 0 or position > 20000:
            return "NO"
    
    # Final position must be back at the North Pole
    if position != 0:
        return "NO"
    
    return "YES"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Output result
print(check_journey(n, journey))