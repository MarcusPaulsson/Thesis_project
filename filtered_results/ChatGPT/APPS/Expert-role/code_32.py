n = int(input())
current_position = 0  # 0 means North Pole, 20000 means South Pole

valid = True

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    if current_position == 0 and direction != "South":
        valid = False
        break
    if current_position == 20000 and direction != "North":
        valid = False
        break

    if direction == "South":
        current_position += t
    elif direction == "North":
        current_position -= t
    elif direction in ["West", "East"]:
        # West and East do not affect the north-south position
        continue

    if current_position < 0 or current_position > 20000:
        valid = False
        break

if valid and current_position == 0:
    print("YES")
else:
    print("NO")