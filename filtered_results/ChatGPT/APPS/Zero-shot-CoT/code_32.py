def check_journey(n, instructions):
    position = 0  # Starting at North Pole, position is 0 (0 km from the North Pole)
    
    for t, direction in instructions:
        if position == 0 and direction != "South":
            return "NO"  # At North Pole, can only move South
        if position == 20000 and direction != "North":
            return "NO"  # At South Pole, can only move North
        
        if direction == "North":
            position -= t
        elif direction == "South":
            position += t
        elif direction == "East" or direction == "West":
            # East and West don't change the position in terms of North/South
            continue
        
        if position < 0 or position > 20000:
            return "NO"  # Out of bounds
        
    if position != 0:
        return "NO"  # Must end at North Pole
    
    return "YES"


# Read input
n = int(input())
instructions = [tuple(input().split()) for _ in range(n)]
instructions = [(int(t), direction) for t, direction in instructions]

# Check the journey and print result
result = check_journey(n, instructions)
print(result)