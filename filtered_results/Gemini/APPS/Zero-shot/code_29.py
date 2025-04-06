s = input()
a = [int(c) for c in s]

ans = 6
for i in range(1000):
    s1 = str(i).zfill(3)
    sum1 = sum(int(c) for c in s1)
    for j in range(1000):
        s2 = str(j).zfill(3)
        sum2 = sum(int(c) for c in s2)
        if sum1 == sum2:
            temp = 0
            s1_list = [int(c) for c in s1]
            s2_list = [int(c) for c in s2]
            
            if a[0] != s1_list[0]:
                temp += 1
            if a[1] != s1_list[1]:
                temp += 1
            if a[2] != s1_list[2]:
                temp += 1
            if a[3] != s2_list[0]:
                temp += 1
            if a[4] != s2_list[1]:
                temp += 1
            if a[5] != s2_list[2]:
                temp += 1
            ans = min(ans, temp)
print(ans)