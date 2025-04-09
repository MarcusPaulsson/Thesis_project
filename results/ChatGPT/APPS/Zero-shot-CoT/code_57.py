def assign_gifts(n, friends):
    gift_given = set(f for f in friends if f != 0)
    gift_needed = set(range(1, n + 1)) - gift_given
    zero_indices = [i for i in range(n) if friends[i] == 0]

    for i in range(len(zero_indices)):
        friend_index = zero_indices[i]
        # Find a gift from the remaining that is not the same as the friend's index
        for gift in gift_needed:
            if gift != friend_index + 1:
                friends[friend_index] = gift
                gift_needed.remove(gift)
                break

    return friends

# Read input
n = int(input())
friends = list(map(int, input().split()))

# Get the result
result = assign_gifts(n, friends)

# Print the result
print(' '.join(map(str, result)))