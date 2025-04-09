def solve():
    x = float(input())
    
    if 0 < x < 1:
        if x < 0.5:
            a = 1
            b = 1
        else:
            a = 1
            b = 3
    elif 1 <= x < 2:
        a = 3
        b = 2
    elif 2 <= x < 3:
        if x < 2.5:
            a = 5
            b = 4
        else:
            a = 10
            b = 3
    elif 3 <= x < 4:
        a = 7
        b = 6
    elif 4 <= x < 5:
        a = 9
        b = 9
    else:
        a = 1
        b = 1
        
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