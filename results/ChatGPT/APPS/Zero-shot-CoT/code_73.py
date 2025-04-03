n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
total_bricks_needed = 0
current_bricks_available = 0

for height in a:
    if height < max_height:
        total_bricks_needed += (max_height - height)
    elif height > max_height:
        print("NO")
        break
else:
    print("YES")