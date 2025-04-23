def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    max_beauty = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            temp_a = a[:]
            for k in range(i, j):
                temp_a[k] *= x

            current_beauty = 0
            max_so_far = 0
            for val in temp_a:
                current_beauty += val
                if current_beauty < 0:
                    current_beauty = 0
                max_so_far = max(max_so_far, current_beauty)
            max_beauty = max(max_beauty, max_so_far)

    print(max_beauty)

solve()