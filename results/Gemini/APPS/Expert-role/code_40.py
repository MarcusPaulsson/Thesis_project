def solve():
    a, b, p = map(int, input().split())
    s = input()
    n = len(s)
    
    cost = 0
    i = n - 2
    while i >= 0:
        j = i
        while j >= 0 and s[j] == s[i]:
            j -= 1
        
        if s[i] == 'A':
            cost += a
        else:
            cost += b
            
        i = j
        if cost > p:
            print(i + 2)
            return
            
    print(1)

t = int(input())
for _ in range(t):
    solve()