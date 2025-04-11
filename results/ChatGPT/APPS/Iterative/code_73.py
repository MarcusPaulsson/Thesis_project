n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
total_bricks_needed = 0
total_bricks_available = sum(a)

for height in a:
    if height < max_height:
        total_bricks_needed += max_height - height

# Check if the total available bricks can cover the needed bricks
if total_bricks_available >= total_bricks_needed:
    print("YES")
else:
    print("NO")