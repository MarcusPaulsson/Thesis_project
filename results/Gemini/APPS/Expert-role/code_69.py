def solve():
    a, b = map(int, input().split())
    s = input()
    n = len(s)
    
    gaps = []
    start = -1
    end = -1
    
    first_one = -1
    last_one = -1
    
    for i in range(n):
        if s[i] == '1':
            if first_one == -1:
                first_one = i
            last_one = i
    
    if first_one == -1:
        print(0)
        return

    
    start = first_one
    end = last_one
    
    
    count = 0
    
    i = start
    while i <= end:
        if s[i] == '0':
            j = i
            while j <= end and s[j] == '0':
                j += 1
            gaps.append(j - i)
            i = j
        else:
            i += 1
    
    cost = a
    
    for gap in gaps:
        if gap * b < a:
            cost += gap * b
        else:
            cost += a
            
    print(cost)

t = int(input())
for _ in range(t):
    solve()