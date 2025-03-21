def min_area_after_insertion(s):
    # Count the moves in each direction
    up = s.count('W')
    down = s.count('S')
    left = s.count('A')
    right = s.count('D')
    
    # Calculate the initial area of the grid
    height = up + down + 1
    width = left + right + 1
    min_area = height * width
    
    # Check if inserting an extra command can reduce the area
    # We will consider each of the four possible insertions
    for extra in ['W', 'S', 'A', 'D']:
        # Create a new counts based on the extra command
        if extra == 'W':
            new_height = (up + 1) + down + 1
        elif extra == 'S':
            new_height = up + (down + 1) + 1
        else:
            new_height = up + down + 1
        
        if extra == 'A':
            new_width = (left + 1) + right + 1
        elif extra == 'D':
            new_width = left + (right + 1) + 1
        else:
            new_width = left + right + 1
        
        new_area = new_height * new_width
        min_area = min(min_area, new_area)
    
    return min_area

T = int(input())
results = []

for _ in range(T):
    s = input().strip()
    results.append(min_area_after_insertion(s))

print('\n'.join(map(str, results)))