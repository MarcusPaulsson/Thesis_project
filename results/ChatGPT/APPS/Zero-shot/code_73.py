n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
total_bricks = sum(max_height - height for height in a)

if total_bricks % 2 == 0:
    print("YES")
else:
    print("NO")