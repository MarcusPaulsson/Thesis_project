import math
import sys

def minimal_angle_pair(n, vectors):
    # Calculate angles and their original indices
    angles = [(math.atan2(y, x), i + 1) for i, (x, y) in enumerate(vectors)]
    
    # Sort angles
    angles.sort(key=lambda item: item[0])

    # Initialize variables to track minimum angle and corresponding indices
    min_angle = float('inf')
    min_pair = (0, 0)

    # Check angles between consecutive vectors and wrap around to the beginning
    for i in range(n):
        j = (i + 1) % n
        angle1, index1 = angles[i]
        angle2, index2 = angles[j]
        
        # Calculate non-oriented angle
        non_oriented_angle = abs(angle2 - angle1)
        if non_oriented_angle > math.pi:
            non_oriented_angle = 2 * math.pi - non_oriented_angle
        
        # Update minimum angle and pair if found
        if non_oriented_angle < min_angle:
            min_angle = non_oriented_angle
            min_pair = (index1, index2)

    return min_pair

if __name__ == "__main__":
    input_data = sys.stdin.read
    data = input_data().strip().splitlines()
    
    n = int(data[0])
    vectors = [tuple(map(int, line.split())) for line in data[1:n + 1]]
    
    result = minimal_angle_pair(n, vectors)
    print(result[0], result[1])