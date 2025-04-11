def is_valid_flag(n, m, field):
    if n % 3 != 0:
        return "NO"
    
    stripe_height = n // 3
    colors = set()
    
    # Check for horizontal stripes
    for i in range(3):
        stripe_color = field[i * stripe_height][0]
        if stripe_color not in 'RGB' or stripe_color in colors:
            return "NO"
        colors.add(stripe_color)
        for j in range(stripe_height):
            if field[i * stripe_height + j] != stripe_color * m:
                return "NO"
    
    return "YES" if len(colors) == 3 else "NO"

def main():
    n, m = map(int, input().split())
    field = [input().strip() for _ in range(n)]
    
    result = is_valid_flag(n, m, field)
    print(result)

if __name__ == "__main__":
    main()