import math

def solve():
    d = int(input())
    
    delta = d * d - 4 * d
    
    if delta < 0:
        print("N")
    else:
        sqrt_delta = math.sqrt(delta)
        a = (d + sqrt_delta) / 2
        b = (d - sqrt_delta) / 2
        
        print("Y", a, b)

t = int(input())
for _ in range(t):
    solve()