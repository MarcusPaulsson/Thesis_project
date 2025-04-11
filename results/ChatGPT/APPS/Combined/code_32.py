def is_valid_journey(n, journey):
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
        # East and West do not affect the North/South position
        elif direction in {"East", "West"}:
            continue
        
        # Check if the current position is out of bounds
        if current_position < 0 or current_position > 20000:
            return "NO"
    
    return "YES" if current_position == 0 else "NO"