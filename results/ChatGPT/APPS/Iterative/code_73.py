n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
total_bricks_needed = sum(max_height - height for height in a)

# Check if the total number of bricks needed is even
# An even number of bricks can be used to equalize the wall
if total_bricks_needed % 2 == 0:
    print("YES")
else:
    print("NO")