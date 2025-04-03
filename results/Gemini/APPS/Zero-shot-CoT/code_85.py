def solve():
    s = input()
    x = int(input())
    n = len(s)
    w = [''] * n
    
    for i in range(n):
        w[i] = '1'

    for i in range(n):
        if s[i] == '0':
            if i - x >= 0:
                w[i - x] = '0'
            if i + x < n:
                w[i + x] = '0'
    
    
    new_s = [''] * n
    for i in range(n):
        new_s[i] = '0'
        if i - x >= 0 and w[i - x] == '1':
            new_s[i] = '1'
        if i + x < n and w[i + x] == '1':
            new_s[i] = '1'
            
    if "".join(new_s) == s:
        print("".join(w))
    else:
        print("-1")


t = int(input())
for _ in range(t):
    solve()