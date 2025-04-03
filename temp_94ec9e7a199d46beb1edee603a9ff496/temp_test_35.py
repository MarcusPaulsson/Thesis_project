def solve():
    n = int(input())
    e = list(map(int, input().split()))
    e.sort()
    
    groups = 0
    current_group_size = 0
    
    for inexperience in e:
        current_group_size += 1
        if current_group_size >= inexperience:
            groups += 1
            current_group_size = 0
            
    print(groups)

t = int(input())
for _ in range(t):
    solve()