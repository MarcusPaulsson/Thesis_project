import math
T = int(input())
for _ in range(T):
    n = int(input())
    perimeter = math.sqrt(4*n)
    square_side = (perimeter/2)*math.sqrt(2) # since we need to embed the polygon inside a square, the side length of the square will be half the perimeter
    print("{:.6f}".format(square_side))