n = int(input())
current_position = 0  # 0 for North Pole, 20000 for South Pole

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    if current_position == 0 and direction != "South":
        print("NO")
        break
    elif current_position == 20000 and direction != "North":
        print("NO")
        break
    elif direction == "North":
        current_position -= t
    elif direction == "South":
        current_position += t
    elif direction in {"West", "East"}:
        continue

    if current_position < 0 or current_position > 20000:
        print("NO")
        break
else:
    print("YES" if current_position == 0 else "NO")