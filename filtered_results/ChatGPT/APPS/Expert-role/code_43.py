import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    vectors = []
    
    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        angle = math.atan2(y, x)  # Get the angle of the vector
        vectors.append((angle, i + 1))  # Store angle and index (1-based)

    # Sort by angle
    vectors.sort()

    # To find the minimal angle, check adjacent angles and consider the circular nature
    min_angle = float('inf')
    best_pair = (0, 0)

    for i in range(n):
        # Compare with the next vector, considering the circular wrap
        j = (i + 1) % n
        angle1 = vectors[i][0]
        angle2 = vectors[j][0]
        angle_diff = angle2 - angle1

        # Adjust for circular angle
        if angle_diff < 0:
            angle_diff += 2 * math.pi
        
        # Non-oriented angle is the smaller of angle_diff and its supplement
        min_non_oriented_angle = min(angle_diff, 2 * math.pi - angle_diff)

        if min_non_oriented_angle < min_angle:
            min_angle = min_non_oriented_angle
            best_pair = (vectors[i][1], vectors[j][1])

    print(best_pair[0], best_pair[1])

if __name__ == "__main__":
    main()