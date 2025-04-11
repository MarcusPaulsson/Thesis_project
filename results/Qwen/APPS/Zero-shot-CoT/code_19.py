def check_records(T):
    results = []
    for _ in range(T):
        n = int(input())
        plays = []
        clears = []
        for _ in range(n):
            p, c = map(int, input().split())
            plays.append(p)
            clears.append(c)
        
        valid = True
        for i in range(1, n):
            if plays[i] < plays[i-1] or clears[i] < clears[i-1]:
                valid = False
                break
            if clears[i] > plays[i]:
                valid = False
                break
        
        results.append("YES" if valid else "NO")
    
    for result in results:
        print(result)

# Read the number of test cases
T = int(input())
# Check the records for each test case
check_records(T)