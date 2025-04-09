n = int(input())
f = list(map(int, input().split()))

# Create a set for the friends who want to give gifts
want_to_give = set(range(1, n + 1)) - {x for x in f if x != 0}

# Create a list for friends who don't know whom to give gifts to
unknown_givers = [i + 1 for i in range(n) if f[i] == 0]

# We will keep track of the available friends who can receive gifts
available_receivers = list(want_to_give)

# Fill the unknown givers
for i in range(len(unknown_givers)):
    giver = unknown_givers[i]
    
    # Find a receiver that is not the giver themselves
    for receiver in available_receivers:
        if receiver != giver:
            f[giver - 1] = receiver
            available_receivers.remove(receiver)
            break

print(' '.join(map(str, f)))