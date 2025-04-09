def solve():
    a1, b1, a2, b2, l, r = map(int, input().split())
    
    count = 0
    
    for k in range(max(0, (l - b1) // a1), (r - b1) // a1 + 2):
        x = a1 * k + b1
        if x >= l and x <= r:
            if (x - b2) % a2 == 0 and (x - b2) // a2 >= 0:
                count += 1
    
    print(count)

solve()