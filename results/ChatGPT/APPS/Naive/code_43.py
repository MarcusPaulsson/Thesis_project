import sys
import math

def minimal_angle_pair(vectors):
    angles = []
    
    for i, (x, y) in enumerate(vectors):
        angle = math.atan2(y, x)
        angles.append((angle, i + 1))  # Store angle and index (1-based)

    # Sort angles
    angles.sort()

    # Add the first angle + 2π to handle the circular nature
    angles.append((angles[0][0] + 2 * math.pi, angles[0][1]))

    min_angle = float('inf')
    min_pair = (0, 0)

    # Find the minimal angle between consecutive vectors
    for i in range(len(angles) - 1):
        angle1, index1 = angles[i]
        angle2, index2 = angles[i + 1]
        angle_diff = angle2 - angle1
        
        if angle_diff < min_angle:
            min_angle = angle_diff
            min_pair = (index1, index2)

    return min_pair

def main():
    n = int(sys.stdin.readline().strip())
    vectors = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    
    result = minimal_angle_pair(vectors)
    print(result[0], result[1])

if __name__ == "__main__":
    main()