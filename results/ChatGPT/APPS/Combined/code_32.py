def is_valid_journey(n, journey):
    current_position = 0  # Represents the distance from the North Pole (0 to 20000)
    
    for distance, direction in journey:
        if current_position == 0 and direction != "South":
            return "NO"  # Cannot move from North Pole except South
        if current_position == 20000 and direction != "North":
            return "NO"  # Cannot move from South Pole except North
        
        if direction == "South":
            current_position += distance
        elif direction == "North":
            current_position -= distance
        # Directions West and East do not affect the North-South position
        elif direction in ["West", "East"]:
            continue
        
        # Ensure we don't go past the poles
        if current_position < 0 or current_position > 20000:
            return "NO"
    
    # Journey must end at the North Pole
    return "YES" if current_position == 0 else "NO"

# Read input
n = int(input().strip())
journey = [tuple(input().strip().split()) for _ in range(n)]
journey = [(int(distance), direction) for distance, direction in journey]

# Output result
print(is_valid_journey(n, journey))