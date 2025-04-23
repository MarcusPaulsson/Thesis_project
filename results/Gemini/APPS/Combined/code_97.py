def solve():
    n = int(input())
    x = list(map(int, input().split()))

    even_count = 0
    odd_count = 0
    for val in x:
        if val % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(min(even_count, odd_count))

solve()