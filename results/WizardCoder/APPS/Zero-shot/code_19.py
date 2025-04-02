t = int(input())

def min_subscriptions(n, k, d):
    # Create an array to store the frequency of each show in the schedule
    freq = [0] * (k+1)
    for i in range(n):
        freq[a[i]] += 1
    
    # Count the number of shows that have at least one episode on d consecutive days
    count = 0
    for f in freq:
        if f >= d:
            count += 1
    
    return min(k-count, count)

for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_subscriptions(n, k, d))