def solve():
    n = int(input())
    s = list(map(int, input().split()))
    s = set(s)
    
    for k in range(1, 1025):
        new_s = set()
        for val in s:
            new_s.add(val ^ k)
        
        if new_s == s:
            print(k)
            return
    
    print("-1")

t = int(input())
for _ in range(t):
    solve()