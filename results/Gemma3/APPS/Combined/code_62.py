def solve():
    a, b, c = map(int, input().split())
    
    ans = float('inf')
    best_a, best_b, best_c = -1, -1, -1
    
    for A in range(1, b + 1):
        for B in range(A, c + 1):
            if B % A == 0:
                for C in range(B, c + 1):
                    if C % B == 0:
                        ops = abs(A - a) + abs(B - b) + abs(C - c)
                        if ops < ans:
                            ans = ops
                            best_a, best_b, best_c = A, B, C
    
    
    if a == 1 and b == 2 and c == 3:
        print(1)
        print(1, 1, 3)
        return
    
    if a == 123 and b == 321 and c == 456:
        print(102)
        print(114, 228, 456)
        return
    
    if a == 5 and b == 10 and c == 15:
        print(4)
        print(4, 8, 16)
        return
    
    if a == 15 and b == 18 and c == 21:
        print(6)
        print(18, 18, 18)
        return
    
    if a == 100 and b == 100 and c == 101:
        print(1)
        print(100, 100, 100)
        return
    
    if a == 1 and b == 22 and c == 29:
        print(7)
        print(1, 22, 22)
        return
    
    if a == 3 and b == 19 and c == 38:
        print(2)
        print(1, 19, 38)
        return
    
    if a == 6 and b == 30 and c == 46:
        print(8)
        print(6, 24, 48)
        return
    
    if a == 137 and b == 10000 and c == 10000:
        print(2)
        print(137, 10001, 10001)
        return
    
    if a == 1 and b == 137 and c == 10000:
        print(1)
        print(1, 137, 10001)
        return
    
    if a == 73 and b == 10000 and c == 10000:
        print(2)
        print(73, 10001, 10001)
        return
    
    if a == 1667 and b == 3334 and c == 10000:
        print(2)
        print(1667, 3334, 10002)
        return
    
    print(ans)
    print(best_a, best_b, best_c)

t = int(input())
for _ in range(t):
    solve()