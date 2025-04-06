def is_valid_journey(n, journey):
    position = 0  # Position starts at the North Pole (0 km from North Pole)
    
    for t, direction in journey:
        if position == 0 and direction != "South":
            return "NO"  # Limak can only move South from the North Pole
        if position == 20000 and direction != "North":
            return "NO"  # Limak can only move North from the South Pole
        
        if direction == "South":
            position += t
        elif direction == "North":
            position -= t
        elif direction == "West" or direction == "East":
            pass  # These directions don't change the position
        
        if position < 0 or position > 20000:
            return "NO"  # Invalid position
    
    if position != 0:
        return "NO"  # Must end at the North Pole
    
    return "YES"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), direction) for t, direction in journey]

# Output the result
print(is_valid_journey(n, journey))