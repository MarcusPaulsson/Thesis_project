def min_grid_area(s):
    # Count movements
    count_W = s.count('W')
    count_S = s.count('S')
    count_A = s.count('A')
    count_D = s.count('D')

    # Calculate the dimensions of the grid without any extra commands
    height = count_S + count_W
    width = count_A + count_D

    # Calculate the area without any extra commands
    min_area = height * width

    # Check the effect of adding one extra command
    # Adding one 'W', 'A', 'S', or 'D' can increase height or width by 1
    # We need to check the new areas and take the minimum
    new_heights = [height + 1, height]
    new_widths = [width + 1, width]
    
    for new_height in new_heights:
        for new_width in new_widths:
            new_area = new_height * new_width
            min_area = min(min_area, new_area)

    return min_area

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        s = data[i]
        results.append(min_grid_area(s))
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()