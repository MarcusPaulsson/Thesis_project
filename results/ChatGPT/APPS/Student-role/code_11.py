def min_grid_area(commands):
    # Count the number of each command
    w = commands.count('W')
    s = commands.count('S')
    a = commands.count('A')
    d = commands.count('D')
    
    # Calculate the width and height of the grid
    width = (a > 0) + (d > 0)  # 1 if A or D is present
    height = (w > 0) + (s > 0)  # 1 if W or S is present
    
    # Original area without extra commands
    original_area = width * height
    
    # Area with one extra command
    min_area = original_area
    
    # Check if we can reduce the area by adding an extra command
    if original_area == 1:
        # If the area is already 1, adding any command will still keep it as 1
        return 1
    
    # If area is 2 or more, we can potentially add one command to reduce the area
    if width == 1 and height == 1:
        # If we have both directions (W/S and A/D), we can potentially go to 2
        min_area = 2
    else:
        # If we already have width or height as 2, we can keep it as is
        min_area = min(min_area, 2)

    return min_area

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        commands = data[i].strip()
        result = min_grid_area(commands)
        results.append(result)
        
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()