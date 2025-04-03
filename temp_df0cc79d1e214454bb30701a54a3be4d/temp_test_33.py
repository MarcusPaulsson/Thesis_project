import math

def solve():
    n = int(input())
    
    print(2)
    
    a = n
    b = n - 1
    
    for i in range(n - 1):
        print(a, b)
        a = (a + b + 1) // 2
        b = n - 2 - i
        if b < 1:
            break
        
t = int(input())
for _ in range(t):
    solve()