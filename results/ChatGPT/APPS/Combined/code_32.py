def is_valid_journey(n, journey):
    current_position = 0  # Starting at the North Pole, represented as 0 km
    for distance, direction in journey:
        if current_position == 0 and direction != "South":
            return "NO"  # At North Pole, can only move South
        if current_position == 20000 and direction != "North":
            return "NO"  # At South Pole, can only move North

        if direction == "North":
            current_position -= distance
        elif direction == "South":
            current_position += distance
        elif direction in {"West", "East"}:
            continue  # Moving East or West does not affect North/South position
        
        # Check if the current position goes out of bounds
        if current_position < 0 or current_position > 20000:
            return "NO"

    return "YES" if current_position == 0 else "NO"  # Must end at the North Pole


# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), d) for t, d in journey]

# Output the result
print(is_valid_journey(n, journey))