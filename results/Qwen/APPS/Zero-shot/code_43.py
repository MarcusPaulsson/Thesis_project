import math
import sys

def main():
    n = int(sys.stdin.readline())
    vectors = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        vectors.append((x, y))
    
    min_angle = math.pi
    min_pair = (0, 0)
    for i in range(n):
        for j in range(i+1, n):
            angle = math.acos((vectors[i][0]*vectors[j][0] + vectors[i][1]*vectors[j][1]) / (math.sqrt(vectors[i][0]**2 + vectors[i][1]**2) * math.sqrt(vectors[j][0]**2 + vectors[j][1]**2))
            if angle < min_angle:
                min_angle = angle
                min_pair = (i+1, j+1)
    
    print(min_pair[0], min_pair[1])

if __name__ == "__main__":
    main()