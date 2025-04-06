n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Check if any rating has changed
if any(a != b for a, b in ratings):
    print("rated")
else:
    # Check the order of the ratings
    if all(ratings[i][0] >= ratings[i + 1][0] for i in range(n - 1)):
        print("maybe")
    else:
        print("unrated")