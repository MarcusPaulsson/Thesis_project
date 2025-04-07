n = int(input())
participants = [tuple(map(int, input().split())) for _ in range(n)]

# Check if any participant's rating has changed
rated = any(a != b for a, b in participants)

# Check if participants are in non-increasing order by their pre-round ratings
unrated = any(participants[i][0] < participants[i + 1][0] for i in range(n - 1))

if rated:
    print("rated")
elif unrated:
    print("unrated")
else:
    print("maybe")