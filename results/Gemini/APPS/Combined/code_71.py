def solve():
    a = int(input())
    total = 0
    count = 0
    i = 1
    while True:
        total += i * (i + 1) // 2
        if total >= a:
            print(count)
            return
        i += 1
        count += 1

solve()