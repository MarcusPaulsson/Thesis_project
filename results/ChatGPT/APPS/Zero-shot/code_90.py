n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Check if any rating has changed
rated = any(a != b for a, b in ratings)

# Check if standings are in non-increasing order of the ratings
ordered = all(ratings[i][0] >= ratings[i + 1][0] for i in range(n - 1))

if rated:
    print("rated")
elif not ordered:
    print("unrated")
else:
    print("maybe")