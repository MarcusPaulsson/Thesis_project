n = int(input())
current_position = 0  # Position in kilometers from the North Pole (0 to 20000)
valid = True

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    if direction == "South":
        if current_position == 0:  # At North Pole
            valid = False
        current_position += t
    elif direction == "North":
        if current_position == 20000:  # At South Pole
            valid = False
        current_position -= t
    elif direction in ["West", "East"]:
        # Moving West or East does not change the position in terms of North/South
        pass

    # Check if current position is valid
    if current_position < 0 or current_position > 20000:
        valid = False

# Final check if we end at the North Pole
if current_position != 0:
    valid = False

print("YES" if valid else "NO")