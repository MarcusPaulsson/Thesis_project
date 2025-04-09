n = int(input())
position = 0  # Position in kilometers from the North Pole

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    # Check movement constraints
    if position == 0 and direction != "South":
        print("NO")
        exit()
    elif position == 20000 and direction != "North":
        print("NO")
        exit()

    # Update position based on direction
    if direction == "South":
        position += t
    elif direction == "North":
        position -= t
    # East and West do not change the position in terms of North/South
    elif direction in ["East", "West"]:
        continue

    # Check for valid position range
    if position < 0 or position > 20000:
        print("NO")
        exit()

# Check if ending at the North Pole
if position == 0:
    print("YES")
else:
    print("NO")