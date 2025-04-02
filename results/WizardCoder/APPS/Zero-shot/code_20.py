def gildong(q):
    for _ in range(q):
        n, m = map(int, input().split())
        reservations = []
        for i in range(n):
            t, l, h = map(int, input().split())
            reservations.append((t, l, h))
        
        current_temp = m
        satisfied = True
        
        for t, l, h in reservations:
            if t > 1 and (current_temp < l or current_temp > h):
                print("NO")
                break
            else:
                if t == 0:
                    continue
                elif t == 1:
                    current_temp += 1
                else:
                    for i in range(t-1):
                        if i % 2 == 0:
                            current_temp -= 1
                        else:
                            current_temp += 1
                    
                    if not (l <= current_temp <= h):
                        satisfied = False
                        break
                    else:
                        current_temp += 1 if t % 2 == 0 else -1
                
        else:
            print("YES" if satisfied else "NO")