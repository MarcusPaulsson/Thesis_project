n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
target_height = min(a)

can_complete = True

for height in a:
    if height < target_height or height > max_height:
        can_complete = False
        break

if can_complete:
    print("YES")
else:
    print("NO")