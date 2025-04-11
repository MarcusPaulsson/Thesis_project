def solve():
    n = int(input())
    s = str(n)
    length = len(s)
    
    first_digit = int(s[0])
    
    next_lucky = (first_digit + 1) * (10**(length-1))
    
    print(next_lucky - n)

solve()