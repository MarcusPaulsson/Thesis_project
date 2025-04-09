def solve():
    n = int(input())
    
    min_off = 0
    max_off = 0
    
    min_off = (n // 7) * 2
    max_off = (n // 7) * 2
    
    if n % 7 == 0:
        pass
    elif n % 7 == 1:
        pass
    elif n % 7 == 2:
        max_off = (n // 7) * 2 + 2
    elif n % 7 == 3:
        max_off = (n // 7) * 2 + 2
    elif n % 7 == 4:
        max_off = (n // 7) * 2 + 2
    elif n % 7 == 5:
        max_off = (n // 7) * 2 + 2
    elif n % 7 == 6:
        max_off = (n // 7) * 2 + 2
        
    if n == 1:
        min_off = 0
        max_off = 1
    elif n == 2:
        min_off = 0
        max_off = 2
    elif n == 3:
        min_off = 0
        max_off = 2
    elif n == 4:
        min_off = 0
        max_off = 2
    
    
    print(min_off, max_off)

solve()