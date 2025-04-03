def solve():
    a, b, x = map(int, input().split())
    
    s = ""
    
    if a > b:
        start = 0
    else:
        start = 1
    
    
    
    diffs = 0
    
    
    if start == 0:
        s += "0"
        a -= 1
    else:
        s += "1"
        b -= 1
        
    
    
    
    
    while diffs < x - 1:
        if s[-1] == '0':
            if b > 0:
                s += '1'
                b -=1
                diffs += 1
            else:
                s += '0'
                a -= 1
                diffs += 1
        else:
            if a > 0:
                s += '0'
                a -= 1
                diffs += 1
            else:
                s += '1'
                b -= 1
                diffs += 1
    
    if s[-1] == '0':
        s += '0' * a
        s += '1' * b
    else:
        s += '1'*b
        s += '0'*a
    
    print(s)

solve()