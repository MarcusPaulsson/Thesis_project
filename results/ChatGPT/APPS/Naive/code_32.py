def check_journey(n, journey):
    current_position = 0  # Position in kilometers from the North Pole (0 to 20000)

    for t, direction in journey:
        if current_position == 0 and direction != "South":
            return "NO"
        if current_position == 20000 and direction != "North":
            return "NO"

        if direction == "South":
            current_position += t
        elif direction == "North":
            current_position -= t
        elif direction == "West" or direction == "East":
            # West and East don't change the North-South position
            continue
        
        # Check if current position is going out of bounds
        if current_position < 0 or current_position > 20000:
            return "NO"
    
    # Final position must be at the North Pole
    if current_position != 0:
        return "NO"

    return "YES"

# Input reading
n = int(input().strip())
journey = [tuple(input().strip().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Output the result
print(check_journey(n, journey))