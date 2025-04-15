["'''input\n5\n3123 3123\n2777 2777\n2246 2246\n2246 2246\n1699 1699\n'''\nn = int(input())\nx = []\nf = 0\nfor _ in range(n):\n\ta, b = list(map(int, input().split()))\n\tif a != b:\n\t\tf = 1\n\tx.append(a)\nif f == 1:\n\tprint(\"rated\")\nelif sorted(x)[::-1] == x:\n\tprint(\"maybe\")\nelse:\n\tprint(\"unrated\")\n\n\n\n\n\n\n\n", "def sol():\n    n = int(input())\n    flag = False\n    last = None\n    for i in range(n):\n        a,b = map(int, input().split(' '))\n        if a != b:\n            return \"rated\"\n        if last is not None and a > last:\n            flag = True\n        last = a\n    if flag:\n        return \"unrated\"\n    else:\n        return \"maybe\"\n\n\n\nprint(sol())", "N = int(input())\nratings = [tuple(int(x) for x in input().split()) for _ in range(N)]\nif any(a != b for a, b in ratings):\n    print(\"rated\")\nelif sorted(ratings, reverse=True) == ratings:\n    print(\"maybe\")\nelse:\n    print(\"unrated\")\n", "n = int(input())\na=[[int(i) for i in input().split()] for i in range(n)]\nans = 'maybe'\nfor i in range(n):\n    if a[i][0] != a[i][1]:\n        ans = 'rated'\n        break\nelse:\n    for i in range(n-1):\n        if a[i][0] < a[i+1][0]:\n            ans = 'unrated'\n            break\nprint(ans)\n", "n = int(input())\na = []\na1 = []\nfor i in range(n):\n    f,s = list(map(int, input().split()))\n    if f != s:\n        print(\"rated\")\n        return\n    a.append(s)\n    a1.append(s)\na.sort()\nif a[::-1] == a1:\n    print(\"maybe\")\n    return\nprint(\"unrated\")\n\n", "n = int(input())\ns = []\nfor i in range(n):\n    a, b = map(int, input().split())\n    if a !=b:\n        print(\"rated\")\n        break\n    s.append(b)\nelse:\n    if s[::-1] != sorted(s):\n        print(\"unrated\")\n    else:\n        print(\"maybe\")", "from sys import stdin\ninput = stdin.readline\n\nn = int(input())\n\nchange = 0\nunordered = 0\nc = float('inf')\nfor i in range(n):\n  a, b = [int(x) for x in input().split()]\n  if a!=b:\n    change = 1\n    break\n  elif c<a:\n    unordered=1\n  c = a\n\nif change:\n  print('rated')\nelif unordered:\n  print('unrated')\nelse:\n  print('maybe')\n  \n", "n = int(input())\n\nans = 'maybe'\nrate = [0] * n\nfor i in range(n):\n    a, b = map(int, input().split())\n    rate[i] = [a, b]\n    if a != b:\n        ans = 'rated'\n        \nif ans == 'rated':\n    print(ans)\nelse:\n    mn = 10 ** 9\n    for i in range(n):\n        if mn < rate[i][0]:\n            ans = 'unrated'\n            break\n        \n        mn = min(mn, rate[i][0])\n        \n    print(ans)", "n = int(input())\na = [0]*n\nb = [0]*n\ns1 = True\ns2 = True\nfor i in range(n):\n    a[i], b[i] = list(map(int, input().split() ))\n    if a[i] != b[i]:\n        s1 = False\nif a == list(reversed(sorted(a))):\n    s2 = False\n\nif not s1:\n    print(\"rated\")\nelif  not s2:\n    print(\"maybe\")\nelse:\n    print(\"unrated\")\n", "n = int(input())\n\nrates = []\n\nfor i in range(n):\n    before, after = list(map(int, input().split()))\n    rates.append(before)\n    if before != after:\n        print('rated')\n        return\n\nprint('maybe' if rates == list(reversed(sorted(rates))) else 'unrated')\n", "n = int(input())\n\nratings = []\nis_rated = False\nfor _ in range(n):\n    start, end = [int(p) for p in input().split()]\n    if start != end:\n        is_rated = True\n    ratings.append((start, end))\n\nif is_rated:\n    print('rated')\nelse:\n    #\n    if list(reversed(sorted(ratings, key=lambda x: x[0]))) == ratings:\n        print('maybe')\n    else:\n        print('unrated')\n", "t=int(input())\nf=1\ng=0\na=[]\nwhile(t):\n    t-=1\n    a.append(list(map(int,input().split())))\nfor i in range(len(a)):\n    if(a[i][0]!=a[i][1]):\n        f=0\n    if(i!=0 and a[i][0]>a[i-1][0]):\n        g=1\nif(f==0):\n    print(\"rated\")\nelse:\n    if(g):\n        print(\"unrated\")\n    else:\n        print(\"maybe\")", "import sys\n\ninput_ = sys.stdin.readline\n\n\ndef is_ordered(arr):\n    for i in range(len(arr) - 1):\n        if arr[i] < arr[i + 1]:\n            return False\n    else:\n        return True\n\n\ndef main():\n    n = int(input_())\n    changed = False\n\n    befores = []\n    afters = []\n\n    for x in range(n):\n        before, after = list(map(int, input_().split()))\n\n        if before != after:\n            changed = True\n\n        befores.append(before)\n        afters.append(after)\n\n    if changed:\n        return \"rated\"\n\n    if is_ordered(afters):\n        return \"maybe\"\n\n    return \"unrated\"\n\n\ndef __starting_point():\n    print(main())\n\n__starting_point()", "from sys import stdin, stdout\n\n\nn = int(stdin.readline().rstrip())\n\na=[]\nb=[]\nfor i in range(n):\n    x,y = list(map(int, stdin.readline().rstrip().split()))\n    a.append(x)\n    b.append(y)\n\nrated = 0\nfor i in range(n):\n    if a[i]!=b[i]:\n        rated=1\n        break\n    \nif not rated:\n    for i in range(n-1):\n        if a[i]<a[i+1]:\n            rated=-1\n\nif rated==1:\n    print(\"rated\")\nelif rated==0:\n    print(\"maybe\")\nelse:\n    print(\"unrated\")\n", "n = int(input())\n\nnochange = True\norder_kept = True\n\nprev_b = float(\"inf\")\nfor i in range(n):\n    b, a = list(map(int, input().split()))\n    if b != a:\n        nochange = False\n        break\n    if b > prev_b:\n        order_kept = False\n    prev_b = b\n\nif not nochange:\n    print(\"rated\")\nelse:\n    if order_kept:\n        print(\"maybe\")\n    else:\n        print(\"unrated\")\n", "n = int(input())\nL = []\nans = \"maybe\"\nfor _ in range(n):\n    a, b = list(map(int, input().split()))\n    L.append((a,b))\n    if a != b:\n        ans = \"rated\"\n        break\nL1 = L[:]\nL1.sort(reverse=True)\nfor i in range(len(L)):\n    if L[i] != L1[i] and ans != \"rated\":\n        ans = \"unrated\"\n        break\nprint(ans)\n", "import math,string,itertools,collections,re,fractions,array,copy\nimport bisect\nimport heapq\nfrom itertools import chain, dropwhile, permutations, combinations\nfrom collections import deque, defaultdict, OrderedDict, namedtuple, Counter, ChainMap\n\n\n# Guide:\n#   1. construct complex data types while reading (e.g. graph adj list)\n#   2. avoid any non-necessary time/memory usage\n#   3. avoid templates and write more from scratch\n#   4. switch to \"flat\" implementations\n\ndef VI(): return list(map(int,input().split()))\ndef I(): return int(input())\ndef LIST(n,m=None): return [0]*n if m is None else [[0]*m for i in range(n)]\ndef ELIST(n): return [[] for i in range(n)]\ndef MI(n=None,m=None): # input matrix of integers\n    if n is None: n,m = VI()\n    arr = LIST(n)\n    for i in range(n): arr[i] = VI()\n    return arr\ndef MS(n=None,m=None): # input matrix of strings\n    if n is None: n,m = VI()\n    arr = LIST(n)\n    for i in range(n): arr[i] = input()\n    return arr\ndef MIT(n=None,m=None): # input transposed matrix/array of integers\n    if n is None: n,m = VI()\n    a = MI(n,m)\n    arr = LIST(m,n)\n    for i,l in enumerate(a):\n        for j,x in enumerate(l):\n            arr[j][i] = x\n    return arr\n\ndef main(info=0):\n    n = I()\n    m = MI(n, 2)\n\n    for a,b in m:\n        if a != b:\n            print(\"rated\")\n            return\n    for i in range(1, n):\n        if m[i][0] > m[i-1][0]:\n            print(\"unrated\")\n            return\n    print(\"maybe\")\n\n\n\n\ndef __starting_point():\n    main()\n\n__starting_point()", "n=int(input())\nl1=[]\nl2=[]\nfor i in range(n):\n\ta,b=map(int,input().split())\n\tl1.append(a)\n\tl2.append(b)\nrc = False\nfor i in range(n):\n\tif(l1[i]!=l2[i]):\n\t\trc=True\n\t\tbreak\nif(rc==True):\n\tprint(\"rated\")\n\treturn\ntot = 0\nfor i in range(1,n):\n\tif(l2[i]<=l2[i-1]):\n\t\ttot+=1\nif(tot==n-1):\n\tprint(\"maybe\")\n\treturn\nprint(\"unrated\")", "# written by sak\n#\n#\tsk<3\n#\n# powered by codechef\n\nn=int(input())\nchange=0\nordered=1\np=997979\nq=86949\nwhile n>0:\n\tx=input()\n\tx=x.split(' ')\n\tif(int(x[0])>p):\n\t\tordered=0\n\tp=int(x[0])\n\tq=int(x[1])\n\tif(p!=q):\n\t\tchange=1\n\tn-=1\n\nif(change==1):\n\tprint(\"rated\")\nelif(ordered==0):\n\tprint(\"unrated\")\nelse:\n\tprint(\"maybe\")\n", "n=int(input())\nx=[]\ny=[]\nfor i in range(n):\n\ts=input()\n\ts=s.split()\n\tx.append(int(s[0]))\n\ty.append(int(s[1]))\nflag=0\nfor i in range(n):\n\tif(x[i]!=y[i]):\n\t\tflag=1\n\t\tbreak\n\telif(i>0):\n\t\tif(x[i]>x[i-1]):\n\t\t\tflag=2\nif(flag==1):\n\tprint(\"rated\")\nelif(flag==2):\n\tprint(\"unrated\")\nelse:\n\tprint(\"maybe\")\n\t\n", "n = int(input())\nA = []\nfor i in range(n):\n\tb, a = map(int, input().split())\n\tA.append(a)\n\tif b != a:\n\t\tprint(\"rated\")\n\t\tbreak\nelse:\n\tB = sorted(A)\n\tA.reverse()\n\tif A == B:\n\t\tprint(\"maybe\")\n\telse:\n\t\tprint(\"unrated\")", "import sys\n\nn = int(input())\n\nkek = False\nchanged = False\n\nprev = 9999\nfor i in range(n):\n    x, y = list(map(int, input().split()))\n    if x != y:\n        changed = True\n    if y > prev:\n        kek = True\n    prev = y\n\nif not kek and not changed:\n    print(\"maybe\")\nelif kek and not changed:\n    print(\"unrated\")\nelse:\n    print(\"rated\")\n", "import sys\nn = int(input())\n\nkek = []\n\nfor i in range(n):\n  a, b = (int(i) for i in input().split())\n  kek.append(a)\n  if a != b:\n    print(\"rated\")\n    return\n\nif kek == list(sorted(kek, reverse=True)):\n  print(\"maybe\")\nelse:\n  print(\"unrated\")\n    \n", "n=int(input())\nmax=4127\nT=True\nfor i in range(n):\n\tl,r=list(map(int,input().split()))\n\tif l==r:\n\t\tif max<l:\n\t\t\tT=False\n\t\tmax=l\n\telse:\n\t\tprint(\"rated\")\n\t\tbreak\nelse:\n\tif T:\n\t\tprint(\"maybe\")\n\telse:\n\t\tprint(\"unrated\")\n"]