import math

def solve():
    n = int(input())
    
    print(2)
    
    a = n
    
    for i in range(n - 1):
        b = a - 1
        print(a, b)
        a = math.ceil((a + b) / 2)
        
t = int(input())
for _ in range(t):
    solve()