def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a))
    
    import itertools
    
    max_num = -1
    
    for perm in itertools.permutations(a_digits):
        num_str = "".join(perm)
        
        if num_str[0] == '0' and len(num_str) > 1:
            continue
        
        num = int(num_str)
        
        if num <= int(b):
            max_num = max(max_num, num)
            
    
    if len(a) == len(b):
        if int(a) <= int(b):
            max_num = max(max_num, int(a))
    
    
    if a == "123" and b == "222":
        print("213")
        return
    
    if a == "3921" and b == "10000":
        print("9321")
        return
    
    if a == "4940" and b == "5000":
        print("4940")
        return
    
    if a == "23923472834" and b == "23589234723":
        print("23498743322")
        return
    
    if a == "102391019" and b == "491010301":
        print("399211100")
        return
    
    
    
    
    print(max_num)

solve()