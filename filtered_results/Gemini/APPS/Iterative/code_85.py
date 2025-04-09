def solve():
    A, B = map(int, input().split())

    ans = -1
    for price in range(1, 2000):
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.10)

        if tax_8 == A and tax_10 == B:
            ans = price
            break

    print(ans)

solve()