def solve():
    s = input()
    t = input()
    n = len(s)
    
    def get_reachable(string):
        reachable = set()
        reachable.add(string)
        
        q = [string]
        visited = {string}
        
        while q:
            curr = q.pop(0)
            
            for i in range(n - 1):
                # s[i+1] = s[i]
                new_s1 = list(curr)
                new_s1[i+1] = new_s1[i]
                new_s1 = "".join(new_s1)
                
                if new_s1 not in visited:
                    reachable.add(new_s1)
                    q.append(new_s1)
                    visited.add(new_s1)
                
                # s[i] = s[i+1]
                new_s2 = list(curr)
                new_s2[i] = new_s2[i+1]
                new_s2 = "".join(new_s2)
                
                if new_s2 not in visited:
                    reachable.add(new_s2)
                    q.append(new_s2)
                    visited.add(new_s2)
        
        return reachable
    
    reachable_s = get_reachable(s)
    reachable_t = get_reachable(t)
    
    if any(r in reachable_t for r in reachable_s):
        print("YES")
    else:
        print("NO")

q = int(input())
for _ in range(q):
    solve()