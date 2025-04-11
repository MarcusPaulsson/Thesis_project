def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    def can_complete(arr):
        if len(set(arr)) == 1:
            return True
        return False
    
    if can_complete(a):
        print("YES")
        return
    
    q = [a]
    visited = {tuple(a)}
    
    while q:
        curr = q.pop(0)
        
        for i in range(len(curr) - 1):
            if curr[i] == curr[i+1]:
                next_arr = curr[:]
                next_arr[i] += 1
                next_arr[i+1] += 1
                
                if can_complete(next_arr):
                    print("YES")
                    return
                
                if tuple(next_arr) not in visited:
                    q.append(next_arr)
                    visited.add(tuple(next_arr))
    
    print("NO")

solve()