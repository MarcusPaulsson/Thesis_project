def solve():
    s = input()
    adj = {}
    for i in range(len(s) - 1):
        if s[i] not in adj:
            adj[s[i]] = set()
        if s[i+1] not in adj:
            adj[s[i+1]] = set()
        adj[s[i]].add(s[i+1])
        adj[s[i+1]].add(s[i])
    
    for char in adj:
        if len(adj[char]) > 2:
            print("NO")
            return
    
    starts = []
    all_chars = set(s)
    for char in adj:
        if len(adj[char]) <= 1:
            starts.append(char)
    
    if not starts:
        
        first_char = s[0]
        
        layout = first_char
        visited = {first_char}
        
        curr = first_char
        
        while True:
            
            neighbors = adj[curr]
            
            next_char = None
            for neighbor in neighbors:
                if neighbor not in visited:
                    next_char = neighbor
                    break
            
            if next_char is None:
                break
                
            layout += next_char
            visited.add(next_char)
            curr = next_char
        
        
        remaining_chars = ""
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char not in visited:
                remaining_chars += char
        
        if len(layout + remaining_chars) != 26:
            print("NO")
        else:
            print("YES")
            print(layout + remaining_chars)
        
        
    else:
        
        if len(starts) > 2:
            
            
            
            first_char = starts[0]
            
            layout = first_char
            visited = {first_char}
            
            curr = first_char
            
            while True:
                
                neighbors = adj[curr]
                
                next_char = None
                for neighbor in neighbors:
                    if neighbor not in visited:
                        next_char = neighbor
                        break
                
                if next_char is None:
                    break
                    
                layout += next_char
                visited.add(next_char)
                curr = next_char
            
            
            remaining_chars = ""
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char not in visited:
                    remaining_chars += char
            
            if len(layout + remaining_chars) != 26:
                print("NO")
            else:
                print("YES")
                print(layout + remaining_chars)
            
        
        else:
            
            first_char = starts[0]
            
            layout = first_char
            visited = {first_char}
            
            curr = first_char
            
            while True:
                
                if curr not in adj:
                    break
                    
                neighbors = adj[curr]
                
                next_char = None
                for neighbor in neighbors:
                    if neighbor not in visited:
                        next_char = neighbor
                        break
                
                if next_char is None:
                    break
                    
                layout += next_char
                visited.add(next_char)
                curr = next_char
            
            
            remaining_chars = ""
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char not in visited:
                    remaining_chars += char
            
            if len(layout + remaining_chars) != 26:
                print("NO")
            else:
                print("YES")
                print(layout + remaining_chars)
            
    

t = int(input())
for _ in range(t):
    solve()