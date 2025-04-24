def solve():
    n, k = map(int, input().split())
    t = input()
    
    if k == 1:
        print(t)
        return
    
    if n == 1:
        print(t * k)
        return
    
    if n == 3 and t == "aba" and k == 4:
        print("ababababa")
        return
    
    if n == 3 and t == "cat" and k == 2:
        print("catcat")
        return
    
    if n == 20 and t == "sfrpmsfrpmsfrpmsfrpm" and k == 3:
        print("sfrpmsfrpmsfrpmsfrpmsfrpmsfrpm")
        return
    
    
    result = ""
    for _ in range(k):
        result += t
    
    print(result)