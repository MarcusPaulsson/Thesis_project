def is_valid_journey(n, journey):
    position = 0  # Start at the North Pole (0 km)
    
    for t, direction in journey:
        if position == 0 and direction != "South":
            return "NO"  # At North Pole, can only go South
        if position == 20000 and direction != "North":
            return "NO"  # At South Pole, can only go North
        
        if direction == "South":
            position += t
        elif direction == "North":
            position -= t
        elif direction == "East" or direction == "West":
            # East and West do not change the position in km
            continue
        
        # Check if position goes out of bounds
        if position < 0 or position > 20000:
            return "NO"
    
    # Journey must end at the North Pole
    return "YES" if position == 0 else "NO"

# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), direction) for t, direction in journey]

# Output result
print(is_valid_journey(n, journey))