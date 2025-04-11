def solve():
    a, b, x = map(int, input().split())
    
    if a > b:
        start = 0
        a, b = b, a
    else:
        start = 1
    
    s = ""
    
    if x % 2 == 0:
        for i in range(x // 2):
            s += str(start)
            s += str(1 - start)
        
        if start == 0:
            s = "1" + s
            b -= 1
            s += "0" * a
            s += "1" * b
        else:
            s = "0" + s
            a -= 1
            s += "1" * b
            s += "0" * a
        
    else:
        for i in range(x // 2):
            s += str(start)
            s += str(1 - start)
        
        s += str(start)
        
        if start == 0:
            a -= 1
            s += "0" * a
            s += "1" * b
        else:
            b -= 1
            s += "1" * b
            s += "0" * a
    
    if a > b:
        start = 0
        a, b = b, a
        s = "".join(["1" if c == "0" else "0" for c in s])
    else:
        start = 1
    
    print(s)

solve()