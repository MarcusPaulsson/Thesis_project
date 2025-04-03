def solve():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    
    a1 = [0] + a + [l]
    
    left_idx = 0
    right_idx = n + 1
    
    left_pos = a1[left_idx]
    right_pos = a1[right_idx]
    
    left_speed = 1
    right_speed = 1
    
    time = 0
    
    while left_idx < right_idx:
        left_time = (a1[left_idx + 1] - left_pos) / left_speed
        right_time = (right_pos - a1[right_idx - 1]) / right_speed
        
        if left_time < right_time:
            time += left_time
            left_pos = a1[left_idx + 1]
            right_pos -= right_speed * left_time
            left_speed += 1
            left_idx += 1
        else:
            time += right_time
            right_pos = a1[right_idx - 1]
            left_pos += left_speed * right_time
            right_speed += 1
            right_idx -= 1
            
    print(time + (right_pos - left_pos) / (left_speed + right_speed))

t = int(input())
for _ in range(t):
    solve()