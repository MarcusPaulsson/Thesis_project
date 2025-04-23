import sys
import math

def minimal_angle_pair(vectors):
    n = len(vectors)
    angles = []

    for i, (x, y) in enumerate(vectors):
        angle = math.atan2(y, x)
        angles.append((angle, i + 1))  # Store angle and index (1-based)

    # Sort angles
    angles.sort()

    # To handle the circular nature, append the first angle + 2π
    angles.append((angles[0][0] + 2 * math.pi, angles[0][1]))

    min_angle = float('inf')
    min_pair = (0, 0)

    for i in range(n):
        angle1, index1 = angles[i]
        angle2, index2 = angles[i + 1]
        angle_diff = angle2 - angle1

        if angle_diff < min_angle:
            min_angle = angle_diff
            min_pair = (index1, index2)

    return min_pair

if __name__ == "__main__":
    input_data = sys.stdin.read
    data = input_data().splitlines()
    n = int(data[0])
    vectors = [tuple(map(int, line.split())) for line in data[1:n + 1]]
    
    result = minimal_angle_pair(vectors)
    print(result[0], result[1])