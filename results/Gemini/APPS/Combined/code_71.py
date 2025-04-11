def solve():
    a = int(input())

    if a == 1:
        print(1)
        return

    count = 0
    i = 2
    while a >= i:
        a -= i
        count += 1
        i += 1

    print(count)

solve()