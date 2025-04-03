def solve():
    n = int(input())
    s = input()
    
    s = list(s)
    
    i = 0
    while i < len(s) - 1:
        if s[i] == '1' and s[i+1] == '0':
            s.pop(i+1)
            i = 0
        else:
            i += 1
            
    print("".join(s))

t = int(input())
for _ in range(t):
    solve()