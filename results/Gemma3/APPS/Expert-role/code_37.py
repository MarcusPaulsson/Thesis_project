def solve():
    a, b, c = map(int, input().split())
    
    for x in range(c // a + 1):
        remaining = c - x * a
        if remaining >= 0 and remaining % b == 0:
            print("Yes")
            return
    
    print("No")

solve()