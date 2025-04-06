def is_valid_flag(n, m, flag):
    # Check for horizontal stripes
    if n % 3 == 0:
        stripe_height = n // 3
        colors = set()
        for i in range(3):
            stripe = flag[i * stripe_height:(i + 1) * stripe_height]
            if all(row == stripe[0] for row in stripe) and stripe[0][0] not in colors:
                colors.add(stripe[0][0])
            else:
                return "NO"
        return "YES" if len(colors) == 3 else "NO"
    
    # Check for vertical stripes
    if m % 3 == 0:
        stripe_width = m // 3
        colors = set()
        for i in range(3):
            stripe = [row[i * stripe_width:(i + 1) * stripe_width] for row in flag]
            if all(row == stripe[0] for row in stripe) and stripe[0][0] not in colors:
                colors.add(stripe[0][0])
            else:
                return "NO"
        return "YES" if len(colors) == 3 else "NO"
    
    return "NO"

# Input reading
n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

# Output the result
print(is_valid_flag(n, m, flag))