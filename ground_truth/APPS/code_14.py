["import sys\n\n#f = open('input', 'r')\nf = sys.stdin\nn,k = list(map(int, f.readline().split()))\na = list(map(int, f.readline().split()))\naset = set(a)\nst = []\nfailed = False\nai = 0\napp = []\nfor p in range(1, n+1):\n  if p in aset:\n    while ai < k and (len(st)==0 or st[-1]!=p):\n      st.append(a[ai])\n      ai += 1\n    if len(st) == 0 or st[-1] != p:\n      failed = True\n      break\n    st.pop(-1)\n    a += app[::-1]\n    app = []\n  else:\n    if ai != k:\n      st += a[ai:k]\n      ai = k\n    app.append(p)\n\nif failed:\n  print(-1)\nelse:\n  print(' '.join(map(str, a + app[::-1])))\n", "import sys\nn,k = [int(x) for x in input().split()]\na = list(reversed([int(x)-1 for x in input().split()]))\ns = []\nb = []\ngoal = 0\n\nused = [False]*(n)\nfor node in a:\n    used[node]=True\n\nsearch_from = -1\nbig = n-1 \nres = []\nwhile goal!=n:\n    while a:\n        res.append(a[-1])\n        s.append(a.pop())\n        search_from = s[-1]-1\n        if (len(s)>1 and s[-1]>s[-2]):\n            print(-1)\n            return\n        while s and s[-1]==goal:\n            goal += 1\n            s.pop()\n            if s:\n                search_from = s[-1]-1\n    if goal==n:\n        break\n    if len(s)==0:\n        while big>=0 and used[big]:\n            big-=1\n        if big==-1:\n            print(-1)\n            return\n        used[big]=True\n        a.append(big)\n    else:\n        while search_from>=0 and used[search_from]:\n            search_from-=1\n        if search_from==-1:\n            print(-1)\n            return\n        used[search_from]=True\n        a.append(search_from)\n        \nprint(*[x+1 for x in res])\n", "import sys\n\n\ndef print_list(list):\n    for i in list:\n        print(i, end=\" \")\n    print()\n\n\nn, k = [int(i) for i in input().split(\" \")]\nmy_list = [int(i) for i in input().split(\" \")]\n\nstack = list()\n\nnext_pop = 1\n\nfor num in my_list:\n    if stack and stack[-1] < num:\n        print(\"-1\")\n        return\n\n    stack.append(num)\n\n    while stack and stack[-1] == next_pop:\n        stack.pop()\n        next_pop += 1\n\nwhile stack:\n    for i in range(stack[-1] - 1, next_pop - 1, -1):\n        my_list.append(i)\n    next_pop = stack.pop() + 1\n\nif next_pop > n:\n    print_list(my_list)\nelse:\n    for j in range(n, next_pop - 1, -1):\n        my_list.append(j)\n    print_list(my_list)\n", "import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools\n\nsys.setrecursionlimit(10**7)\ninf = 10**20\neps = 1.0 / 10**15\nmod = 10**9+7\n\ndef LI(): return [int(x) for x in sys.stdin.readline().split()]\ndef LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]\ndef LF(): return [float(x) for x in sys.stdin.readline().split()]\ndef LS(): return sys.stdin.readline().split()\ndef I(): return int(sys.stdin.readline())\ndef F(): return float(sys.stdin.readline())\ndef S(): return input()\ndef pf(s): return print(s, flush=True)\n\n\ndef main():\n    n,k = LI()\n    a = LI()\n    r = a[:]\n    s = []\n    m = 1\n    for c in a:\n        if c == m:\n            m += 1\n            t = len(s)\n            for i in range(t-1,-1,-1):\n                if s[i] == m:\n                    m += 1\n                    t = i\n                else:\n                    break\n            if t != len(s):\n                s = s[:t]\n        else:\n            s.append(c)\n    for i in range(len(s)-1):\n        if s[i] < s[i+1]:\n            return -1\n\n    for i in range(len(s)-1,-1,-1):\n        c = s[i]\n        r += list(range(c-1,m-1,-1))\n        m = c+1\n    r += list(range(n,m-1,-1))\n\n    return ' '.join(map(str,r))\n\nprint(main())\n\n\n", "n, k = map(int, input().split(' '))\np = list(map(int, input().split(' ')))\n\ni = 0\ns = []\ncur = 1\nsolution = list(p)\nwhile True:\n    if len(s) > 0 and s[-1] == cur:\n        cur += 1\n        s.pop()\n    elif i < len(p):\n        if len(s) > 0 and p[i] > s[-1]:\n            solution = [-1]\n            break\n        s.append(p[i])\n        i += 1\n    else:\n        break\n\nif solution[0] != -1:\n    while cur <= n:\n        top = s.pop() if len(s) > 0 else n + 1\n        solution.extend(reversed(range(cur, top)))\n        cur = top + 1\n        \nprint(' '.join(str(x) for x in solution))", "import sys\nf=sys.stdin\nn,k=map(int,f.readline().split())\ns,t=[n+1],1\na=list(map(int,f.readline().split()))\nfor i in range(n):\n\tif i>=k:\n\t\ta+=[s[-1]-1]\n\ts+=[a[i]]\n\twhile (len(s)!=0) and (s[-1]==t):\n\t\ts.pop()\n\t\tt+=1\nif len(s):\n\tprint('-1')\nelse:\n\tprint(' '.join(str(x) for x in a))", "import sys\nf=sys.stdin\nn,k=map(int,f.readline().split())\ns,t=[n+1],1\na=list(map(int,f.readline().split()))\nfor i in range(n):\n\tif i>=k:\n\t\ta+=[s[-1]-1]\n\ts+=[a[i]]\n\twhile (len(s)!=0) and (s[-1]==t):\n\t\ts.pop()\n\t\tt+=1\nif len(s):\n\tprint('-1')\nelse:\n\tprint(' '.join(str(x) for x in a))", "import sys\nf=sys.stdin\nn,k=map(int,f.readline().split())\ns,t=[n+1],1\na=list(map(int,f.readline().split()))\nfor i in range(n):\n\tif i>=k:\n\t\ta+=[s[-1]-1]\n\ts+=[a[i]]\n\twhile (len(s)!=0) and (s[-1]==t):\n\t\ts.pop()\n\t\tt+=1\nif len(s):\n\tprint('-1')\nelse:\n\tprint(' '.join(str(x) for x in a))", "# https://codeforces.com/problemset/problem/911/E\n\nn, k = map(int, input().split())\np    = list(map(int, input().split()))\nd    = {x:1 for x in p}\n\ndef solve(p, d, n):\n    add  = []\n    s    = []\n    \n    for x in range(1, n+1):\n        if x not in d:\n            while len(p) > 0:\n                s.append(p.pop(0))\n                \n                if len(s) >= 2 and s[-1] > s[-2]:\n                    return False, None\n                \n            # len(p)=0\n            if len(s) == 0 or s[-1] != x:\n                up = n if len(s) == 0 else s[-1]-1\n            \n                for y in range(up, x-1, -1):\n                    add.append(y)\n                    s.append(y)\n                    d[y]=1\n            s.pop()\n        else:\n            if len(s) == 0 or s[-1] != x:\n                while len(p) > 0:\n                    s.append(p.pop(0))\n                \n                    if len(s) >= 2 and s[-1] > s[-2]:\n                        return False, None\n                \n                    if s[-1] == x:\n                        break\n            s.pop()\n    return True, add\n\nans =  [x for x in p]\nflg, add = solve(p, d, n)\nif flg==False:\n    print(-1)\nelse:\n    print(' '.join([str(x) for x in ans+add]))", "import sys\n \nn,k = map(int,input().split())\na = list(map(int,input().split()))\nsetofa = set(a)\ns = []\nf= False\nai = 0\nans = []\nfor i in range(1, n+1):\n  if i in setofa:\n    while ai < k and (len(s)==0 or s[-1]!=i):\n      s.append(a[ai])\n      ai += 1\n    if len(s) == 0 or s[-1] != i:\n      f = True\n      break\n    s.pop(-1)\n    a += ans[::-1]\n    ans = []\n  else:\n    if ai != k:\n      s += a[ai:k]\n      ai = k\n    ans.append(i)\n \nif f:\n  print(-1)\nelse:\n  print(' '.join(map(str, a + ans[::-1])))"]