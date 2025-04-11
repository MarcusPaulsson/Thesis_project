n = int(input())
position = 0  # Position in kilometers from the North Pole (0 at North Pole, 20000 at South Pole)

valid = True

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    if direction == "North":
        if position == 0 or position + t > 20000:
            valid = False
            break
        position += t
    elif direction == "South":
        if position == 20000 or position - t < 0:
            valid = False
            break
        position -= t
    elif direction in ["West", "East"]:
        # Moving West or East does not change the position in terms of North/South
        continue

# Check if the journey is valid and ends at the North Pole
if valid and position == 0:
    print("YES")
else:
    print("NO")