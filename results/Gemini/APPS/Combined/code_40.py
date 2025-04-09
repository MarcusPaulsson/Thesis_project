def solve():
    n = int(input())
    ratings = []
    for _ in range(n):
        ratings.append(list(map(int, input().split())))

    rating_changed = any(a != b for a, b in ratings)

    if rating_changed:
        print("rated")
        return

    is_sorted = all(ratings[i][0] >= ratings[i+1][0] for i in range(n - 1))

    if not is_sorted:
        print("unrated")
    else:
        print("maybe")

solve()