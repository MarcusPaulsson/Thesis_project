def solve():
    n, m = map(int, input().split())
    count = 0
    for x in range(1, n + 1):
        rem_x = x % 5
        needed_rem_y = (5 - rem_x) % 5
        
        if needed_rem_y == 0:
            count += m // 5
            if m % 5 != 0:
                count += 1
        else:
            count += m // 5
            if m % 5 >= needed_rem_y:
                count += 1
    print(count)

solve()