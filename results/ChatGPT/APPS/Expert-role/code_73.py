def can_complete_wall(n, heights):
    max_height = max(heights)
    total_bricks_needed = 0
    total_bricks_available = 0

    for height in heights:
        total_bricks_needed += max_height - height
        total_bricks_available += height

    if total_bricks_needed <= total_bricks_available:
        return "YES"
    else:
        return "NO"

n = int(input())
heights = list(map(int, input().split()))
print(can_complete_wall(n, heights))