def solve():
    a, b, c = map(int, input().split())

    for num_ebony in range(c // a + 1):
        remaining_damage = c - num_ebony * a
        if remaining_damage >= 0 and remaining_damage % b == 0:
            print("Yes")
            return

    print("No")

solve()