def can_distribute(x, n, a, b):
    plates_for_a = (a + x - 1) // x  # Ceil division for pieces of cake A
    plates_for_b = (b + x - 1) // x  # Ceil division for pieces of cake B
    return plates_for_a + plates_for_b <= n

def max_min_pieces(n, a, b):
    left, right = 1, max(a, b)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_distribute(mid, n, a, b):
            answer = mid  # mid is a valid minimum
            left = mid + 1
        else:
            right = mid - 1
            
    return answer

# Input reading
n, a, b = map(int, input().split())
print(max_min_pieces(n, a, b))