import math

def minimum_square_side_length(n):
    # Calculate the radius of the circumscribed circle of the 2n-gon
    radius = 1 / (2 * math.sin(math.pi / (2 * n)))
    # The side of the square needed to embed the 2n-gon
    side_length = radius * math.sqrt(2)
    return side_length

T = int(input())
results = []
for _ in range(T):
    n = int(input())
    result = minimum_square_side_length(n)
    results.append(result)

for res in results:
    print(f"{res:.9f}")