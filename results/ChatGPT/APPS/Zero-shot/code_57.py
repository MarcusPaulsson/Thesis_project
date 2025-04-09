def fill_gift_preferences(n, f):
    # Track who has received a gift
    gift_received = set(f_i for f_i in f if f_i != 0)
    
    # Friends who don't know whom to give the gift to
    unknown_givers = [i + 1 for i in range(n) if f[i] == 0]
    
    # Friends who are not receiving gifts
    all_friends = set(range(1, n + 1))
    not_giving_gifts = all_friends - gift_received
    
    # Create a list of pairs of unknown givers and not giving gifts
    result = f[:]
    
    for giver in unknown_givers:
        for receiver in not_giving_gifts:
            if giver != receiver:  # Ensure no one gives a gift to themselves
                result[giver - 1] = receiver
                not_giving_gifts.remove(receiver)  # Remove the receiver from available ones
                break

    print(" ".join(map(str, result)))

# Input reading
n = int(input())
f = list(map(int, input().split()))

fill_gift_preferences(n, f)