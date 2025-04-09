n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

def check_flag(flag):
    if n % 3 == 0:
        stripe_height = n // 3
        stripes = [flag[i * stripe_height:(i + 1) * stripe_height] for i in range(3)]
        colors = set()
        for stripe in stripes:
            if len(set(stripe[0])) != 1 or len(set(stripe)) != 1:
                return "NO"
            colors.add(stripe[0][0])
        return "YES" if len(colors) == 3 else "NO"
    elif m % 3 == 0:
        stripe_width = m // 3
        stripes = [flag[i] for i in range(n)]
        colors = set()
        for j in range(3):
            stripe_color = ''.join(stripes[j * stripe_width][i] for i in range(m))
            if len(set(stripe_color)) != 1 or any(stripes[i][j * stripe_width:j * stripe_width + stripe_width].count(stripe_color[0]) != stripe_width for i in range(n)):
                return "NO"
            colors.add(stripe_color[0])
        return "YES" if len(colors) == 3 else "NO"
    else:
        return "NO"

print(check_flag(flag))