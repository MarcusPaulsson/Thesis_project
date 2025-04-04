n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

if any(a != b for a, b in ratings):
    print("rated")
elif any(ratings[i][0] < ratings[i+1][0] for i in range(n-1)):
    print("unrated")
else:
    print("maybe")