def solve():
    a, b, x = map(int, input().split())
    
    if a > b:
        start = 0
    else:
        start = 1
    
    s = ""
    
    for i in range(x):
        s += str(start)
        start = 1 - start
    
    if start == 0:
        s += "0" * (a - (x + 1) // 2)
        s += "1" * (b - x // 2)
    else:
        s += "1" * (b - (x + 1) // 2)
        s += "0" * (a - x // 2)
    
    print(s)

solve()