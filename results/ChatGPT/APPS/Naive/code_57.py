def fill_gift_preferences(n, f):
    # Prepare lists to track givers and takers
    givers = set(range(1, n + 1))  # Set of all friends
    known_gifts = set()  # Friends who have known gift preferences

    # Identify known gifts and available givers
    for i in range(n):
        if f[i] != 0:
            known_gifts.add(f[i])
            givers.discard(i + 1)  # Remove giver from available set
    
    # Available friends who haven't received gifts yet
    available_givers = list(givers)
    giftless_friends = [i + 1 for i in range(n) if f[i] == 0]

    # Assign gifts to those who have 0
    for i in range(len(giftless_friends)):
        friend = giftless_friends[i]
        # We need to assign them a gift from available_givers
        # Ensure not to assign to themselves
        for j in range(len(available_givers)):
            if available_givers[j] != friend:
                f[friend - 1] = available_givers[j]
                available_givers.pop(j)  # Remove the assigned giver
                break

    return f

# Input reading
n = int(input().strip())
f = list(map(int, input().strip().split()))

# Fill the preferences
result = fill_gift_preferences(n, f)

# Output the result
print(" ".join(map(str, result)))