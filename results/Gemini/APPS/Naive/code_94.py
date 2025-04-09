def solve():
    a, b, x = map(int, input().split())
    
    if a > b:
        start = 0
    else:
        start = 1
    
    res = ""
    
    while x > 1:
        res += str(start)
        if start == 0:
            a -= 1
            start = 1
        else:
            b -= 1
            start = 0
        x -= 1
    
    if start == 0:
        res += "0" * a + "1" * b
    else:
        res += "1" * b + "0" * a
        
    print(res)

solve()