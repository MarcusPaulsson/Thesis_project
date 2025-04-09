import sys
import math

def main():
    input_data = sys.stdin.read().strip().splitlines()
    n = int(input_data[0])
    vectors = []

    for i in range(1, n + 1):
        x, y = map(int, input_data[i].split())
        angle = math.atan2(y, x)
        vectors.append((angle, i))

    # Sort vectors by angle
    vectors.sort()

    min_angle = float('inf')
    answer = (0, 0)

    # Check the minimal angle between consecutive vectors
    for i in range(n):
        current_angle = vectors[i][0]
        next_angle = vectors[(i + 1) % n][0]
        
        # Calculate the angle difference
        angle_diff = (next_angle - current_angle) % (2 * math.pi)
        if angle_diff > math.pi:
            angle_diff = 2 * math.pi - angle_diff

        if angle_diff < min_angle:
            min_angle = angle_diff
            answer = (vectors[i][1], vectors[(i + 1) % n][1])

    print(answer[0], answer[1])

if __name__ == "__main__":
    main()