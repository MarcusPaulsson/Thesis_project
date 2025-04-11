n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Check if any rating has changed
rated = any(a != b for a, b in ratings)

if rated:
    print("rated")
else:
    # Check if the standings are in non-increasing order of ratings
    for i in range(1, n):
        if ratings[i-1][0] < ratings[i][0]:
            print("unrated")
            break
    else:
        print("maybe")