n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

rated = False
unrated = False

for a, b in ratings:
    if a != b:
        rated = True
        break

if rated:
    print("rated")
else:
    for i in range(n - 1):
        if ratings[i][0] < ratings[i + 1][0]:
            unrated = True
            break

    if unrated:
        print("unrated")
    else:
        print("maybe")