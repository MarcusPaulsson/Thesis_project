def solve():
    a, b, x = map(int, input().split())
    
    if a > b:
        start_with_zero = True
    else:
        start_with_zero = False
        
    s = ""
    
    if start_with_zero:
        
        if x % 2 == 0:
            while x > 0:
                s += "0"
                a -= 1
                s += "1"
                b -= 1
                x -= 2
            s += "0" * a
            s += "1" * b
        else:
            while x > 1:
                s += "0"
                a -= 1
                s += "1"
                b -= 1
                x -= 2
            s += "0" * a
            s += "1" * b
            s += "0"
            a -= 1
            s = s[::-1]
    else:
        if x % 2 == 0:
            while x > 0:
                s += "1"
                b -= 1
                s += "0"
                a -= 1
                x -= 2
            s += "1" * b
            s += "0" * a
        else:
            while x > 1:
                s += "1"
                b -= 1
                s += "0"
                a -= 1
                x -= 2
            s += "1" * b
            s += "0" * a
            s += "1"
            b -= 1
            s = s[::-1]
    
    print(s)

solve()