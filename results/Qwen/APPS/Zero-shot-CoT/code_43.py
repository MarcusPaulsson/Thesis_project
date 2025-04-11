import math
import sys

def main():
    n = int(sys.stdin.readline())
    vectors = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        angle = math.atan2(y, x)
        vectors.append((angle, i + 1))
    
    vectors.sort()
    
    min_angle = float('inf')
    min_pair = (0, 0)
    
    for i in range(n):
        angle1, index1 = vectors[i]
        angle2, index2 = vectors[(i + 1) % n]
        diff = abs(angle1 - angle2)
        if diff > math.pi:
            diff = 2 * math.pi - diff
        if diff < min_angle:
            min_angle = diff
            min_pair = (index1, index2)
    
    print(min_pair[0], min_pair[1])

if __name__ == "__main__":
    main()