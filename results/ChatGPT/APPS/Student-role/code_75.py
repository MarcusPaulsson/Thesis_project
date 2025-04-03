import math

def minimum_square_side_length(n):
    # Calculate the radius of the circumcircle of the 2n-gon
    radius = 1 / (2 * math.sin(math.pi / (2 * n)))
    # The side length of the square needed to contain the 2n-gon
    square_side_length = radius * math.sqrt(2)
    return square_side_length

T = int(input())
results = []
for _ in range(T):
    n = int(input())
    results.append(minimum_square_side_length(n))

for result in results:
    print(f"{result:.9f}")