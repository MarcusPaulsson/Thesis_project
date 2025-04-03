def is_possible_visible_pips(x):
    # The minimum visible pips for one die is 14 (1 on top) and maximum is 20 (6 on top)
    # For n dice, the number of visible pips can be calculated as:
    # visible_pips = 14 + 7 * (n - 1), where n is the number of dice.
    # The series produces values: 14, 21, 28, 35, ..., which is 14 + 7k for k >= 0.
    
    if x < 14:
        return False
    # Check if (x - 14) is a multiple of 7
    return (x - 14) % 7 == 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # number of favourite integers
    x_values = list(map(int, data[1:t + 1]))
    
    results = []
    for x in x_values:
        if is_possible_visible_pips(x):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()