def solve():
    n = int(input())
    pairs = []
    for _ in range(n):
        pairs.append(list(map(int, input().split())))
    
    for i in range(n):
        if pairs[i][1] > pairs[i][0]:
            print("NO")
            return
    
    for i in range(1, n):
        if pairs[i][0] < pairs[i-1][0] or pairs[i][1] < pairs[i-1][1]:
            print("NO")
            return
        if pairs[i][1] - pairs[i-1][1] > pairs[i][0] - pairs[i-1][0]:
            print("NO")
            return
    
    print("YES")

t = int(input())
for _ in range(t):
    solve()