n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
min_height = min(a)

# Check if all heights can be raised to max_height without gaps
can_complete = True
for i in range(n):
    if a[i] < min_height or (i > 0 and a[i] != a[i - 1] and a[i] != max_height):
        can_complete = False
        break

print("YES" if can_complete else "NO")