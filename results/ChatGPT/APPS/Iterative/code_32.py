n = int(input())
position = 0  # Position in kilometers from the North Pole (0 = North Pole, 20000 = South Pole)

valid = True

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    if position == 0 and direction != "South":
        valid = False
        break
    elif position == 20000 and direction != "North":
        valid = False
        break

    if direction == "South":
        position += t
    elif direction == "North":
        position -= t
    # West and East do not affect the North/South position
    elif direction in ("West", "East"):
        continue

    # Check if the position is out of bounds
    if position < 0 or position > 20000:
        valid = False
        break

# Check if the journey ends at the North Pole
if valid and position == 0:
    print("YES")
else:
    print("NO")