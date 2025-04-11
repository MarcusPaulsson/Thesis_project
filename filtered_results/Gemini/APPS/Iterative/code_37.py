def solve():
    a, b, c = map(int, input().split())
    
    for i in range(c // a + 1):
        if (c - i * a) % b == 0 and (c - i * a) >= 0:
            print("Yes")
            return
    
    print("No")

solve()