n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Check if any participant's rating has changed
if any(a != b for a, b in ratings):
    print("rated")
else:
    # Check if the ratings are in non-increasing order
    if any(ratings[i][0] < ratings[i + 1][0] for i in range(n - 1)):
        print("unrated")
    else:
        print("maybe")