def solve():
    n = int(input())
    ratings = []
    for _ in range(n):
        ratings.append(list(map(int, input().split())))

    rating_changed = False
    for before, after in ratings:
        if before != after:
            rating_changed = True
            break

    if rating_changed:
        print("rated")
        return

    sorted_correctly = True
    for i in range(n - 1):
        if ratings[i][0] < ratings[i + 1][0]:
            sorted_correctly = False
            break

    if not sorted_correctly:
        print("unrated")
    else:
        print("maybe")

solve()