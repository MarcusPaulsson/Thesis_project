def solve():
    a, b, c = map(int, input().split())

    for i in range(101):
        if a * i > c:
            break
        remaining_damage = c - a * i
        if remaining_damage % b == 0:
            print("Yes")
            return

    print("No")

solve()