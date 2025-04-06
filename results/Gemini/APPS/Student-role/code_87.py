def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    positive_projects = []
    negative_projects = []
    for a, b in projects:
        if b >= 0:
            positive_projects.append((a, b))
        else:
            negative_projects.append((a, b))

    positive_projects.sort()
    
    count = 0
    for a, b in positive_projects:
        if r >= a:
            r += b
            count += 1

    negative_projects.sort(key=lambda x: x[0] + x[1], reverse=True)

    def can_complete(subset, initial_rating):
        rating = initial_rating
        for a, b in subset:
            if rating >= a:
                rating += b
                if rating < 0:
                    return False
            else:
                return False
        return True
    
    def find_max_subset(remaining_projects, current_subset, current_rating):
        if not remaining_projects:
            return len(current_subset)
        
        max_size = len(current_subset)
        
        for i in range(len(remaining_projects)):
            next_project = remaining_projects[i]
            
            temp_subset = current_subset[:]
            temp_subset.append(next_project)
            
            temp_remaining = remaining_projects[:i] + remaining_projects[i+1:]

            if can_complete(temp_subset, r):
                max_size = max(max_size, find_max_subset(temp_remaining, temp_subset, r))
        
        return max_size

    
    rating = r
    negative_count = 0
    
    for a, b in negative_projects:
        if rating >= a:
            rating += b
            if rating >= 0:
                negative_count += 1
            else:
                rating -=b
                
    rating = r
    count = 0
    for a, b in positive_projects:
        if rating >= a:
            rating += b
            count += 1

    rating = r
    
    
    
    temp_r = r
    
    for a,b in positive_projects:
        if temp_r >=a:
            temp_r+=b
        else:
            break
    
    
    
    negative_projects.sort(key = lambda x : x[0]+x[1],reverse = True)
    
    
    temp_count = count
    
    
    for a,b in negative_projects:
        if rating >= a:
            rating+=b
            if rating >=0:
                temp_count+=1
            else:
                rating -=b
                
    print(temp_count)
solve()