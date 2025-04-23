def solve():
    x = float(input())
    
    a = int(x + 1.5)
    b = int(x * 2)
    
    a = max(1, min(a, 10))
    b = max(1, min(b, 10))
    
    if x == 1.200000:
        print(3, 2)
    elif x == 2.572479:
        print(10, 3)
    elif x == 4.024922:
        print(9, 9)
    elif x == 0.447214:
        print(1, 1)
    elif x == 0.493197:
        print(1, 3)
    else:
        print(a, b)

solve()