["n = int(input())\na = list(map(int, input().split()))\na.sort()\nprint(min(a[-1] - a[1], a[-2] - a[0]))\n", "n=int(input())\na=list(map(int,input().split()))\na.sort()\nif a[1]-a[0]>=a[-1]-a[-2]:\n    print(a[-1]-a[1])\nelse:\n    print(a[-2]-a[0])\n", "n=int(input())\narr=list(map(int,input().split()))\narr.sort()\nval1=max(arr)-min(arr[1:])\nval2=max(arr[:n-1])-min(arr)\nprint(min(val1,val2))\n", "n = int(input())\nnums = sorted(list(map(int, input().split())))\n\nr1 = nums[-2] - nums[0]\nr2 = nums[-1] - nums[1]\nprint(min(r1, r2))\n", "#      \nimport collections, atexit, math, sys, bisect \n\nsys.setrecursionlimit(1000000)\ndef getIntList():\n    return list(map(int, input().split()))    \n\ntry :\n    #raise ModuleNotFoundError\n    import numpy\n    def dprint(*args, **kwargs):\n        #print(*args, **kwargs, file=sys.stderr)\n        # in python 3.4 **kwargs is invalid???\n        print(*args,  file=sys.stderr)\n    dprint('debug mode')\nexcept Exception:\n    def dprint(*args, **kwargs):\n        pass\n\n\n\ninId = 0\noutId = 0\nif inId>0:\n    dprint('use input', inId)\n    sys.stdin = open('input'+ str(inId) + '.txt', 'r') #\u6807\u51c6\u8f93\u51fa\u91cd\u5b9a\u5411\u81f3\u6587\u4ef6\nif outId>0:\n    dprint('use output', outId)\n    sys.stdout = open('stdout'+ str(outId) + '.txt', 'w') #\u6807\u51c6\u8f93\u51fa\u91cd\u5b9a\u5411\u81f3\u6587\u4ef6\n    atexit.register(lambda :sys.stdout.close())     #idle \u4e2d\u4e0d\u4f1a\u6267\u884c atexit\n    \nN, = getIntList()\n#print(N)\nza = getIntList()\n\nza.sort()\n\nt = za[-1] - za[1]\nt1 = za[-2] - za[0]\n\nprint(min(t,t1))\n\n\n\n\n\n", "n = int(input())\na = list(map(int,input().split()))\na.sort()\n\nif(len(a) == 2):\n\tprint(0)\nelse:\n\tprint(min(a[-1]-a[1], a[-2]-a[0]))", "def read_nums():\n    return [int(x) for x in input().split()]\n\n\ndef main():\n    n, = read_nums()\n    nums = sorted(read_nums())\n    res = min(nums[-2] - nums[0], nums[-1] - nums[1])\n    print(res)\n\n\ndef __starting_point():\n    main()\n\n__starting_point()", "def solve():\n    n = int(input())\n    arr = [int(k) for k in input().split()]\n    \n    arr.sort()\n    \n    if n == 2:\n        print (0)\n        return\n    \n    ans = arr[-1] - arr[1]\n    ans = min(ans, arr[-2] - arr[0])\n    \n    print (ans)\n    \ndef __starting_point():\n    solve()\n__starting_point()", "# alpha = \"abcdefghijklmnopqrstuvwxyz\"\nt = 1\nfor test in range(t):\n    # n,s = (map(int, input().split()))\n    n = int(input())\n    a = list(map(int, input().split()))\n    a.sort()\n    if a[1]-a[0]>a[-1]-a[-2]:\n        print(a[-1]-a[1])\n    else:\n        print(a[-2]-a[0])\n\n", "def go():\n    n = int(input())\n    a = [int(i) for i in input().split(' ')]\n    if n == 2:\n        return 0\n    m1 = max(a)\n    a.remove(m1)\n    m2 = max(a)\n    mi1 = min(a)\n    a.remove(mi1)\n    mi2 = min(a)\n    if m2 - mi1 < m1 - mi2:\n        return m2 - mi1\n    return m1 - mi2\n\nprint(go())\n", "n = input()\narr = [int(x) for x in input().split()]\narr.sort()\n\nx1, x2 = arr[0], arr[1]\ny1, y2 = arr[-1], arr[-2]\n\nif (y2 - x1) > (y1 - x2):\n    print(y1 - x2)\nelse:\n    print(y2 - x1)\n", "n=int(input())\na=[int(s) for s in input().split()]\na.sort()\nmn1=a[n-2]-a[0]\nmn2=a[n-1]-a[1]\nprint(min(mn1,mn2))\n", "#JMD\n#Nagendra Jha-4096\n\n \nimport sys\nimport math\n\n#import fractions\n#import numpy\n \n###File Operations###\nfileoperation=0\nif(fileoperation):\n    orig_stdout = sys.stdout\n    orig_stdin = sys.stdin\n    inputfile = open('W:/Competitive Programming/input.txt', 'r')\n    outputfile = open('W:/Competitive Programming/output.txt', 'w')\n    sys.stdin = inputfile\n    sys.stdout = outputfile\n\n###Defines...###\nmod=1000000007\n \n###FUF's...###\ndef nospace(l):\n    ans=''.join(str(i) for i in l)\n    return ans\n \n \n \n##### Main ####\nt=1\nfor tt in range(t):\n    n=int(input())\n    a=list(map(int,sys.stdin.readline().split(' ')))\n    a.sort()\n\n    print(min(a[-2]-a[0],a[-1]-a[1]))\n    #n,k,s= map(int, sys.stdin.readline().split(' '))\n    \n    \n#####File Operations#####\nif(fileoperation):\n    sys.stdout = orig_stdout\n    sys.stdin = orig_stdin\n    inputfile.close()\n    outputfile.close()\n", "n = int(input())\na = sorted(list(map(int, input().split())))\nans = 0\nif n > 2:\n    ans = min(a[-2] - a[0], a[-1] - a[1])\nprint(ans)\n", "n = int(input())\na = [int(x) for x in input().split()]\na.sort()\nif a[1]-a[0]>a[-1]-a[-2]:\n\tdel a[0]\nelse:\n\tdel a[-1]\nprint(a[-1]-a[0])", "n = int(input())\ns = list(map(int, input().split()))\nM = max(s)\nm = min(s)\ni = M - m\ns.remove(M)\nM1 = max(s)\ni1 = M1 - m\ns.append(M)\ns.remove(m)\nm1 = min(s)\ni2 = M - m1\nprint(min(i,i1,i2))\n", "from operator import itemgetter\n#int(input())\n#map(int,input().split())\n#[list(map(int,input().split())) for i in range(q)]\n#print(\"YES\" * ans + \"NO\" * (1-ans))\nn = int(input())\nai = list(map(int,input().split()))\nai.sort()\nprint(min(ai[-2] - ai[0],ai[-1] - ai[1]))\n", "n=int(input())\na=list(map(int,input().split()))\na.sort()\nprint(min(a[n-1]-a[1],a[n-2]-a[0]))", "n = int(input())\na = sorted(list(map(int, input().split())))\nprint(min(a[n - 2] - a[0], a[n - 1] - a[1]))", "n = int(input())\nl = list(map(int, input().split()))\nl.sort()\nans1 = l[-2] - l[0]\nans2 = l[-1] - l[1]\nprint(min(ans1, ans2))\n", "n = int(input())\na = [int(i) for i in input().split()]\na.sort(reverse = True)\nprint(min(a[0] - a[-2], a[1] - a[-1]))", "n=int(input())\nl=list(map(int,input().split()))\nl.sort()\nprint(min(l[n-1]-l[0],l[n-1]-l[1],l[n-2]-l[0]))", "import sys\nsys.setrecursionlimit(10**6)\n\ndef main(): \n   nbEntrees = int(input())\n   nb = list(map(int, input().split()))\n   maximum = max(nb)\n   nb.remove(maximum)\n\n   etendue = max(nb) - min(nb)\n   nb.append(maximum)\n   maximum = min(nb)\n   nb.remove(maximum)\n   \n   etendue = min(etendue, max(nb) - min(nb))\n\n   print(etendue)\n\nmain()", "#codeforces _1095B_live\ngi = lambda : list(map(int,input().split()))\nn, = gi()\nl = gi()\nl.sort()\nans = min(max(l)-min(l[1:]),(max(l[:-1])-min(l)))\nprint(ans)\n"]