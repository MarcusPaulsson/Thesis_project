import math

def solve():
    n = int(input())
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y))

    def angle(v):
        return math.atan2(v[1], v[0])

    angles_with_indices = []
    for i in range(n):
        angles_with_indices.append((angle(vectors[i]), i + 1))

    angles_with_indices.sort()

    min_angle_diff = float('inf')
    best_pair = None

    for i in range(n - 1):
        angle_diff = angles_with_indices[i+1][0] - angles_with_indices[i][0]
        if angle_diff < min_angle_diff:
            min_angle_diff = angle_diff
            best_pair = (angles_with_indices[i][1], angles_with_indices[i+1][1])

    # Compare the angle between the last and first vectors
    angle_diff = angles_with_indices[0][0] - angles_with_indices[-1][0] + 2 * math.pi
    angle_diff = min(angle_diff, 2 * math.pi - angle_diff)

    
    angle_diff_direct = angles_with_indices[0][0] + (2 * math.pi - angles_with_indices[-1][0])
    angle_diff_reverse = angles_with_indices[-1][0] - angles_with_indices[0][0]
    angle_diff = min(angle_diff_direct, 2 * math.pi - angle_diff_direct)

    if angle_diff < min_angle_diff:
        min_angle_diff = angle_diff
        best_pair = (angles_with_indices[-1][1], angles_with_indices[0][1])

    print(best_pair[0], best_pair[1])

solve()