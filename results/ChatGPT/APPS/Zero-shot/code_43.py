import sys
import math

def angle_with_x_axis(x, y):
    return math.atan2(y, x)

def main():
    n = int(sys.stdin.readline().strip())
    vectors = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    
    angles = [(angle_with_x_axis(x, y), i + 1) for i, (x, y) in enumerate(vectors)]
    angles.sort()
    
    min_angle = float('inf')
    min_index_pair = (0, 0)
    
    for i in range(n):
        a1, index1 = angles[i]
        a2, index2 = angles[(i + 1) % n]
        
        angle_diff = abs(a2 - a1)
        if angle_diff > math.pi:
            angle_diff = 2 * math.pi - angle_diff
        
        if angle_diff < min_angle:
            min_angle = angle_diff
            min_index_pair = (index1, index2)
    
    print(min_index_pair[0], min_index_pair[1])

if __name__ == "__main__":
    main()