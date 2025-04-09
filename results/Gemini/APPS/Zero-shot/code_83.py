import math

def solve():
    a, b = map(int, input().split())
    total = a + b
    
    best_perimeter = float('inf')
    
    for height in range(1, int(math.sqrt(total)) + 2):
        if total % height == 0:
            width = total // height
            
            # Case 1: Red forms a rectangle
            for red_height in range(1, int(math.sqrt(a)) + 2):
                if a % red_height == 0:
                    red_width = a // red_height
                    if red_height <= height and red_width <= width:
                        best_perimeter = min(best_perimeter, 2 * (height + width))
                        
            # Case 2: Blue forms a rectangle
            for blue_height in range(1, int(math.sqrt(b)) + 2):
                if b % blue_height == 0:
                    blue_width = b // blue_height
                    if blue_height <= height and blue_width <= width:
                        best_perimeter = min(best_perimeter, 2 * (height + width))
                        
    print(best_perimeter)

solve()