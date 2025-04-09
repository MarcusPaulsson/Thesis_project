def is_valid_journey(n, journey):
    current_position = 0  # North Pole is 0, South Pole is 20000

    for t, direction in journey:
        if current_position == 0 and direction != "South":
            return "NO"
        if current_position == 20000 and direction != "North":
            return "NO"
        
        if direction == "South":
            current_position += t
        elif direction == "North":
            current_position -= t
        # "West" and "East" do not affect the position in this model.
        
        if current_position < 0 or current_position > 20000:
            return "NO"

    if current_position != 0:
        return "NO"
    
    return "YES"

# Read input
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Output result
print(is_valid_journey(n, journey))