def solve():
    a, b, x = map(int, input().split())
    
    s = ""
    
    if a > b:
        start = 0
    else:
        start = 1
    
    
    for i in range(x):
        s += str(start)
        start = 1 - start
    
    if start == 0:
        s += "0" * (a - s.count("0"))
        s += "1" * (b - s.count("1"))
    else:
        s += "1" * (b - s.count("1"))
        s += "0" * (a - s.count("0"))
        
    print(s)

solve()