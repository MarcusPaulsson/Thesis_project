def solve():
    n = int(input())
    ratings = []
    for _ in range(n):
        ratings.append(list(map(int, input().split())))

    changed = False
    for a, b in ratings:
        if a != b:
            changed = True
            break

    if changed:
        print("rated")
        return

    sorted_flag = True
    for i in range(n - 1):
        if ratings[i][0] < ratings[i+1][0]:
            sorted_flag = False
            break

    if not sorted_flag:
        print("unrated")
    else:
        print("maybe")

solve()