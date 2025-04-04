n = int(input())
position = 0

for _ in range(n):
    t, d = input().split()
    t = int(t)
    
    if d == "North":
        if position + t > 20000:
            print("NO")
            exit()
        position += t
    elif d == "South":
        if position - t < -20000:
            print("NO")
            exit()
        position -= t
    elif d == "East" or d == "West":
        if position == 20000 or position == -20000:
            print("NO")
            exit()
        position += t if d == "East" else -t

if position == 0:
    print("YES")
else:
    print("NO")