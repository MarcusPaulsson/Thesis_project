n = int(input())
current_distance = 0  # Distance from the North Pole in kilometers

valid = True

for _ in range(n):
    t_i, dir_i = input().split()
    t_i = int(t_i)
    
    if current_distance == 0 and dir_i != "South":
        valid = False
        break
    if current_distance == 20000 and dir_i != "North":
        valid = False
        break
    
    if dir_i == "South":
        current_distance += t_i
    elif dir_i == "North":
        current_distance -= t_i
    elif dir_i == "West" or dir_i == "East":
        # Moving West or East does not affect the distance from the poles
        pass
    
    if current_distance < 0 or current_distance > 20000:
        valid = False
        break

if valid and current_distance == 0:
    print("YES")
else:
    print("NO")