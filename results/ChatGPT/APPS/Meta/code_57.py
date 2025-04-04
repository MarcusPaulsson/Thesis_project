def fill_gift_values(n, f):
    # Create a list to hold the final gift values
    nf = f[:]
    
    # Find all the friends that have a known gift
    known_givers = set(fi for fi in f if fi != 0)
    
    # Find all the friends that have an unknown gift (f_i = 0)
    unknown_givers = [i + 1 for i in range(n) if f[i] == 0]
    
    # Find all the friends that are targeted to receive a gift
    known_receivers = set(range(1, n + 1)) - known_givers
    
    # Fill in the unknown gift values
    for i in range(len(unknown_givers)):
        # The current unknown giver
        giver = unknown_givers[i]
        
        # Select a receiver from the known receivers
        receiver = known_receivers.pop()
        
        # Assign the gift
        nf[giver - 1] = receiver
        
        # If there are still unknown givers, put this receiver in the known givers
        known_givers.add(receiver)
        
        # If there are still unknown receivers, we might need to re-add this to the pool
        if len(known_receivers) == 0:
            known_receivers.add(giver)
            break
    
    # Now, fill in any remaining 0s ensuring no one gives a gift to themselves
    for i in range(n):
        if nf[i] == 0:
            nf[i] = known_receivers.pop()
    
    return nf

# Input reading
n = int(input())
f = list(map(int, input().split()))

# Get the result and print it
result = fill_gift_values(n, f)
print(' '.join(map(str, result)))