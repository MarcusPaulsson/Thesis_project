n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Check if any rating has changed
rated = any(a != b for a, b in ratings)

if rated:
    print("rated")
else:
    # Check if standings are valid
    is_valid = all(ratings[i][0] >= ratings[i + 1][0] for i in range(n - 1))
    if is_valid:
        print("maybe")
    else:
        print("unrated")