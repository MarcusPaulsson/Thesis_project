def solve():
    a, b, x = map(int, input().split())

    if a > b:
        start = 0
    else:
        start = 1

    s = ""
    
    while x > 1:
        if start == 0:
            s += "0"
            a -= 1
            start = 1
        else:
            s += "1"
            b -= 1
            start = 0
        x -= 1
    
    if start == 0:
        s += "0"
        a -= 1
        s += "0" * a
        s += "1" * b
    else:
        s += "1"
        b -= 1
        s += "1" * b
        s += "0" * a
        
    print(s)

solve()