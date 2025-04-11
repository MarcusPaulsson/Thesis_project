def is_valid_flag(n, m, flag):
    colors = set()
    
    # Check for horizontal stripes
    stripe_height = n // 3
    if n % 3 != 0:
        return "NO"
    
    for i in range(3):
        stripe = flag[i * stripe_height:(i + 1) * stripe_height]
        first_row_color = stripe[0][0]
        
        # Check if all rows in the stripe are the same color
        if any(row != first_row_color * m for row in stripe):
            return "NO"
        
        colors.add(first_row_color)
    
    return "YES" if len(colors) == 3 else "NO"

def main():
    n, m = map(int, input().split())
    flag = [input().strip() for _ in range(n)]
    
    result = is_valid_flag(n, m, flag)
    print(result)

if __name__ == "__main__":
    main()