n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
total_bricks_needed = sum(max_height - h for h in a)

# Check if the total height can be achieved without any gaps
current_height = 0
is_possible = True

for height in a:
    if height > current_height:
        current_height = height
    elif height < current_height:
        is_possible = False
        break

print("YES" if is_possible else "NO")