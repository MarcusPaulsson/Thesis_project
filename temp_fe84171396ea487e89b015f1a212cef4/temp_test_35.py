def solve():
    n = int(input())
    e = list(map(int, input().split()))
    e.sort()
    
    count = 0
    group_size = 0
    
    for i in range(n):
        group_size += 1
        if group_size >= e[i]:
            count += 1
            group_size = 0
            
    print(count)

t = int(input())
for _ in range(t):
    solve()