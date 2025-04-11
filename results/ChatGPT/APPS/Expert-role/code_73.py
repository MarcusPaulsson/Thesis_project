n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
total_bricks_needed = 0

for height in a:
    total_bricks_needed += max_height - height

# Check if the total number of bricks needed is even
if total_bricks_needed % 2 == 0:
    print("YES")
else:
    print("NO")