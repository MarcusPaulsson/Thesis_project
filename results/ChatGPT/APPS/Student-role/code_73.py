n = int(input())
a = list(map(int, input().split()))

# Find the maximum height of the wall
max_height = max(a)

# Check if all parts can reach the maximum height without gaps
for height in a:
    if height < max_height and (height + 1) not in a:
        print("NO")
        break
else:
    print("YES")