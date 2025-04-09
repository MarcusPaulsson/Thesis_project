n = int(input())
a = list(map(int, input().split()))

max_height = max(a)

# Check for gaps
for height in a:
    if height < max_height and (height + 1) not in a:
        print("NO")
        break
else:
    print("YES")