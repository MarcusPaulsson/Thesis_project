n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
min_height = min(a)

# Check if all parts can be raised to the max height
for height in a:
    if (height < min_height) or (height > max_height):
        print("NO")
        break
else:
    # Check for gaps in the wall
    if any(a[i] < a[i-1] for i in range(1, n)):
        print("NO")
    else:
        print("YES")