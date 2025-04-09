n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
# Check if the wall can be completed
can_complete = True

for height in a:
    if height < max_height and (height % 2) != (max_height % 2):
        can_complete = False
        break

print("YES" if can_complete else "NO")