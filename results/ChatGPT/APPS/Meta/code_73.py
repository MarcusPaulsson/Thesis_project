def can_complete_wall(n, heights):
    max_height = max(heights)
    for h in heights:
        if h < max_height and (h + 1) not in heights:
            return "NO"
    return "YES"

n = int(input())
heights = list(map(int, input().split()))
print(can_complete_wall(n, heights))