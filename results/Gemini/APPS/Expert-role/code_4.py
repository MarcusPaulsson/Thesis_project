def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    result = ""
    for m in range(1, n + 1):
        is_beautiful = False
        for l in range(n):
            for r in range(l, n):
                sub_array = p[l:r+1]
                if len(sub_array) == m:
                    nums = sorted(sub_array)
                    if nums == list(range(1, m + 1)):
                        is_beautiful = True
                        break
                elif len(sub_array) > m:
                    nums = sorted(sub_array)
                    if len(set(nums)) != len(nums):
                      continue
                    
                    max_val = max(nums)
                    if max_val > m:
                      continue
                    
                    
                    temp = [x for x in nums if x <= m]
                    if len(temp) != len(set(temp)):
                        continue
                    
                    
                    if sorted(temp) == list(range(1,m+1)):
                        is_beautiful = True
                        break

            if is_beautiful:
                break
        
        if is_beautiful:
            result += "1"
        else:
            result += "0"
    
    print(result)

t = int(input())
for _ in range(t):
    solve()