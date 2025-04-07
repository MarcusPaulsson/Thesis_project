n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

def is_valid_flag(flag):
    colors = {'R', 'G', 'B'}
    
    # Check for horizontal stripes
    if n % 3 == 0:
        stripe_height = n // 3
        used_colors = set()
        for i in range(3):
            stripe = flag[i * stripe_height:(i + 1) * stripe_height]
            if len(set(stripe)) != 1 or stripe[0][0] not in colors:
                return False
            used_colors.add(stripe[0][0])
        return used_colors == colors
    
    # Check for vertical stripes
    if m % 3 == 0:
        stripe_width = m // 3
        used_colors = set()
        for i in range(3):
            stripe = [row[i * stripe_width:(i + 1) * stripe_width] for row in flag]
            if len(set(stripe)) != 1 or stripe[0][0] not in colors:
                return False
            used_colors.add(stripe[0][0])
        return used_colors == colors
    
    return False

print("YES" if is_valid_flag(flag) else "NO")