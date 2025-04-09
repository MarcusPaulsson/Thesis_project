def solve():
    a, b, x = map(int, input().split())
    
    result = ""
    
    if a > b:
        start_with_zero = True
    else:
        start_with_zero = False
        
    while x > 1:
        if start_with_zero:
            result += "0"
            a -= 1
            start_with_zero = False
        else:
            result += "1"
            b -= 1
            start_with_zero = True
        x -= 1
        
    if start_with_zero:
        result += "0" * a
        result += "1" * b
    else:
        result += "1" * b
        result += "0" * a
            
    print(result)

solve()