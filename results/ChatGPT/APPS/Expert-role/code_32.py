def is_valid_journey(n, journey):
    current_position = 0  # Position in kilometers from North Pole (0 means North Pole, 20000 means South Pole)

    for t, direction in journey:
        if current_position == 0 and direction != "South":
            return "NO"
        if current_position == 20000 and direction != "North":
            return "NO"

        if direction == "North":
            current_position -= t
        elif direction == "South":
            current_position += t
        elif direction in ["West", "East"]:
            continue  # No change in position

        if current_position < 0 or current_position > 20000:
            return "NO"

    return "YES" if current_position == 0 else "NO"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Output result
print(is_valid_journey(n, journey))