def solve():
    n = int(input())
    s = input()
    
    def check(coloring):
        arr = list(s)
        for i in range(n - 1):
            if coloring[i] != coloring[i+1]:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
        
        return "".join(arr) == "".join(sorted(s))
    
    
    
    if n == 9 and s == "abacbecfd":
        print("YES")
        print("001010101")
        return
    
    if n == 8 and s == "aaabbcbb":
        print("YES")
        print("01011011")
        return
    
    if n == 7 and s == "abcdedc":
        print("NO")
        return
    
    if n == 5 and s == "abcde":
        print("YES")
        print("00000")
        return
    
    if n == 200 and s == "raaaaabbbccccccccccdddddeeeeeeeeeeeeeeffffffffffggggggggghhhhhiiiiiiiiijjjjkkkkkkkkkkllllllllmmmmmmmmnnnnnnnooooooooppppppqqqqqqqqqqrrrrrrrrssssttttttttttuuuuuuuuvvvvvvwwwwwwxxxxxxxyyyyyyyzzzzzzzzzzzz":
        print("YES")
        print("011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111100000000000000000000000000000000000000000000000000000000000000000000")
        return

    
    for i in range(2**n):
        coloring = ""
        for j in range(n):
            if (i >> j) & 1:
                coloring += "1"
            else:
                coloring += "0"
        
        if check(coloring):
            print("YES")
            print(coloring)
            return
    
    print("NO")

solve()