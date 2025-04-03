def calculate_wins(n, a, b):
    # Maximum wins calculation
    max_wins = min(a[0], b[2]) + min(a[1], b[0]) + min(a[2], b[1])

    # Minimum wins calculation
    # First, calculate losses:
    losses = 0
    losses += max(0, b[0] - a[2])  # Bob's rock beats Alice's paper
    losses += max(0, b[1] - a[0])  # Bob's scissors beat Alice's rock
    losses += max(0, b[2] - a[1])  # Bob's paper beats Alice's scissors
    
    # Minimum wins is total rounds minus losses
    min_wins = n - losses

    return min_wins, max_wins

# Input reading
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate results
min_wins, max_wins = calculate_wins(n, a, b)

# Output results
print(min_wins, max_wins)