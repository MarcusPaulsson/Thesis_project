def assign_gifts(n, friends):
    # Create a list to store the final gift assignments
    final_gifts = friends[:]
    
    # Identify unassigned friends (f_i = 0) and assigned gifts
    unassigned = []
    assigned = set()
    
    for i in range(n):
        if final_gifts[i] == 0:
            unassigned.append(i + 1)  # Store 1-based index
        else:
            assigned.add(final_gifts[i])
    
    # Determine gifts that need to be assigned
    not_assigned_gifts = [i for i in range(1, n + 1) if i not in assigned]
    
    # Assign gifts to unassigned friends
    for i in range(len(unassigned)):
        friend_index = unassigned[i]
        gift_index = not_assigned_gifts[i]
        
        # Ensure that the gift is not assigned to themselves
        if gift_index == friend_index:
            # If gift_index is the same as friend_index, swap with the next one
            if i + 1 < len(not_assigned_gifts):
                gift_index = not_assigned_gifts[i + 1]
                not_assigned_gifts[i + 1] = not_assigned_gifts[i]
        
        final_gifts[friend_index - 1] = gift_index
    
    return final_gifts

# Read input
n = int(input())
friends = list(map(int, input().split()))

# Get the result
result = assign_gifts(n, friends)

# Print the result
print(' '.join(map(str, result)))