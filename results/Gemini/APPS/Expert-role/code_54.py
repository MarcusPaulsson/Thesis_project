def solve():
    n = int(input())
    s = list(map(int, input().split()))

    total_sum = 0
    for x in s:
        if x <= 2048:
            total_sum += x

    if total_sum >= 2048:
        print("YES")
    else:
        print("NO")

q = int(input())
for _ in range(q):
    solve()