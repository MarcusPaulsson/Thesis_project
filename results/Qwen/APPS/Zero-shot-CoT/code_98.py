import math

def min_moves_to_reach_N(N):
    # Find the smallest integer i such that i * i >= N
    i = math.ceil(math.sqrt(N))
    # The minimum number of moves is i - 1 (to move from (1,1) to (i,1)) + (i - j) (to move from (i,1) to (i,j))
    # where j is the largest integer such that i * j <= N
    j = N // i
    return i - 1 + (i - j)

N = int(input())
print(min_moves_to_reach_N(N))