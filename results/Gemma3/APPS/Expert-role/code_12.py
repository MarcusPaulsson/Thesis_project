def solve():
    n = int(input())
    trophies = input()
    
    def get_max_len(arr):
        max_len = 0
        curr_len = 0
        for trophy in arr:
            if trophy == 'G':
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 0
        max_len = max(max_len, curr_len)
        return max_len
    
    max_beauty = get_max_len(list(trophies))
    
    for i in range(n):
        for j in range(i + 1, n):
            temp_trophies = list(trophies)
            temp_trophies[i], temp_trophies[j] = temp_trophies[j], temp_trophies[i]
            max_beauty = max(max_beauty, get_max_len(temp_trophies))
            
    print(max_beauty)

solve()