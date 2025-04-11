def fill_gift_choices(n, f):
    # Create a list to store the final gift choices
    nf = f[:]
    
    # Find the friends who have not chosen anyone (f_i = 0)
    unchosen = [i + 1 for i in range(n) if nf[i] == 0]
    
    # Find the friends who are already chosen by someone
    chosen = set(f_i for f_i in nf if f_i != 0)
    
    # Find the friends who are not chosen by anyone
    not_chosen = [i + 1 for i in range(1, n + 1) if i not in chosen]
    
    # Fill in the unchosen friends
    for i in range(len(unchosen)):
        nf[unchosen[i] - 1] = not_chosen[i]
    
    return nf

# Read input
n = int(input())
f = list(map(int, input().split()))

# Get the result
result = fill_gift_choices(n, f)

# Print the result
print(' '.join(map(str, result)))