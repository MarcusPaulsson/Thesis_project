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
    
    x -= 1
    
    curr = 1 - start
    
    while x > 0:
        if curr == 0:
            if a > 0:
                s += "0"
                a -= 1
            else:
                s += "1"
                b -= 1
        else:
            if b > 0:
                s += "1"
                b -= 1
            else:
                s += "0"
                a -= 1
        
        curr = 1 - curr
        x -= 1
        
    if curr == 0:
        s += "0" * a
        s += "1" * b
    else:
        s += "1" * b
        s += "0" * a
    
    print(s)

solve()