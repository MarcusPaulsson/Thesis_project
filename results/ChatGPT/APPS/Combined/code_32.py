def is_valid_journey(n, journey):
    current_position = 0  # Position in kilometers from the North Pole (0 to 20000)

    for t, direction in journey:
        if current_position == 0 and direction != "South":
            return "NO"  # At North Pole, can only move South
        if current_position == 20000 and direction != "North":
            return "NO"  # At South Pole, can only move North
        
        if direction == "South":
            current_position += t
        elif direction == "North":
            current_position -= t
        # West and East do not affect the North/South position
        # No need to handle them explicitly as they don't change current_position
        
        # Check if the position goes out of bounds
        if current_position < 0 or current_position > 20000:
            return "NO"
    
    # Journey must end at the North Pole
    return "YES" if current_position == 0 else "NO"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), direction) for t, direction in journey]

# Output the result
print(is_valid_journey(n, journey))