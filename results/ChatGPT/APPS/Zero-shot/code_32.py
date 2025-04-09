n = int(input())
position = 0  # Position in kilometers from North Pole (0 at North Pole, 20000 at South Pole)

valid = True

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    if direction == "South":
        if position == 0 or position + t > 20000:
            valid = False
            break
        position += t
    elif direction == "North":
        if position == 20000 or position - t < 0:
            valid = False
            break
        position -= t
    elif direction in ["West", "East"]:
        if position == 0 or position == 20000:
            valid = False
            break

if valid and position == 0:
    print("YES")
else:
    print("NO")