n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
total_bricks_needed = 0
total_bricks_available = 0

for i in range(n):
    total_bricks_needed += max_height - a[i]
    if i > 0 and a[i] == a[i - 1]:
        total_bricks_available += 1

if total_bricks_needed <= total_bricks_available:
    print("YES")
else:
    print("NO")