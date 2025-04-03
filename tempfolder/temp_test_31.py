def calculate_time(path):
    visited_segments = set()
    x, y = 0, 0
    total_time = 0

    for move in path:
        if move == 'N':
            new_x, new_y = x, y + 1
        elif move == 'S':
            new_x, new_y = x, y - 1
        elif move == 'E':
            new_x, new_y = x + 1, y
        elif move == 'W':
            new_x, new_y = x - 1, y

        segment = (x, y, new_x, new_y) if (x, y) < (new_x, new_y) else (new_x, new_y, x, y)

        if segment in visited_segments:
            total_time += 1
        else:
            total_time += 5
            visited_segments.add(segment)

        x, y = new_x, new_y

    return total_time

t = int(input())
for _ in range(t):
    path = input().strip()
    print(calculate_time(path))