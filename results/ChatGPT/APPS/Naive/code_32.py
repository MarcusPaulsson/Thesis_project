def check_journey(n, journey):
    position = 0  # 0 represents the North Pole, 20000 represents the South Pole

    for t, direction in journey:
        if position == 0 and direction != "South":
            return "NO"
        if position == 20000 and direction != "North":
            return "NO"
        
        if direction == "North":
            position -= t
        elif direction == "South":
            position += t
        elif direction == "West" or direction == "East":
            # Moving West or East does not change the position on the meridian
            continue

        # Ensure position does not go below 0 or above 20000
        if position < 0 or position > 20000:
            return "NO"

    # Final check to ensure Limak ends at the North Pole
    if position != 0:
        return "NO"

    return "YES"


# Input reading
n = int(input())
journey = [tuple(input().split()) for _ in range(n)]
journey = [(int(t), dir) for t, dir in journey]

# Check the journey and print the result
result = check_journey(n, journey)
print(result)