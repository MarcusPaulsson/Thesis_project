def solve():
    s = input()
    t = input()
    n = len(s)
    
    def can_transform(s, t):
        if s == t:
            return True
        
        q = [(s, [])]
        visited = {s}
        
        while q:
            curr_s, path = q.pop(0)
            
            if curr_s == t:
                return True
            
            for i in range(n - 1):
                new_s1 = list(curr_s)
                new_s1[i+1] = new_s1[i]
                new_s1 = "".join(new_s1)
                
                if new_s1 not in visited:
                    q.append((new_s1, path + [(i, i+1)]))
                    visited.add(new_s1)
                    
                new_s2 = list(curr_s)
                new_s2[i] = new_s2[i+1]
                new_s2 = "".join(new_s2)
                
                if new_s2 not in visited:
                    q.append((new_s2, path + [(i+1, i)]))
                    visited.add(new_s2)
        
        return False

    
    s_chars = set(s)
    t_chars = set(t)
    
    if any(c in s_chars for c in t_chars):
        print("YES")
    else:
        print("NO")


q = int(input())
for _ in range(q):
    solve()