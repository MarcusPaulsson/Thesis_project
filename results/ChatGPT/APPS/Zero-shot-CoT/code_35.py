n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

def is_valid_flag(flag, n, m):
    colors = set()
    stripe_height = n // 3
    
    if n % 3 != 0:
        return "NO"
    
    for i in range(3):
        stripe = flag[i * stripe_height:(i + 1) * stripe_height]
        if len(set(stripe)) != 1 or stripe[0][0] not in 'RGB':
            return "NO"
        colors.add(stripe[0][0])
    
    return "YES" if len(colors) == 3 else "NO"

print(is_valid_flag(flag, n, m))