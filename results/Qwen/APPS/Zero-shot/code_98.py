import math

def min_moves(N):
    return int(math.log2(N)) + 1

N = int(input())
print(min_moves(N))