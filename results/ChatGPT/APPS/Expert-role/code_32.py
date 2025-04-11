def is_valid_journey(n, journey):
    position = 0  # Position on the meridian, 0 is North Pole, 20000 is South Pole

    for t, direction in journey:
        if position == 0 and direction != "South":
            return "NO"
        if position == 20000 and direction != "North":
            return "NO"

        if direction == "South":
            position += t
        elif direction == "North":
            position -= t
        elif direction == "East" or direction == "West":
            # East and West do not change the position on the meridian
            continue

        if position < 0 or position > 20000:
            return "NO"

    if position != 0:
        return "NO"

    return "YES"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), direction) for t, direction in journey]

# Output result
print(is_valid_journey(n, journey))