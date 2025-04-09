def solve():
    a, b, x = map(int, input().split())
    
    if a > b:
        start = 0
    else:
        start = 1
    
    s = ""
    
    if start == 0:
        s += "0"
        a -= 1
    else:
        s += "1"
        b -= 1
    
    
    while x > 0:
        if s[-1] == '0':
            if b > 0:
                s += "1"
                b -= 1
                x -= 1
            else:
                s += "0" * a
                a = 0
                break
        else:
            if a > 0:
                s += "0"
                a -= 1
                x -= 1
            else:
                s += "1" * b
                b = 0
                break
    
    if a > 0:
        s += "0" * a
    if b > 0:
        s += "1" * b
    
    print(s)

solve()