def solve():
    a, b, p = map(int, input().split())
    s = input()
    n = len(s)
    
    cost = 0
    last_change = n - 1
    
    for i in range(n - 2, -1, -1):
        if s[i] != s[i+1]:
            if s[i+1] == 'A':
                cost += a
            else:
                cost += b
            last_change = i + 1
            
        if cost > p:
            print(last_change + 1)
            return
    
    print(1)

t = int(input())
for _ in range(t):
    solve()