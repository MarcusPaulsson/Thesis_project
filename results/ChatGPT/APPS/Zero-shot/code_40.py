n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Check if the round is rated
for a, b in ratings:
    if a != b:
        print("rated")
        break
else:
    # Check if the round is unrated
    for i in range(n - 1):
        if ratings[i][0] < ratings[i + 1][0]:
            print("unrated")
            break
    else:
        print("maybe")