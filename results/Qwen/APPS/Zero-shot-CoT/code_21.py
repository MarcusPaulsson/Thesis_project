def max_distance(n, a):
    min_pos = a.index(1)
    max_pos = a.index(n)
    distance = abs(min_pos - max_pos)
    
    # Try swapping the minimum element with the last element
    new_min_pos = n - 1
    new_max_pos = max_pos
    if min_pos != new_min_pos:
        new_distance = abs(new_min_pos - new_max_pos)
        if new_distance > distance:
            distance = new_distance
    
    # Try swapping the maximum element with the first element
    new_min_pos = min_pos
    new_max_pos = 0
    if max_pos != new_max_pos:
        new_distance = abs(new_min_pos - new_max_pos)
        if new_distance > distance:
            distance = new_distance
    
    return distance

n = int(input())
a = list(map(int, input().split()))
print(max_distance(n, a))