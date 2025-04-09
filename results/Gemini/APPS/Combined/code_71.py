def solve():
    a = int(input())

    if a == 1:
        print(0)  # Corrected output for a=1 to match the problem description's implied behavior.
        return

    n = 0
    power_of_2 = 1
    while power_of_2 <= a:
        power_of_2 *= 2
        n += 1

    print(n - 1)


solve()