def is_valid_flag(n, m, flag):
    colors = {'R', 'G', 'B'}
    
    # Check for horizontal stripes
    stripe_height = n // 3
    if n % 3 != 0 or stripe_height == 0:
        return "NO"
    
    used_colors = set()
    for i in range(3):
        stripe_color = flag[i * stripe_height][0]
        if stripe_color not in colors or stripe_color in used_colors:
            return "NO"
        used_colors.add(stripe_color)
        for j in range(stripe_height):
            if flag[i * stripe_height + j] != stripe_color * m:
                return "NO"
    
    return "YES" if len(used_colors) == 3 else "NO"

def main():
    n, m = map(int, input().split())
    flag = [input().strip() for _ in range(n)]
    
    # Check for vertical stripes
    if m % 3 == 0:
        stripe_width = m // 3
        used_colors = set()
        for i in range(3):
            stripe_color = flag[0][i * stripe_width]
            if stripe_color not in {'R', 'G', 'B'} or stripe_color in used_colors:
                print("NO")
                return
            used_colors.add(stripe_color)
            for row in flag:
                if row[i * stripe_width:(i + 1) * stripe_width] != stripe_color * stripe_width:
                    print("NO")
                    return
        print("YES" if len(used_colors) == 3 else "NO")
    else:
        print(is_valid_flag(n, m, flag))

if __name__ == "__main__":
    main()