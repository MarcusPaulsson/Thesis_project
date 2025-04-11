def solve():
    a, b, x = map(int, input().split())
    
    if a > b:
        start = 0
        a_char = '0'
        b_char = '1'
    else:
        start = 1
        a_char = '1'
        b_char = '0'
    
    result = ""
    
    if start == 0:
        result += a_char
        a -= 1
    else:
        result += b_char
        b -= 1
    
    x -= 1
    
    while x > 0:
        if result[-1] == a_char:
            result += b_char
            b -= 1
        else:
            result += a_char
            a -= 1
        x -= 1
    
    if result[-1] == a_char:
        result += b_char * b
        result += a_char * a
    else:
        result += a_char * a
        result += b_char * b
    
    print(result)

solve()