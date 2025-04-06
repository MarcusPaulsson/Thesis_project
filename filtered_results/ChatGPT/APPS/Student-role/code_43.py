import math

def angle_between(v1, v2):
    # Calculate the angle between two vectors using the dot product
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
    magnitude_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
    cos_angle = dot_product / (magnitude_v1 * magnitude_v2)
    return math.acos(cos_angle)

def main():
    n = int(input())
    vectors = []
    
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y, i + 1))  # Save vector with its index

    # Sort vectors by angle
    vectors.sort(key=lambda v: math.atan2(v[1], v[0]))

    min_angle = float('inf')
    min_pair = (0, 0)

    for i in range(n):
        v1 = vectors[i]
        v2 = vectors[(i + 1) % n]  # Wrap around to the first vector
        angle = angle_between(v1[:2], v2[:2])
        
        if angle < min_angle:
            min_angle = angle
            min_pair = (v1[2], v2[2])  # Save indices

    print(min_pair[0], min_pair[1])

if __name__ == "__main__":
    main()