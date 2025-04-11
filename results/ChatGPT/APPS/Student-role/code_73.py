n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
min_height = min(a)

# Check if the wall can be completed
if all(x == max_height or x == min_height for x in a):
    print("YES")
else:
    print("NO")