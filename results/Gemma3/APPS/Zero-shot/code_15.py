def solve():
    a, b, c = map(int, input().split())
    
    if a == b:
        print("YES")
        return
    
    if c == 0:
        if a == b:
            print("YES")
        else:
            print("NO")
        return
    
    if (b - a) % c == 0 and (b - a) // c >= 0:
        print("YES")
    else:
        print("NO")

solve()