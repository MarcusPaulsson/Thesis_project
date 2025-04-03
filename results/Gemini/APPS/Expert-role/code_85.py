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
    
    w_str = "".join(w)
    
    s_reconstructed = [''] * n
    for i in range(n):
        s_reconstructed[i] = '0'
        if i - x >= 0 and w_str[i - x] == '1':
            s_reconstructed[i] = '1'
        if i + x < n and w_str[i + x] == '1':
            s_reconstructed[i] = '1'
    
    s_reconstructed_str = "".join(s_reconstructed)
    
    if s_reconstructed_str == s:
        print(w_str)
    else:
        print("-1")

t = int(input())
for _ in range(t):
    solve()