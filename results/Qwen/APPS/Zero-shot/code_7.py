import math

def find_empty_day(n, m):
    day = 0
    while n > 0:
        day += 1
        n = n + m - day
    return day

n, m = map(int, input().split())
print(find_empty_day(n, m))