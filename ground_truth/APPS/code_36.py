["def f(n):\n\tleft, right = -1, n + 1\n\twhile right - left > 1:\n\t\tmid = (left + right) // 2\n\t\tx = 6 * mid * (mid + 1) // 2 + 5 * (mid + 1)\n\t\tif x > n:\n\t\t\tright = mid\n\t\telse:\n\t\t\tleft = mid\n\tif left >= 0:\n\t\tmid = left\n\t\tx = 6 * mid * (mid + 1) // 2 + 5 * (mid + 1)\n\t\tn -= x\n\treturn (n, left + 1)\n\ndef main():\n\tn = int(input())\n\tn, k = f(n)\n\tx = k\n\ty = -2 * k\n\t\n\td = [k + 1] * 6\n\td[1] -= 1\n\tdx = [1, -1, -2, -1,  1, 2]\n\tdy = [2,  2,  0, -2, -2, 0]\n\t\n\tfor i in range(6):\n\t\tx += min(d[i], n) * dx[i]\n\t\ty += min(d[i], n) * dy[i]\n\t\tn = max(0, n - d[i])\n\t\n\tprint(x, y)\n\n\nmain()\n", "from functools import reduce\nfrom decimal import *\nimport math\nimport itertools\n\nclass pair(list):\n    def __init__(self, a, b):\n        list.__init__(self, (a, b))\n    def __add__(self, q): return pair(self[0]+q[0], self[1]+q[1])\n    def __sub__(self, q): return pair(self[0]-q[0], self[1]-q[1])\n    def __mul__(self, k): return pair(k*self[0], k*self[1])\n    def __neg__(self): return pair(-self[0], -self[1])\n\nsetcontext(ExtendedContext)\ngetcontext().prec = 100\na, b, c = pair(1,2), pair(-2,0), pair(-1,2)\nn = int(input())\nk = int(((Decimal(3 + 4*n) / Decimal(3)).sqrt() - Decimal(1)) // 2)\nn1 = n - 3*k*(k+1)\nx, y = n1//(k+1), n1%(k+1)\nL = [c, b, -a, -c, -b, a]\nM = [pair(0,0)] + list(itertools.accumulate(L))\nif n1 == 0:\n    ans = pair(2,0)*k\nelse:\n    ans = pair(2,0)*(k+1) + M[x]*(k+1) + L[x]*y\nprint(ans[0], ans[1])\n", "#!/usr/bin/env python3\ndef binsearch(p, l, r): # (l,r], return the smallest n which p holds\n    while l+1 != r:\n        m = (l + r) // 2\n        if p(m):\n            r = m\n        else:\n            l = m\n    return r\nn = int(input())\nif n == 0:\n    print(0, 0)\nelse:\n    i = binsearch(lambda i: n <= 3*i*(i+1), 0, 10**18)\n    acc = 3*(i-1)*i\n    j = binsearch(lambda j: n <= acc + i*(j+1), -1, 6)\n    k = n - acc - i*j - 1\n    dy = [ 0, 2,  2,  0, -2, -2 ]\n    dx = [ 2, 1, -1, -2, -1,  1 ]\n    y = dy[(j+1)%6] + dy[j]*(i-1) + dy[(j+2)%6]*k\n    x = dx[(j+1)%6] + dx[j]*(i-1) + dx[(j+2)%6]*k\n    print(x, y)\n", "import math\ndef main(m):\n    if m == 0:\n        print(\"0 0\")\n    else:\n        x = math.floor(1/6*((12*m - 3)**0.5 + 3)) # Approx ?...\n        while True:\n            d = m - (x**3 - (x-1)**3)\n            if (d < 0): x -= 1\n            elif (d > x * 6 + 6): x += 1\n            else: break\n        s,r = divmod(d, x)\n        #print(\"x:{}, d:{}, s:{}, r:{}\".format(x,d,s,r));\n        if s == 0:\n            print(\"{} {}\".format(2*x-r-1,2*r+2))\n        elif s == 1:\n            print(\"{} {}\".format(x-2*r-2,2*x))\n        elif s == 2:\n            print(\"{} {}\".format(-x-r-1,2*(x-r-1)))\n        elif s == 3:\n            print(\"{} {}\".format(-2*x+r+1,-2*r-2))\n        elif s == 4:\n            print(\"{} {}\".format(-x+2*r+2,-2*x))\n        elif s == 5:\n            print(\"{} {}\".format(x+r+1,-2*x+2*r+2))\n            \ndef __starting_point():\n    main(int(input()))\n\n__starting_point()", "def layer(n):\n    a = (-3 + (9+12*n)**0.5)//6\n    a = int(a)\n    a+=1\n    while 3*a*(a+1) >= n:\n        a-=1\n    return a+1\n\nn = int(input())\nif n == 0:\n    print(0, 0)\n    quit()\n\nl = layer(n)\nbase = 3*(l-1)*l+1\n# base = (2*l-1, 2)\n\na = [2*l, 0]\nb = [l, 2*l]\nbx = base + (l-1)\nc = [-l, 2*l]\ncx = bx + l\nd = [-2*l, 0]\ndx = cx + l\ne = [-l, -2*l]\nex = dx + l\nf = [l, -2*l]\nfx = ex + l\nax = fx + l\ndaa = abs(n-base+1)\nda = abs(n-ax)\ndb = abs(n-bx)\ndc = abs(n-cx)\ndd = abs(n-dx)\nde = abs(n-ex)\ndf = abs(n-fx)\n\nif (n <= bx):\n    print(int((db*a[0]+daa*b[0])/(db+daa)), int((db*a[1]+daa*b[1])/(db+daa)))\n    quit()\n    \nif (bx <= n <= cx):\n    print(int((dc*b[0]+db*c[0])/(db+dc)), b[1])\n    quit()\n    \nif (cx <= n <= dx):\n    print(int((dd*c[0]+dc*d[0])/(dc+dd)), int((dd*c[1]+dc*d[1])/(dc+dd)))\n    quit()\n    \nif (dx <= n <= ex):\n    print(int((de*d[0]+dd*e[0])/(dd+de)), int((de*d[1]+dd*e[1])/(dd+de)))\n    quit()\n    \nif (ex <= n <= fx):\n    print(int((df*e[0]+de*f[0])/(de+df)), e[1])\n    quit()\n    \nif (fx <= n <= ax):\n    print(int((da*f[0]+df*a[0])/(df+da)), int((da*f[1]+df*a[1])/(df+da)))\n    quit()\n", "ru = (1,2)\nr = (2,0)\nrd = (1,-2)\nld = (-1,-2)\nl = (-2,0)\nlu = (-1,2)\nx, y = 0, 0\nn = int(input())\nl = -1\nr = int(1e18)\nwhile r - l > 1:\n    m = (r + l)//2\n    if 5 * m + 3 * m * (m - 1) > n: r = m\n    else: l = m\n    \nx += l * (1)\ny += l * (-2)\nn -= 5 * l + 3 * l * (l - 1)\nif n<r:\n    x+= n * 1\n    y+= n * (2)\n    n = 0\nelse:\n    n -= r\n    x+=r*1\n    y+=r*2\n    \nif n<r-1:\n    x+= n * (-1)\n    y+= n * 2\n    n = 0\nelse:\n    n -= l\n    x+=l*(-1)\n    y+=l*2\nif n < r:\n    x+=-2 * n\n    n = 0\nelse:\n    n-=r\n    x+=-2 * r\nif n < r:\n    x+=-1 * n\n    y+=-2 * n\n    n = 0\nelse:\n    n -= r\n    x+=-1 * r\n    y+=-2 * r\n    \nif n < r:\n    x+=1 * n\n    y+=-2 * n\n    n = 0\nelse:\n    n -= r\n    x += 1*r\n    y += -2*r\n    \nif n < r:\n    x+=2*n\n    \nprint(x, y)\n    \n\n\n", "from math import sqrt, ceil\nfrom collections import namedtuple\n\ndef add(a, b):\n    return a[0] + b[0], a[1] + b[1]\n\ndef count(p):\n    return p * (3 * p + 2)\n\n\ndef bin_search(n):\n    l = 0\n    r = ceil(sqrt(n))\n    while r - l > 1:\n        m = (l + r) // 2\n        if count(m) > n:\n            r = m - 1\n        else:\n            l = m\n    if count(r) > n:\n        return l\n    else:\n        return r\n\n\ndef get_pos(n, p):\n    if n < p: # /\n        return add( (p - 1, -2 * p + 2), (n, 2 * n) ) \n    n -= p\n    if n < p - 1: # \\\n        return add( (1 + 2 * (p - 1), 2), (-n, 2 * n) )\n    n -= p - 1\n    if n < p: # -\n        return add( (p, 2 * p), (-2 * n, 0) )\n    n -= p\n    if n < p: # /\n        return add( (-p, 2 * p), (-n, -2 * n) )\n    n -= p\n    if n < p: # \\\n        return add( (-2 * p, 0), (n, -2 * n) )\n    n -= p\n    if n < p: # -\n        return add( (-p, -2 * p), (2 * n, 0) )\n    raise RuntimeError(\"You're a big guy\")\n\n\nn = int(input())\nif n == 0:\n    print(0, 0)\nelse:\n    p = bin_search(n)\n    start = count(p)\n    #print(p, start)\n    n -= start\n    ans = get_pos(n, p + 1)\n    print(ans[0], ans[1])\n", "def sLayer(n):\n\treturn 3*n*(n+1)\n\ndef getLayer(N):\n\ta = 0\n\tb = 600000000\n\twhile b-a > 1:\n\t\tn = (a+b)//2\n\t\ttN = sLayer(n)\n\t\tif tN > N:\n\t\t\tb = n\n\t\telse:\n\t\t\ta = n\n\treturn a\n\nN = int(input())\nif N == 0:\n\tprint(\"0 0\")\n\traise SystemExit\n\nN -= 1\nlayer = getLayer(N)\nN -= sLayer(layer)\n\nseg = N//(layer+1)\nidx = N%(layer+1)\n\nsegDiff = [(-1,2), (-2,0), (-1,-2), (1,-2), (2,0), (1,2)]\n\nif seg == 0:\n\tx = 2*layer+1\n\ty = 2\nelif seg == 1:\n\tx = -1+layer\n\ty = 2*(layer+1)\nelif seg == 2:\n\tx = -2-layer\n\ty = 2*layer\nelif seg == 3:\n\tx = -1-2*layer\n\ty = -2\nelif seg == 4:\n\tx = 1-layer\n\ty = -2-2*layer\nelif seg == 5:\n\tx = 2+layer\n\ty = -2*layer\n\nx += segDiff[seg][0]*idx\ny += segDiff[seg][1]*idx\nprint(\"%d %d\" % (x,y))\n", "3\n\nimport math\n\ndef solve(n):\n  if n == 0:\n    return (0, 0)\n\n  k = int(0.5 * (-1 + math.sqrt(1 + 4 * n / 3.0))) + 10\n  while 3 * k * (k + 1) >= n:\n    k -= 1\n \n  n -= 3 * k * (k + 1) + 1\n  x = 1 + 2 * k\n  y = 2\n\n  lim = [k] + [k + 1] * 5\n  dx = [-1, -2, -1, 1, 2, 1]\n  dy = [2, 0, -2, -2, 0, 2]\n\n  i = 0\n  while n > 0:\n    t = min(n, lim[i])\n    x += t * dx[i]\n    y += t * dy[i]\n    n -= t\n    i += 1\n\n  return (x, y)\n\nx, y = solve(int(input()))\nprint(x, y)\n\n# for i in range(21):\n#   print(i, solve(i))\n\n\n", "def main():\n\tn = int(input())\n\t(x, y) = solver(n)\n\tprint(x, y)\n\ndef solver(n):\n\trounds = int(quadraticEqPlus(3, 3, -n))\n\tn -= 3 * rounds * (rounds + 1)\n\tcurPoint = (2 * rounds, 0)\n\tcurRound = rounds + 1\n\t# go UpRight\n\t#if n >= 1:\n\t#\tcurPoint = goUpRight()\n\tcircle = [(goUpRight, 1), (goUpLeft, curRound - 1), \n\t(goLeft, curRound), (goDownLeft, curRound), \n\t(goDownRight, curRound), (goRight, curRound), \n\t(goUpRight, curRound)]\n\tfor (func, steps) in circle:\n\t\tif n >= steps:\n\t\t\tcurPoint = func(curPoint, steps)\n\t\t\tn -= steps\n\t\telse:\n\t\t\tcurPoint = func(curPoint, n)\n\t\t\tn = 0\n\t\t\treturn curPoint\n\tassert(False)\n\ndef quadraticEqPlus(a, b, c):\n\treturn (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)\n\n#print(quadraticEqPlus(3, 3, 0))\ndef goUpLeft(point, steps):\t\n\treturn (point[0] - steps, point[1] + 2 * steps)\n\ndef goLeft(point, steps):\t\n\treturn (point[0] - 2 * steps, point[1])\n\ndef goDownLeft(point, steps):\t\n\treturn (point[0] - steps, point[1] - 2 * steps)\n\ndef goDownRight(point, steps):\t\n\treturn (point[0] + steps, point[1] - 2 * steps)\n\ndef goRight(point, steps):\t\n\treturn (point[0] + 2 * steps, point[1])\n\ndef goUpRight(point, steps):\t\n\treturn (point[0] + steps, point[1] + 2 * steps)\n\nmain()\n#for n in range(21):\n#\tprint(solver(n))\n\n#print(solver(7))\n", "from math import sqrt\n\n\ndef hex(l):\n    return 1 + 3*l*(l+1)\n\n\ndef level(n):\n    if n == 0:\n        return 0, 0    \n    l = int((-3. + sqrt(9. + 12.*(n-1))) / 6.)\n    while hex(l) > n:\n        l -= 1\n    while hex(l+1) <= n:\n        l += 1\n    return l+1, n-hex(l)\n\n\ndef coordinates(l, k):\n    if l == 0:\n        return 0, 0\n    s, i = divmod(k, l)\n    if s == 0:\n        return 2*l - (i+1), 2*(i+1)\n    elif s == 1:\n        return l - 2*(i+1), 2*l\n    elif s == 2:\n        return -l - (i+1), 2*l-2*(i+1)\n    elif s == 3:\n        return -2*l + (i+1), -2*(i+1)\n    elif s == 4:\n        return -l + 2*(i+1), -2*l\n    elif s == 5:\n        return l + (i+1), -2*l+2*(i+1)\n\n\ndef ayrat(n):\n    l, k = level(n)\n    return coordinates(l, k)\n\n\ndef __starting_point():\n    n = int(input())\n    print(\"{} {}\".format(*ayrat(n)))\n\n__starting_point()", "#By Tianyi Chen\nn=int(input())\ndef j(i):\n\treturn 3*i*(i+1)<=n\nhigh=10**18;low=0\nwhile high-low>5:\n\tmid=high+low>>1\n\tif j(mid):low=mid\n\telse:high=mid\nwhile j(low+1):low+=1\nr=low\nx=r<<1;y=0\nn-=3*r*(r+1)\nr+=1\nif n:\n\tn-=1;x+=1;y+=2\nif n:\n\tsub=min(n,r-1);n-=sub;x-=sub;y+=sub<<1\nif n:\n\tsub=min(n,r);n-=sub;x-=sub<<1\nif n:\n\tsub=min(n,r);n-=sub;x-=sub;y-=sub<<1\nif n:\n\tsub=min(n,r);n-=sub;x+=sub;y-=sub<<1\nif n:\n\tsub=min(n,r);n-=sub;x+=sub<<1\nif n:\n\tsub=min(n,r);n-=sub;x+=sub;y+=sub<<1\nprint(x,y)", "# Contest: 21 - Codeforces Rating >= 2200 (https://a2oj.com/ladder?ID=21)\n# Problem: (25) Hexagons (Difficulty: 5) (http://codeforces.com/problemset/problem/615/E)\n\ndef rint():\n    return int(input())\n\n\ndef rints():\n    return list(map(int, input().split()))\n\n\nSIDES = [\n    lambda c, v: (1 + 2 * c - v, 2 + 2 * v),\n    lambda c, v: (-1 + c - 2 * v, 2 + 2 * c),\n    lambda c, v: (-c - 2 - v, 2 * c - 2 * v),\n    lambda c, v: (-1 - 2 * c + v, -2 - 2 * v),\n    lambda c, v: (1 - c + 2 * v, -2 - 2 * c),\n    lambda c, v: (2 + c + v, -2 * c + 2 * v),\n]\n\nn = rint()\nif n == 0:\n    print(0, 0)\n    return\nn -= 1\nl, h = 0, 10**9\nwhile h - l > 1:\n    m = (h + l) // 2\n    if 3 * m * (m + 1) > n:\n        h = m - 1\n    else:\n        l = m\nc = h if 3 * h * (h + 1) <= n else l\nn -= 3 * c * (c + 1)\n\nprint(*SIDES[n // (c + 1)](c, n % (c + 1)))\n", "def __starting_point():\n    n = int(input())\n    l, r = 1, 10 ** 9\n    x, mid = 0, 0\n    while l <= r:\n        mid = (l+r)//2\n        if 3*mid*(mid-1) <= n:\n            l = mid + 1\n            x = mid\n        else:\n            r = mid - 1\n    a, b = (n-3*x*(x-1))//x, (n-3*x*(x-1)) % x\n    q, w = 0, 0\n    if a == 0:\n        q, w = 2*x, 0\n        if b == 0:\n            q = 2*x - 2\n        else:\n            q += -b\n            w += 2*b\n    elif a == 1:\n        q, w = x-2*b, 2*x\n    elif a == 2:\n        q, w = -x-b, 2*x-2*b\n    elif a == 3:\n        q, w = -2*x+b, -2*b\n    elif a == 4:\n        q, w = -x+2*b, -2*x\n    elif a == 5:\n        q, w = x+b, -2*x+2*b\n    print(q, w)\n\n\n__starting_point()"]