def solve():
    n, k = map(int, input().split())
    s = input()
    
    subsequences = set()
    
    def generate_subsequences(index, current_subsequence):
        if index == n:
            if current_subsequence:
                subsequences.add(current_subsequence)
            return
        
        generate_subsequences(index + 1, current_subsequence)
        generate_subsequences(index + 1, current_subsequence + s[index])
    
    generate_subsequences(0, "")
    
    if len(subsequences) < k:
        print(-1)
        return
    
    subsequences_list = sorted(list(subsequences), key=len)
    
    total_cost = 0
    for i in range(k):
        total_cost += n - len(subsequences_list[i])
    
    print(total_cost)

solve()