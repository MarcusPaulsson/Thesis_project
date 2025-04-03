def is_possible_visible_pips(x):
    # The minimum number of visible pips for 1 die is 14 (when 6 is at the bottom)
    # The maximum number of visible pips for 1 die is 20 (when 1 is at the top)
    # For n dice, the visible pips can be calculated as follows:
    # Min visible pips when n dice: 14 + 5*(n-1) = 9 + 5n (the 5n comes from each die contributing 5 pips on the sides)
    # Max visible pips when n dice: 20 + 5*(n-1) = 15 + 5n
    # Therefore, the range of visible pips for n dice is [9 + 5n, 15 + 5n]

    # We want to check if x can be expressed as:
    # x = 9 + 5n + k where k is in [0, 6] (because the top die can show 1 to 6)
    # Thus x can be expressed as: x - 9 = 5n + k with k in [0, 6]
    # Therefore, for some integer n, (x - 9 - k) must be divisible by 5.

    if x < 9:
        return False
    
    x_minus_9 = x - 9
    return (x_minus_9 % 5) in range(7)  # k can be 0 to 6

t = int(input())
x_values = list(map(int, input().split()))

results = []
for x in x_values:
    if is_possible_visible_pips(x):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))