def solve():
    a, b, x = map(int, input().split())
    
    if a > b:
        start = '0'
        a -= 1
    else:
        start = '1'
        b -= 1
    
    s = start
    
    for i in range(x - 1):
        if start == '0':
            if len(s) % 2 == 1:
                s += '1'
                b -= 1
            else:
                s += '0'
                a -= 1
        else:
            if len(s) % 2 == 1:
                s += '0'
                a -= 1
            else:
                s += '1'
                b -= 1
                
        start = s[-1]
    
    if start == '0':
        s += '0' * a
        s += '1' * b
    else:
        s += '1' * b
        s += '0' * a
        
    print(s)
    
solve()