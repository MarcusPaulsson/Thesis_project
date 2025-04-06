def is_journey_valid(n, movements):
    current_position = 20000  # Starting at North Pole, 0 km to South Pole, 20000 km from North Pole

    for t, direction in movements:
        if current_position == 20000 and direction != "South":
            return "NO"  # At North Pole, can only move South
        if current_position == 0 and direction != "North":
            return "NO"  # At South Pole, can only move North
        
        if direction == "South":
            current_position -= t
        elif direction == "North":
            current_position += t
        elif direction in ["West", "East"]:
            # West and East do not change the position in terms of North-South distance
            pass
        
        # Check if current_position goes out of bounds
        if current_position < 0 or current_position > 20000:
            return "NO"

    # Check if we end at the North Pole
    if current_position != 20000:
        return "NO"

    return "YES"

# Read input
n = int(input())
movements = [tuple(input().split()) for _ in range(n)]
movements = [(int(t), dir) for t, dir in movements]

# Get the result and print it
result = is_journey_valid(n, movements)
print(result)