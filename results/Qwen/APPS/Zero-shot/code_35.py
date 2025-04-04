n, m = map(int, input().split())
colors = set()
for i in range(n):
    row = input()
    if len(set(row)) != 1:
        print("NO")
        exit()
    colors.add(row[0])
if len(colors) != 3:
    print("NO")
else:
    print("YES")