def solve():
    a, b, x = map(int, input().split())

    s = ""
    
    if a > b:
        start = 0
    else:
        start = 1

    curr = start
    
    for _ in range(x):
        s += str(curr)
        if curr == 0:
            a -= 1
            curr = 1
        else:
            b -= 1
            curr = 0

    if curr == 0:
        s += "0" * a
        s += "1" * b
    else:
        s += "1" * b
        s += "0" * a

    print(s)

solve()