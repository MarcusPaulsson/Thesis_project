def fill_gift_list(n, f):
    # Find the friends who want to give gifts (f_i != 0)
    givers = set(range(1, n + 1)) - set(f)
    
    # Find the friends who are not receiving gifts (f_i = 0)
    receivers = [i + 1 for i in range(n) if f[i] == 0]
    
    # Create a mapping for the final gift list
    for i in range(len(receivers)):
        # Assign each receiver a giver, ensuring no one gives a gift to themselves
        for giver in givers:
            if giver != receivers[i]:
                f[receivers[i] - 1] = giver
                givers.remove(giver)
                break
    
    print(" ".join(map(str, f)))

# Input reading
n = int(input())
f = list(map(int, input().split()))

fill_gift_list(n, f)