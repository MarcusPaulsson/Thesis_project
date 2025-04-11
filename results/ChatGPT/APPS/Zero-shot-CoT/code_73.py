n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
total_bricks_needed = 0
total_bricks_available = 0

for height in a:
    total_bricks_needed += max_height - height
    total_bricks_available += height

if total_bricks_needed <= total_bricks_available:
    print("YES")
else:
    print("NO")