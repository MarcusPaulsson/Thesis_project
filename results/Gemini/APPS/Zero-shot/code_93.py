def solve():
    s = input()
    t = input()
    n = len(s)
    
    for i in range(n):
        for j in range(n):
            temp_s = list(s)
            temp_t = list(t)
            
            def transform(arr, start_idx, end_idx):
                if start_idx < 0 or start_idx >= len(arr) or end_idx < 0 or end_idx >= len(arr):
                    return arr
                
                arr[end_idx] = arr[start_idx]
                return "".join(arr)
            
            
            queue_s = [s]
            visited_s = {s}
            
            while queue_s:
                curr_s = queue_s.pop(0)
                
                if curr_s == t:
                    print("YES")
                    return
                
                for k in range(n - 1):
                    next_s1 = list(curr_s)
                    next_s1 = transform(next_s1, k, k+1)
                    next_s1 = "".join(next_s1)
                    
                    if next_s1 not in visited_s:
                        queue_s.append(next_s1)
                        visited_s.add(next_s1)
                        
                    next_s2 = list(curr_s)
                    next_s2 = transform(next_s2, k+1, k)
                    next_s2 = "".join(next_s2)
                    
                    if next_s2 not in visited_s:
                        queue_s.append(next_s2)
                        visited_s.add(next_s2)
                
    
    
    sets = set(s)
    sett = set(t)
    
    common = sets.intersection(sett)
    
    if len(common) > 0:
        print("YES")
    else:
        print("NO")
        

q = int(input())
for _ in range(q):
    solve()