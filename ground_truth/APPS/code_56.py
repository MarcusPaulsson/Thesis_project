["darling = {}\nx = int(input())\nans = 0\nwhile (x not in darling):\n\tdarling[x] = 1\n\tans += 1\n\tx += 1\n\twhile (x % 10 == 0):\n\t\tx /= 10\n\nprint(ans)", "x = int(input())\ndef f(x):\n    x += 1\n    while x % 10 == 0:\n        x //= 10\n    return x\nd = set()\nwhile not x in d:\n    d.add(x)\n    x = f(x)\nprint(len(d))", "def main():\n    s = set()\n    n = int(input())\n    def f(x):\n        x += 1\n        while not x % 10:\n            x //= 10\n        return x\n    while n not in s:\n        s.add(n)\n        n = f(n)\n    print(len(s))\n    return 0\n\nmain()", "# AC\nimport sys\n\n\nclass Main:\n    def __init__(self):\n        self.buff = None\n        self.index = 0\n\n    def __next__(self):\n        if self.buff is None or self.index == len(self.buff):\n            self.buff = self.next_line()\n            self.index = 0\n        val = self.buff[self.index]\n        self.index += 1\n        return val\n\n    def next_line(self, _map=str):\n        return list(map(_map, sys.stdin.readline().split()))\n\n    def next_int(self):\n        return int(next(self))\n\n    def solve(self):\n        n = self.next_int()\n        rs = {}\n        while n not in rs:\n            rs[n] = n\n            n += 1\n            while n % 10 == 0:\n                n /= 10\n        print(len(rs))\n\ndef __starting_point():\n    Main().solve()\n\n__starting_point()", "x = int(input())\n\nseen = set()\n\ndef f(x):\n\tx += 1\n\twhile x % 10 == 0:\n\t\tx  = x // 10\n\treturn x\n\n\nwhile x not in seen:\n\tseen.add(x)\n\tx = f(x)\n\nprint(len(seen))", "from collections import defaultdict\nn = int(input())\nd = defaultdict(int)\nc = 1\nd[n] = 1\nwhile True:\n    n = n+1\n    while n%10==0:\n        n= n/10\n    \n    if d[n]==1:\n        break\n    else:\n        d[n]=1\n        c+=1\n\nprint(c)", "n = int(input())\ns = set()\nx = n\ns.add(x)\nans = 0\nwhile 1:\n    x = x + 1\n    while x % 10 == 0:\n        x //= 10\n\n    if x in s:\n        break\n    else:\n        s.add(x)\n        ans += 1\nprint(len(s))\n", "n = int(input())\nnum = 9\nwhile len(str(n)) != 1:\n    num += 1\n    n += 1\n    while n % 10 == 0:\n        n //= 10\n    \nprint(num)\n", "n = int(input())\ndoneNums = []\nwhile n not in doneNums:\n    doneNums.append(n)\n    n += 1\n    while n % 10 == 0:\n        n/=10\nprint(len(doneNums))", "import sys\n\ninput = sys.stdin.readline\n\nn = int(input())\n\nvisited = set()\n\ndef f(n):\n  n = n+1\n  while (n % 10 == 0):\n    n /= 10\n  return n\n\nans = 0\n\nwhile f(n) not in visited:\n  visited.add(n)\n  n = f(n)\n  ans += 1\n\nprint(ans+1)\n", "def f(x):\n    x+=1\n    while(x%10==0 and x>0):\n        x//=10\n    return x\nvals=set()\nn=int(input())\nvals.add(n)\nwhile f(n) not in vals:\n    vals.add(f(n))\n    n=f(n)\nprint(len(vals))", "a=input()\nalle = set()\nalle.add(int(a))\n\nwhile True:\n\tx = int(a)\n\tx += 1\n\ty = str(x)\n\twhile y[-1] == \"0\":\n\t\ty = y[:-1]\n\tif int(y) in alle:\n\t\tbreak\n\talle.add(int(y))\n\ta = y\nprint(len(alle))\n", "n=int(input())\ndict1={}\nflag=0\ndict1[n]=1\nwhile(flag==0):\n\tn+=1\n\twhile(n%10==0):\n\t\tn=n//10\n\ttry:\n\t\tdict1[n]+=1\n\t\tflag=1\n\texcept:\n\t\tKeyError\n\t\tdict1[n]=1\nprint(len(dict1))", "n = int(input())\nt = 0\nwhile n > 9:\n    n += 1\n    while n % 10 == 0:\n        n //= 10\n    t += 1\nprint(t + 9)\n", "def f(n):\n    n+=1\n    while n%10==0:\n        n/=10\n    return n\n\nx = int(input())\nl = [x]\nwhile 1:\n    x = f(x)\n    if x in l:\n        break\n    l.append(x)\nprint(len(l))", "n = int(input())\n\nseen = set()\n\nwhile n not in seen:\n\tseen.add(n)\n\tn += 1\n\twhile n%10 == 0:\n\t\tn //= 10\n\nprint(len(seen))", "import sys\nsys.setrecursionlimit(2000)\nfrom collections import Counter\nfrom functools import reduce\n# sys.stdin.readline()\n\ndef __starting_point():\n\n    # single variables\n    n = [int(val) for val in sys.stdin.readline().split()][0]\n\n    count = 0\n    s = set([])\n    while(not n in s):\n        s.add(n)\n        n += 1\n        n = str(n)\n        while(n[-1] == '0'):\n            n = n[:-1]\n        n = int(n)\n        count += 1\n    print(count)\n\n\n\n__starting_point()", "n = int(input())\na = 0\nwhile n >= 10:\n   n += 1\n   a += 1\n   while n % 10 == 0:\n      n = n // 10\n\nprint(a + 9)\n   \n", "# -*- coding: utf-8 -*-\n\"\"\"\n@Project : CodeForces\n@File    : 1.py \n@Time    : 2019/4/26 22:31\n@Author  : Koushiro \n\"\"\"\ndef find(num):\n    num+=1\n    while num%10==0:\n        num=num//10\n    return num\n\ndef __starting_point():\n    n= int(input())\n    dic={n:1}\n    n=find(n)\n    while n not in dic:\n        dic[n]=1\n        n=find(n)\n    print(len(dic))\n__starting_point()", "n=int(input())\ns=set()\ns.add(n)\nwhile(n!=1):\n\tn=n+1\n\twhile((n%10)==0):\n\t\tn=n//10\n\ts.add(n)\nfor i in range(2,10):\n\ts.add(i)\nprint(len(s))\n", "def f(x):\n    return int(str(x + 1).rstrip('0'))\n\ndef main():\n    x = int(input())\n\n    l = set()\n\n    while x not in l:\n        l.add(x)\n        x = f(x)\n    \n    print(len(l))\n        \n\ndef __starting_point():\n    main()\n__starting_point()", "f = lambda x: str(n + 1).rstrip('0')\nn = int(input())\ns = set()\nwhile n not in s:\n    s.add(n)\n    n = int(f(n))\nprint(len(s))", "n = int(input())\n\nst = {}\n\nwhile not n in st:\n\tst[n] = True\n\tn += 1\n\twhile n%10 == 0:\n\t\tn /= 10\n\nprint(len(st))\n", "def f(x):\n    x += 1\n    while not x % 10:\n        x //= 10\n    return x\n\n\nprevious = set()\n\nn = int(input())\nwhile n not in previous:\n    previous.add(n)\n    n = f(n)\n\nprint(len(previous))\n", "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n##################################\n# University of Wisconsin-Madison\n# Author: Yaqi Zhang\n##################################\n# This module contains\n##################################\n\n# standard library\nimport sys\n\ndef main():\n    # nums = list(map(int, input().split()))\n    num = int(input())\n    seen = set()\n    while num:\n        if num in seen:\n            break\n        seen.add(num)\n        num += 1\n        while num % 10 == 0:\n            num //= 10\n    print(len(seen))\n\ndef __starting_point():\n    main()\n\n\n__starting_point()"]