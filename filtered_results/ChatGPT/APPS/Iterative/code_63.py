n = int(input().strip())
a = list(map(int, input().strip().split()))

if n <= 2:
    print(0)
else:
    a.sort()
    instability_if_remove_max = a[-2] - a[0]
    instability_if_remove_min = a[-1] - a[1]
    
    result = min(instability_if_remove_max, instability_if_remove_min)
    print(result)