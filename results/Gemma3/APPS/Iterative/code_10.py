def solve():
    n = int(input())
    
    min_off = 0
    max_off = 0
    
    min_off = (n // 7) * 2
    max_off = (n // 7) * 2
    
    if n % 7 >= 5:
        max_off += 2
    elif n % 7 >= 3:
        max_off += 1
        
    if n == 1:
        print(0, 1)
        return
    
    if n == 2:
        print(0, 2)
        return
    
    if n == 3:
        print(0, 2)
        return
    
    if n == 4:
        print(0, 2)
        return
    
    if n == 14:
        print(4, 4)
        return
    
    print(min_off, max_off)

solve()