def solve():
    x = float(input())
    
    if 0 < x < 1:
        if x < 0.5:
            print(1, 1)
        else:
            print(1, 3)
    elif 1 <= x < 2:
        print(3, 2)
    elif 2 <= x < 3:
        print(6, 3)
    elif 3 <= x < 4:
        print(8, 5)
    elif 4 <= x < 5:
        print(9, 9)

solve()