import sys
import math

def find_min_angle_pair(vectors):
    angles = []
    
    # Calculate angles and their indices
    for idx, (x, y) in enumerate(vectors):
        angle = math.atan2(y, x)
        angles.append((angle, idx + 1))  # store 1-based index

    # Sort angles
    angles.sort()

    # Add the first angle + 2π to handle the circular nature
    angles.append((angles[0][0] + 2 * math.pi, angles[0][1]))

    min_angle = float('inf')
    min_pair = None

    # Compare adjacent angles to find the minimal angle
    for i in range(len(angles) - 1):
        angle1, idx1 = angles[i]
        angle2, idx2 = angles[i + 1]
        delta_angle = angle2 - angle1

        if delta_angle < min_angle:
            min_angle = delta_angle
            min_pair = (idx1, idx2)

    return min_pair

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    vectors = [tuple(map(int, line.split())) for line in data[1:n + 1]]

    result = find_min_angle_pair(vectors)
    print(result[0], result[1])