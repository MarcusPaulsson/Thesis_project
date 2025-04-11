def assign_gifts(n, friends):
    # Create a list to store the final gift assignments
    final_gifts = friends[:]
    
    # Find the friends who want to give gifts (f_i != 0)
    givers = set(i + 1 for i in range(n) if final_gifts[i] != 0)
    
    # Find the friends who are not assigned a gift (f_i == 0)
    receivers = [i + 1 for i in range(n) if final_gifts[i] == 0]
    
    # Find the friends who are already assigned gifts
    assigned = set(final_gifts) - {0}
    
    # Find the friends who are not assigned gifts yet
    unassigned = set(range(1, n + 1)) - assigned
    
    # Create a mapping of unassigned friends to receivers
    unassigned = list(unassigned)
    
    # Fill in the zeros in the final_gifts
    for i in range(len(receivers)):
        # Assign the gift to the receiver from the unassigned list
        final_gifts[receivers[i] - 1] = unassigned[i]
    
    # Ensure no one gives a gift to themselves
    for i in range(n):
        if final_gifts[i] == i + 1:
            # Swap with the next friend to avoid self-gifting
            next_index = (i + 1) % n
            final_gifts[i], final_gifts[next_index] = final_gifts[next_index], final_gifts[i]
    
    return final_gifts

# Input reading
n = int(input())
friends = list(map(int, input().split()))

# Get the result and print it
result = assign_gifts(n, friends)
print(" ".join(map(str, result)))