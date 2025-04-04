import sys
import math

def find_min_angle_pair(vectors):
    n = len(vectors)
    angles = []
    
    for i in range(n):
        x, y = vectors[i]
        angle = math.atan2(y, x)
        angles.append((angle, i + 1))

    # Sort by angles
    angles.sort()

    # Add the first angle + 2π to handle the wrap-around case
    angles.append((angles[0][0] + 2 * math.pi, angles[0][1]))

    min_angle = float('inf')
    min_pair = (0, 0)

    for i in range(n):
        angle1, index1 = angles[i]
        angle2, index2 = angles[i + 1]
        
        # Calculate the non-oriented angle
        current_angle = angle2 - angle1
        if current_angle < min_angle:
            min_angle = current_angle
            min_pair = (index1, index2)

    return min_pair

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    vectors = [tuple(map(int, line.split())) for line in data[1:n + 1]]
    
    result = find_min_angle_pair(vectors)
    print(result[0], result[1])

if __name__ == "__main__":
    main()