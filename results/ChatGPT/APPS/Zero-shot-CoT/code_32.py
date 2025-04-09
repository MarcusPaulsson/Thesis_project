n = int(input())
position = 0  # position relative to the North Pole (0 is North Pole, 20000 is South Pole)

for _ in range(n):
    t_i, dir_i = input().split()
    t_i = int(t_i)

    if position == 0:  # If at North Pole
        if dir_i == "South":
            position += t_i
        else:
            print("NO")
            exit()
    elif position == 20000:  # If at South Pole
        if dir_i == "North":
            position -= t_i
        else:
            print("NO")
            exit()
    else:  # If somewhere in between
        if dir_i == "South":
            position += t_i
        elif dir_i == "North":
            position -= t_i
        elif dir_i == "East" or dir_i == "West":
            continue  # East and West do not affect the position

    # Check for invalid movement
    if position < 0 or position > 20000:
        print("NO")
        exit()

# Check if ended at North Pole
if position == 0:
    print("YES")
else:
    print("NO")