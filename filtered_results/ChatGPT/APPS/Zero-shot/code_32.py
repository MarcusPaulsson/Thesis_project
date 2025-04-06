def is_valid_journey(n, journey):
    current_position = 0  # 0 represents the North Pole, 20000 represents the South Pole
    for t, direction in journey:
        if current_position == 0 and direction != "South":
            return "NO"  # At North Pole, can only go South
        if current_position == 20000 and direction != "North":
            return "NO"  # At South Pole, can only go North
        
        if direction == "South":
            current_position += t
        elif direction == "North":
            current_position -= t
        # West and East do not change the position in terms of latitude
        # but we need to ensure that we don't go beyond the poles
        if current_position < 0 or current_position > 20000:
            return "NO"
    
    if current_position != 0:
        return "NO"  # Journey must end at the North Pole
    return "YES"

# Input reading
n = int(input().strip())
journey = [input().strip().split() for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Checking the validity of the journey
result = is_valid_journey(n, journey)
print(result)