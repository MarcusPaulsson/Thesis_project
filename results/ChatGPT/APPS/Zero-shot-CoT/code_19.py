def min_subscriptions(t, cases):
    results = []
    for n, k, d, shows in cases:
        # To store the unique shows in the current window of size d
        unique_shows = set()
        # Initialize the first window
        for i in range(d):
            unique_shows.add(shows[i])
        
        # The minimum number of subscriptions needed is the size of the unique set
        min_subs = len(unique_shows)
        
        # Slide the window across the shows
        for i in range(d, n):
            # Remove the show that is left behind and add the new show in the window
            unique_shows.add(shows[i])  # Add the new show
            unique_shows.discard(shows[i - d])  # Remove the show that is sliding out
            
            # Update the minimum subscriptions if current unique shows are less
            min_subs = min(min_subs, len(unique_shows))
        
        results.append(min_subs)
    
    return results


# Input handling
import sys
input = sys.stdin.read

data = input().splitlines()
t = int(data[0])
cases = []
index = 1
for _ in range(t):
    n, k, d = map(int, data[index].split())
    shows = list(map(int, data[index + 1].split()))
    cases.append((n, k, d, shows))
    index += 2

# Get the results
results = min_subscriptions(t, cases)

# Print the results
print('\n'.join(map(str, results)))