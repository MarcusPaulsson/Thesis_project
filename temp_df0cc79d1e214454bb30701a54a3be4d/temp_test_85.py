def solve():
    s = input()
    x = int(input())
    n = len(s)
    w = ['0'] * n
    
    for i in range(n):
        if s[i] == '1':
            if i - x >= 0:
                w[i - x] = '1'
            if i + x < n:
                w[i + x] = '1'
    
    w_str = "".join(w)
    
    s_reconstructed = ['0'] * n
    for i in range(n):
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