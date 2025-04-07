def check_journey(n, journey):
    position = 0  # North Pole is 0, South Pole is 20000
    for t, direction in journey:
        # Check for valid moves from the poles
        if position == 0 and direction != "South":
            return "NO"
        if position == 20000 and direction != "North":
            return "NO"
        
        # Update position based on direction
        if direction == "South":
            position += t
        elif direction == "North":
            position -= t
        # West and East do not affect the North/South position

        # Check if the position goes out of bounds
        if position < 0 or position > 20000:
            return "NO"
    
    # Check if we are back at the North Pole
    return "YES" if position == 0 else "NO"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Output result
print(check_journey(n, journey))