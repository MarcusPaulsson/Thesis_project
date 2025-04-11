n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Check if any rating has changed
rated = any(a != b for a, b in ratings)

if rated:
    print("rated")
else:
    # Check if the standings are in non-increasing order of the initial ratings
    for i in range(n - 1):
        if ratings[i][0] < ratings[i + 1][0]:
            print("unrated")
            break
    else:
        print("maybe")