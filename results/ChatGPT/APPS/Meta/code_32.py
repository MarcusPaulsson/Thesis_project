def is_valid_journey(n, journey):
    current_distance_from_pole = 0  # Distance from the North Pole in kilometers

    for t, direction in journey:
        if current_distance_from_pole == 0 and direction != "South":
            return "NO"  # At North Pole, can only move South
        if current_distance_from_pole == 20000 and direction != "North":
            return "NO"  # At South Pole, can only move North
        
        if direction == "South":
            current_distance_from_pole += t
        elif direction == "North":
            current_distance_from_pole -= t
        # East and West do not change the distance from the poles, so we ignore them

        # Check if we exceed the limits
        if current_distance_from_pole < 0 or current_distance_from_pole > 20000:
            return "NO"

    # Journey must end at the North Pole
    return "YES" if current_distance_from_pole == 0 else "NO"


# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Output the result
print(is_valid_journey(n, journey))