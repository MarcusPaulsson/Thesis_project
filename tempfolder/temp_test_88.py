def is_possible_visible_pips(x):
    # The minimum visible pips for a single die is 14 (1 on top, 3+2+4+5 on the sides)
    # The maximum visible pips for a single die is 20 (6 on top, 1+2+3+4 on the sides)
    # For n dice, the visible pips can be calculated as:
    # visible_pips = n * 14 + k (where k is the sum of the top faces of the n dice)
    # and k can vary from 1 to 6 for each die.

    # Therefore, the total visible pips can be expressed as:
    # x = n * 14 + k
    # where k can take any value from n (minimum) to 6 * n (maximum).
    # This means k can be expressed as:
    # k = x - n * 14
    # This must also satisfy:
    # n <= k <= 6 * n
    # This simplifies to:
    # n <= x - n * 14 <= 6 * n
    
    # Rearranging gives us:
    # n <= x - 14n <= 6n
    # which means:
    # 15n <= x <= 20n
    # Thus, we need to find if there exists an integer n such that:
    # n <= x / 15 and x / 20 <= n
    
    # This gives us:
    # x / 20 <= n <= x / 15
    # We can check this for all possible n values.

    # Check for possible n
    for n in range(1, 10**18):
        if n * 15 <= x <= n * 20:
            return True
        if n * 20 > x:
            break
    return False

# Reading input
t = int(input())
x_values = list(map(int, input().split()))

# Output results for each x_i
results = []
for x in x_values:
    if is_possible_visible_pips(x):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))