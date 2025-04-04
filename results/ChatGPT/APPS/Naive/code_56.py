def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

def reachable_count(n):
    visited = set()
    queue = [n]
    
    while queue:
        current = queue.pop()
        if current not in visited:
            visited.add(current)
            next_value = f(current)
            if next_value not in visited:
                queue.append(next_value)
            # Also add the next number without applying f
            if current + 1 not in visited:
                queue.append(current + 1)

    return len(visited)

n = int(input().strip())
print(reachable_count(n))