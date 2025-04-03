def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

def reachable_count(n):
    reachable = set()
    queue = [n]
    
    while queue:
        current = queue.pop()
        if current not in reachable:
            reachable.add(current)
            next_value = f(current)
            if next_value not in reachable:
                queue.append(next_value)
            for i in range(1, 10):
                next_to_add = current - i
                if next_to_add > 0 and next_to_add not in reachable:
                    queue.append(next_to_add)
    
    return len(reachable)

n = int(input())
print(reachable_count(n))