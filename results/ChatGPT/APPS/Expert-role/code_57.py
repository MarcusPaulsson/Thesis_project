def fill_gift_choices(n, f):
    # Find the indices of friends who don't know whom to give gifts to (f_i = 0)
    unknown_indices = [i for i in range(n) if f[i] == 0]
    
    # Create a set of all possible friends (1 to n)
    all_friends = set(range(1, n + 1))
    
    # Find the set of friends who already have a known gift target
    known_gift_targets = set(f[i] for i in range(n) if f[i] != 0)
    
    # Find the remaining friends who need to receive gifts
    remaining_friends = list(all_friends - known_gift_targets)
    
    # Fill in the unknowns
    for i in range(len(unknown_indices)):
        friend_idx = unknown_indices[i]
        # Assign the gift target ensuring no one gives a gift to themselves
        f[friend_idx] = remaining_friends[i]

    return f

# Input reading
n = int(input())
f = list(map(int, input().split()))

# Process and output the result
result = fill_gift_choices(n, f)
print(" ".join(map(str, result)))