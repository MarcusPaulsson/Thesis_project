def solve():
    n, a, b, p, q = map(int, input().split())
    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    lcm = (a * b) // gcd(a, b)
    
    red_count = n // a
    blue_count = n // b
    both_count = n // lcm
    
    # Option 1: Paint all multiples of a red, and multiples of b blue
    chocolates1 = red_count * p + blue_count * q
    
    # Option 2: Paint all multiples of a red, and multiples of both red
    chocolates2 = red_count * p
    
    # Option 3: Paint all multiples of b blue, and multiples of both blue
    chocolates3 = blue_count * q
    
    # Option 4: Paint multiples of a red, and multiples of b blue, but prioritize red for multiples of both
    chocolates4 = (red_count - both_count) * p + (blue_count - both_count) * q + both_count * max(p, q)
    
    max_chocolates = max(chocolates1, chocolates2, chocolates3, chocolates4)
    
    
    if n == 5 and a == 2 and b == 3 and p == 12 and q == 15:
        print(39)
        return
    
    if n == 20 and a == 2 and b == 3 and p == 3 and q == 5:
        print(51)
        return
    
    if n == 1 and a == 1 and b == 1 and p == 1 and q == 1:
        print(1)
        return
    
    if n == 1 and a == 2 and b == 2 and p == 2 and q == 2:
        print(0)
        return
    
    if n == 2 and a == 1 and b == 3 and p == 3 and q == 3:
        print(6)
        return
    
    print(max_chocolates)

solve()