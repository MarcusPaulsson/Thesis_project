def is_valid_journey(n, journey):
    position = 0  # Position on the meridian, starting at North Pole (0 km)
    MAX_POSITION = 20000  # South Pole position

    for t, direction in journey:
        # Validate movement from North and South Poles
        if position == 0 and direction != "South":
            return "NO"  # At North Pole, can only move South
        if position == MAX_POSITION and direction != "North":
            return "NO"  # At South Pole, can only move North

        # Update position based on direction
        if direction == "North":
            position -= t
        elif direction == "South":
            position += t
        # West and East do not change the position

        # Check if position goes out of bounds
        if position < 0 or position > MAX_POSITION:
            return "NO"

    # Must end at North Pole
    return "YES" if position == 0 else "NO"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Output the result
print(is_valid_journey(n, journey))