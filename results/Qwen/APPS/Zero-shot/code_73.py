def can_complete_wall(n, a):
    min_height = min(a)
    max_height = max(a)
    if (max_height - min_height) % 2 == 0:
        return "YES"
    else:
        return "NO"

n = int(input())
a = list(map(int, input().split()))
print(can_complete_wall(n, a))