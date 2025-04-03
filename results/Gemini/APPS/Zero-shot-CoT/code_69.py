def solve():
    a, b = map(int, input().split())
    s = input()
    n = len(s)
    
    gaps = []
    
    first = -1
    last = -1
    
    for i in range(n):
        if s[i] == '1':
            if first == -1:
                first = i
            last = i
            
    if first == -1:
        print(0)
        return
    
    
    
    
    prev = first
    for i in range(first + 1, last + 1):
        if s[i] == '1':
            if i - prev - 1 > 0:
                gaps.append(i - prev - 1)
            prev = i
    
    
    cost = a
    
    for gap in gaps:
        cost += min(a, gap * b)
    
    print(cost)

t = int(input())
for _ in range(t):
    solve()