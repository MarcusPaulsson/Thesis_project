def fill_gift_values(n, f):
    # Create a set of friends who are already receiving gifts
    received = {fi for fi in f if fi != 0}
    
    # Find friends who are not receiving gifts
    not_received = [i for i in range(1, n + 1) if i not in received]
    
    # Fill in the zeros in f
    result = f[:]
    zero_indices = [i for i in range(n) if f[i] == 0]
    
    for idx, zero_index in enumerate(zero_indices):
        # Assign the next friend who is not receiving a gift
        result[zero_index] = not_received[idx]
    
    # Ensure no one gives a gift to themselves
    for i in range(n):
        if result[i] == i + 1:
            # Swap with the last not_received friend
            result[i], result[zero_indices[-1]] = result[zero_indices[-1]], result[i]
            break
    
    return result

# Read input
n = int(input())
f = list(map(int, input().split()))

# Get the result and print it
result = fill_gift_values(n, f)
print(' '.join(map(str, result)))