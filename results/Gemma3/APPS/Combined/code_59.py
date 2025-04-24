def solve():
    n, x, y = map(int, input().split())
    s = input()
    
    target = 10**y
    
    ops = 0
    for i in range(x):
        if i < y:
            if int(s[n-1-i]) != 0:
                ops += 1
        else:
            if int(s[n-1-i]) != 1:
                ops += 1
                
    print(ops)

solve()