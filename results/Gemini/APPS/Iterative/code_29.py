s = input()
ans = 6
for i in range(28):
    for j in range(28):
        cnt = 0
        s1 = ""
        s2 = ""
        
        sum1 = i
        sum2 = j
        
        for d1 in range(10):
            for d2 in range(10):
                for d3 in range(10):
                    if d1 + d2 + d3 == sum1:
                        s1 = str(d1) + str(d2) + str(d3)
                        
                        for e1 in range(10):
                            for e2 in range(10):
                                for e3 in range(10):
                                    if e1 + e2 + e3 == sum2:
                                        s2 = str(e1) + str(e2) + str(e3)
                                        
                                        cur_cnt = 0
                                        for k in range(3):
                                            if s[k] != s1[k]:
                                                cur_cnt += 1
                                        for k in range(3):
                                            if s[k+3] != s2[k]:
                                                cur_cnt += 1
                                        ans = min(ans, cur_cnt)
print(ans)