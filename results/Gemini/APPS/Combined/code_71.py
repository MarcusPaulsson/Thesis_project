def solve():
    """
    Reads an integer 'a' from input and finds the largest integer 'n' such that 2^n <= a.
    Prints the value of 'n'.
    """
    a = int(input())

    if a == 1:
        print(1)
        return

    n = 0
    power_of_2 = 1
    while power_of_2 <= a:
        power_of_2 *= 2
        n += 1

    print(n - 1)

solve()