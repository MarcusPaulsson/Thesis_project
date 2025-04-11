n = int(input())
f = list(map(int, input().split()))

# Determine the friends who want to give gifts (those who have f_i != 0)
givers = set(range(1, n + 1)) - set(f)
# Determine the friends who are already assigned to receive gifts
receivers = set(f) - {0}

# Convert givers to a list for easier manipulation
givers = list(givers)

# Fill the unknown values (f_i = 0)
for i in range(n):
    if f[i] == 0:
        # Find a giver who hasn't been assigned yet
        for giver in givers:
            if giver != i + 1 and giver not in receivers:
                f[i] = giver
                receivers.add(giver)
                break

print(' '.join(map(str, f)))