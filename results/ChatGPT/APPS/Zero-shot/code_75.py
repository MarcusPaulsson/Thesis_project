import math

def min_square_side_length(n):
    # Calculate the radius of the circumcircle for the 2n-gon
    R = 1 / (2 * math.sin(math.pi / (2 * n)))
    # The side length of the square will be the diameter of the circumcircle
    return 2 * R

T = int(input())
results = []
for _ in range(T):
    n = int(input())
    side_length = min_square_side_length(n)
    results.append(f"{side_length:.9f}")

print("\n".join(results))