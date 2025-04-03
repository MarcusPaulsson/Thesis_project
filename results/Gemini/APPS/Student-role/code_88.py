def solve():
    t = int(input())
    x = list(map(int, input().split()))

    for target in x:
        if target < 14:
            print("NO")
        elif target % 14 >= 1 and target % 14 <= 6:
            print("YES")
        else:
            print("NO")

solve()