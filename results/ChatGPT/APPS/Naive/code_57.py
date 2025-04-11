def fill_gift_preferences(n, f):
    # Create a list to store the final gift preferences
    nf = f[:]
    
    # Find the friends who have not decided whom to give gifts to
    undecided = [i + 1 for i in range(n) if f[i] == 0]
    
    # Find the friends who are already chosen as gift recipients
    chosen = set(fi for fi in f if fi != 0)
    
    # Find the friends who are not chosen by anyone
    not_chosen = [i + 1 for i in range(1, n + 1) if i not in chosen]
    
    # Fill in the undecided friends
    for i in range(len(undecided)):
        giver = undecided[i]
        receiver = not_chosen[i]
        
        # Ensure that the giver does not give a gift to themselves
        if giver == receiver:
            # If they are the same, swap with the next one
            if i + 1 < len(not_chosen):
                receiver = not_chosen[i + 1]
                not_chosen[i + 1] = not_chosen[i]  # Swap to maintain the list
            else:
                receiver = not_chosen[i - 1]  # Use the previous one if at the end
        
        nf[giver - 1] = receiver
    
    return nf

# Read input
n = int(input())
f = list(map(int, input().split()))

# Get the result
result = fill_gift_preferences(n, f)

# Print the result
print(' '.join(map(str, result)))