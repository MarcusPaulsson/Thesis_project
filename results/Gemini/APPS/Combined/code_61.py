def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    a_list = list(a)
    best_a = a_list[:]

    for i in range(n):
        temp_a = a_list[:]
        changed = False
        for j in range(i, n):
            digit = int(a_list[j])
            new_digit = f[digit - 1]
            if new_digit > digit:
                temp_a[j] = str(new_digit)
                changed = True
            elif new_digit < digit:
                break
            else:
                temp_a[j] = str(new_digit)

        if changed:
            break

    print("".join(temp_a))

solve()