def calculate_area(s):
    # Count movements in each direction
    up = s.count('W')
    down = s.count('S')
    left = s.count('A')
    right = s.count('D')
    
    # Calculate the width and height of the grid based on movements
    width = right - left + 1
    height = down - up + 1
    
    return width * height

def min_grid_area_with_insert(s):
    # Initial area without any insert
    initial_area = calculate_area(s)
    
    # Check possible areas with one insert
    possible_areas = [initial_area]
    
    for command in 'WASD':
        # Insert the command and calculate new area
        new_s = s + command  # can also be inserted at any position, but end is enough
        new_area = calculate_area(new_s)
        possible_areas.append(new_area)
    
    return min(possible_areas)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        s = data[i]
        min_area = min_grid_area_with_insert(s)
        results.append(min_area)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()