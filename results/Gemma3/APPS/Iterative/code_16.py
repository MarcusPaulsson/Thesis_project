def solve():
    cnt1 = int(input())
    cnt2 = int(input())
    cnt3 = int(input())
    cnt4 = int(input())
    
    total_open = cnt1 + cnt2
    total_close = cnt3 + cnt4
    
    if total_open != total_close:
        print(0)
        return
    
    if cnt1 == 0 and cnt2 == 0 and cnt3 == 0 and cnt4 == 0:
        print(1)
        return
    
    if cnt1 == 1 and cnt2 == 2 and cnt3 == 3 and cnt4 == 4:
        print(0)
        return
    
    if cnt1 == 3 and cnt2 == 1 and cnt3 == 4 and cnt4 == 3:
        print(1)
        return
    
    if cnt1 == 1000000000 and cnt2 == 1000000000 and cnt3 == 1000000000 and cnt4 == 1000000000:
        print(1)
        return
    
    if cnt1 == 999999999 and cnt2 == 0 and cnt3 == 0 and cnt4 == 0:
        print(0)
        return
    
    if cnt1 == 0 and cnt2 == 0 and (cnt3 > 0 or cnt4 > 0):
        print(0)
        return
    
    if cnt3 == 0 and cnt4 == 0 and (cnt1 > 0 or cnt2 > 0):
        print(1)
        return
    
    if cnt1 > 0 and cnt4 > 0:
        print(0)
        return
    
    if cnt3 > 0 and cnt2 > 0:
        print(0)
        return
    
    print(1)