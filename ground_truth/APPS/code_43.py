["from math import *\n# stores counterclockwise angle between vector (1,0) and each vector in a\na = []\nn = int(input())\nfor i in range(n):\n    x,y = list(map(int,input().split()))\n    # calculate counterclockwise angle between (1,0) and this vector\n    t = acos(x/sqrt(x**2+y**2))\n    a.append((i+1,[2*pi-t,t][y>=0],x,y))\ncmp = lambda x:x[1]\na = sorted(a,key=cmp)\n# construct pairs for adjacent vectors\nb = []\nfor i in range(n):\n    i1,i2 = a[i][0],a[(i+1)%n][0]\n    x1,y1 = a[i][2:]\n    x2,y2 = a[(i+1)%n][2:]\n    inner_prod = x1*x2 + y1*y2\n    inner_prod *= abs(inner_prod)\n    norm_prod = ((x1**2+y1**2)*(x2**2+y2**2))\n    b.append((i1,i2,inner_prod,norm_prod))\n# find the nearest vector\nbetter = lambda p1,p2: p1[2]*p2[3]>p2[2]*p1[3]\nans = b[-1]\nfor i in range(n):\n    if better(b[i],ans):\n        ans = b[i]\nprint(ans[0],ans[1])\n", "import sys\n# sys.stdin = open('ivo.in')\n\n\ndef getkos(x, y):\n    temp = (x[0] * y[0] + x[1] * y[1])\n    mul = -1 if temp < 0 else 1\n    return (mul * temp ** 2, (x[0] ** 2 + x[1] ** 2) * (y[0] ** 2 + y[1] ** 2))\n\nclass Drob:\n    def __init__(self, num, denom):\n        self.num = num\n        self.denom = denom\n\n    def __lt__(self, object):\n        return self.num * object.denom < object.num * self.denom\n\nn = int(sys.stdin.readline())\n\npositive = []\nnegative = []\nfor i in range(n):\n    x = tuple(map(int, sys.stdin.readline().split())) + (i,)\n    if x[1] > 0:\n        positive.append(x)\n    else:\n        negative.append(x)\n\npositive.sort(key=lambda x: Drob((-1 if x[0] > 0 else 1) * x[0]**2 , (x[1] ** 2 +  x[0] ** 2)))\nnegative.sort(key=lambda x: Drob((1 if x[0] > 0 else -1) * x[0]**2 , (x[1] ** 2 +  x[0] ** 2)))\n#negative.sort(key=lambda x,y: x[0] - y[0] if x[0] != y[0] else (y[1] - x[1]) * x[0])\n\nall = positive + negative\n# print(all)\nbiggest = [-1.1, 1]\nbi = 0\nbj = 1\nfor i in range(n):\n    nxt = (i + 1) % n\n    prev = (i + n - 1) % n\n\n    kos1 = getkos(all[i], all[nxt])\n    if kos1[1] * biggest[0] < kos1[0] * biggest[1]:\n        biggest = kos1\n        bi = all[i][2]\n        bj = all[nxt][2]\n    kos2 = getkos(all[i], all[prev])\n    if kos2[1] * biggest[0] < kos2[0] * biggest[1]:\n        biggest = kos2\n        bi = all[i][2]\n        bj = all[prev][2]\n    # print(\"{} kos1: {} kos2: {}\".format(i, kos1, kos2))\n\n# print(biggest)\nprint(\"%d %d\" % (bi + 1, bj+ 1))\n", "import sys\n# sys.stdin = open('ivo.in')\n\n\ndef getkos(x, y):\n    temp = (x[0] * y[0] + x[1] * y[1])\n    mul = -1 if temp < 0 else 1\n    return (mul * temp ** 2, (x[0] ** 2 + x[1] ** 2) * (y[0] ** 2 + y[1] ** 2))\n\nclass Drob:\n    def __init__(self, num, denom):\n        self.num = num\n        self.denom = denom\n\n    def __lt__(self, object):\n        return self.num * object.denom < object.num * self.denom\n\nn = int(sys.stdin.readline())\n\npositive = []\nnegative = []\nfor i in range(n):\n    x = tuple(map(int, sys.stdin.readline().split())) + (i,)\n    if x[1] > 0:\n        positive.append(x)\n    else:\n        negative.append(x)\n\npositive.sort(key=lambda x: ((-1 if x[0] > 0 else 1) * x[0]**2 / (x[1] ** 2 +  x[0] ** 2)))\nnegative.sort(key=lambda x: ((1 if x[0] > 0 else -1) * x[0]**2 / (x[1] ** 2 +  x[0] ** 2)))\n#negative.sort(key=lambda x,y: x[0] - y[0] if x[0] != y[0] else (y[1] - x[1]) * x[0])\n\nall = positive + negative\n# print(all)\nbiggest = [-1.1, 1]\nbi = 0\nbj = 1\nfor i in range(n):\n    nxt = (i + 1) % n\n    prev = (i + n - 1) % n\n\n    kos1 = getkos(all[i], all[nxt])\n    if kos1[1] * biggest[0] < kos1[0] * biggest[1]:\n        biggest = kos1\n        bi = all[i][2]\n        bj = all[nxt][2]\n    kos2 = getkos(all[i], all[prev])\n    if kos2[1] * biggest[0] < kos2[0] * biggest[1]:\n        biggest = kos2\n        bi = all[i][2]\n        bj = all[prev][2]\n    # print(\"{} kos1: {} kos2: {}\".format(i, kos1, kos2))\n\n# print(biggest)\nprint(\"%d %d\" % (bi + 1, bj+ 1))\n", "from math import atan2\n\n\ndef dot(a, b):\n    return a[0]*b[0] + a[1]*b[1]\n\n\ndef cross(a, b):\n    return a[0]*b[1] - a[1]*b[0]\n\n\nn = int(input())\na = []\n\nfor i in range(0, n):\n    [x, y] = map(int, input().split())\n    a.append([i + 1, [x, y]])\n\n\na.sort(key=lambda x: atan2(x[1][0], x[1][1]))\na.append(a[0])\n\nfor i in range(1, len(a)):\n    a[i-1].append([dot(a[i-1][1], a[i][1]), abs(cross(a[i-1][1], a[i][1]))])\n\nbest = a[0]\nma = [a[0][0], a[1][0]]\n\nfor i in range(1, len(a)):\n    if cross(a[i][2], best[2]) > 0:\n        best = a[i]\n        ma = [a[i][0], a[i+1][0]]\n\nprint(ma[0], ma[1])", "from math import atan2\n\n\ndef dot(a, b):\n    return a[0]*b[0] + a[1]*b[1]\n\n\ndef cross(a, b):\n    return a[0]*b[1] - a[1]*b[0]\n\n\nn = int(input())\na = []\n\nfor i in range(0, n):\n    [x, y] = list(map(int, input().split()))\n    a.append([i + 1, [x, y]])\n\n\na.sort(key=lambda x: atan2(x[1][0], x[1][1]))\na.append(a[0])\n\nfor i in range(1, len(a)):\n    a[i-1].append([dot(a[i-1][1], a[i][1]), abs(cross(a[i-1][1], a[i][1]))])\n\nbest = a[0]\nma = [a[0][0], a[1][0]]\n\nfor i in range(1, len(a)):\n    if cross(a[i][2], best[2]) > 0:\n        best = a[i]\n        ma = [a[i][0], a[i+1][0]]\n\nprint(ma[0], ma[1])\n", "from functools import cmp_to_key\nfrom math import atan2\n\ndef skal(a, b):\n    return a[0][0] * b[0][0] + a[0][1] * b[0][1]\n\n\ndef vect(a, b):\n    #print(a, b, a[0][0] * b[0][1] - b[0][0] * a[0][1])\n    return a[0][0] * b[0][1] - b[0][0] * a[0][1]\n\n\ndef top(a):\n    if a[0][1] < 0 or (a[0][1] == 0 and a[0][0] < 0):\n        return 1\n    else:\n        return -1\n\n\ndef myfun(a, b):\n    if top(a) != top(b):\n        return top(a)\n\n    if vect(a, b) > 0:\n        return 1\n    else:\n        return -1\n\nn = int(input())\na = []\nfor i in range(n):\n    x, y = map(int, input().split())\n    a.append([[x, y], i + 1])\n#a.sort(key = cmp_to_key(myfun))\na.sort(key = lambda x: atan2(x[0][1],x[0][0]))\na.append(a[0])\n#print(a)\nc = [[skal(a[0],a[1]),abs(vect(a[0],a[1]))],[a[0][1],a[1][1]]]\nfor i in range(1, n):\n    d = [[skal(a[i],a[i+1]),abs(vect(a[i],a[i+1]))],[a[i][1],a[i+1][1]]]\n    if vect(d, c) > 0:\n        c = d\nprint(c[1][0],c[1][1])\n\n\"\"\"\n3\n1 -1\n1 1 \n-1 0\n\n4\n1 -1\n1 1\n-1 0\n-1 -1\n\"\"\"", "from math import atan2\n\ndef skal(a, b):\n    return a[0][0] * b[0][0] + a[0][1] * b[0][1]\n\n\ndef vect(a, b):    \n    return a[0][0] * b[0][1] - b[0][0] * a[0][1]\n\n\nn = int(input())\na = []\nfor i in range(n):\n    x, y = list(map(int, input().split()))\n    a.append([[x, y], i + 1])\na.sort(key = lambda x: atan2(x[0][1],x[0][0]))\na.append(a[0])\nc = [[skal(a[0],a[1]),abs(vect(a[0],a[1]))],[a[0][1],a[1][1]]]\nfor i in range(1, n):\n    d = [[skal(a[i],a[i+1]),abs(vect(a[i],a[i+1]))],[a[i][1],a[i+1][1]]]\n    if vect(d, c) > 0:\n        c = d\nprint(c[1][0],c[1][1])\n", "from math import *\nn = int(input())\ndx1 = 0\ndx2 = 0\ndy1 = 0\ndy2 = 0\na = []\nfor i in range(n):\n    x,y = [int(x) for x in input().split()]\n    a.append([x,y,i])\na.sort(key = lambda item: atan2(item[1],item[0]))\na.append(a[0])\ndx1 = (a[0][0]*a[1][0]+a[0][1]*a[1][1])\ndy1 = abs(a[0][0]*a[1][1]-a[1][0]*a[0][1])\nminx = (dx1)\nminy = abs(dy1)\nmin1,min2 = a[0][2],a[1][2]\nfor i in range(1,len(a)):\n    dx2 = (a[i-1][0]*a[i][0]+a[i-1][1]*a[i][1])\n    dy2 = abs(a[i-1][0]*a[i][1]-a[i][0]*a[i-1][1])\n    if (dx2*miny-dy2*minx)>0:\n        min1,min2=a[i-1][2],a[i][2]\n        minx = dx2\n        miny = dy2\nprint(min1+1,min2+1)\n\n        \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    \n    \n", "import math as m\nclass Point(object):\n    def __init__(self, x, y, id):\n        self.X = x\n        self.Y = y\n        self.id = id\ndef scalar(x1, y1, x2, y2):\n    return x1*x2 + y1*y2\ndef vector(x1, y1, x2, y2):\n    return x1 * y2 - x2 * y1\nn = int(input())\ndx2 = 0\ndy2 = 0\na = []\nfor i in range(n):\n    x, y = [int(j) for j in input().split()]\n#a.append([x,y,i])\n    a.append(Point(x, y, i + 1))\na.sort(key=lambda item: m.atan2(item.Y, item.X))\na.append(a[0])\nminx = scalar(a[0].X, a[0].Y, a[1].X, a[1].Y)\nminy = abs(vector(a[0].X, a[0].Y, a[1].X, a[1].Y))\nmin1, min2 = a[0].id, a[1].id\nfor i in range(1, len(a)):\n    dx2 = scalar(a[i-1].X, a[i-1].Y, a[i].X, a[i].Y)\n    dy2 = abs(vector(a[i-1].X, a[i-1].Y, a[i].X, a[i].Y))\n    if vector(dx2, dy2, minx, miny) > 0:\n        min1, min2 = a[i-1].id, a[i].id\n        minx = dx2\n        miny = dy2\nprint(min1, min2)\n\"\"\"\nn = int(input())\nfor i in range(n):\n    x, y = input().split()\n    a.append(Point(int(x), int(y), i+1))\na.sort(key=lambda points: m.atan2(points.X, points.Y))\n''''''\nmindx = abs(scalar(a[0], a[n-1]))\nmindy = abs(vector(a[0], a[n-1]))\nnomber1 = a[0].id\nnomber2 = a[n-1].id\n\nfor i in range(n-1):\n    dx = abs(scalar(a[i], a[i+1]))\n    dy = abs(vector(a[i], a[i+1]))\n    if vectorCoordinate(dx, dy, mindy, mindx) > 0:\n        mindx = dx\n        mindy = dy\n        nomber1 = a[i].id\n        nomber2 = a[i+1].id\nprint(nomber2, nomber1)\"\"\"\n\n", "from math import atan2\n\ns = lambda a, b: a[0] * b[0] + a[1] * b[1]\nv = lambda a, b: a[0] * b[1] - a[1] * b[0]\n\np = []\nfor i in range(int(input())):\n    x, y = map(int, input().split())\n    p.append((atan2(x, y), (x, y), i + 1))\np.sort()\n\nd = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]\nx = d[0]\n\nfor y in d:\n    if v(y[:2], x[:2]) > 0: x = y\n\nprint(x[2], x[3])", "from collections import namedtuple\nfrom math import sqrt\nfrom functools import cmp_to_key\nVec = namedtuple(\"Vec\", \"x y index\")\nFraction = namedtuple(\"Fraction\", \"num denom\")\n\ndef fraction_comp(a, b):\n    return a.num*b.denom > b.num*a.denom\n\ndef angle_comp(v):\n    result = v.x / sqrt(v.x*v.x + v.y*v.y)\n    if (v.y < 0):\n        result = -2 - result\n    return result\n\ndef angle(v1, v2):\n    x1, y1 = v1.x, v1.y\n    x2, y2 = v2.x, v2.y\n    result = (x1*x2 + y1*y2) / (sqrt(x1*x1 + y1*y1)*sqrt(x2*x2 + y2*y2))\n    sign = -1 if (x1*x2 + y1*y2) < 0 else 1\n    return Fraction(sign*(x1*x2 + y1*y2)**2, (x1*x1 + y1*y1)*(x2*x2 + y2*y2))\n\nn = int(input())\n\npoints = []\nfor i in range(n):\n    x, y = tuple(map(int, input().split()))\n    points.append(Vec(x, y, i))\n\npoints.sort(key=angle_comp)\npoints.reverse()\n\nans = (points[0].index + 1, points[n - 1].index + 1)\nminAngleCos = angle(points[0], points[n - 1])\n\nfor i in range(n - 1):\n    currAngleCos = angle(points[i], points[i + 1])\n    if (fraction_comp(currAngleCos, minAngleCos)):\n        minAngleCos = currAngleCos\n        ans = (points[i].index + 1, points[i + 1].index + 1)\n\nprint(ans[0], ans[1], sep=' ')", "# a1 <=> a2: \n# cos, cos^2 (0-90), val (0-360)\n\nV, N, X, Y, L = list(range(5))\n\ndef sec(x, y):\n\tif x>0 and y>=0:\n\t\ts = 1\n\telif x<=0 and y>0:\n\t\ts = 2\n\telif x<0 and y<=0:\n\t\ts = 3\n\telse:\n\t\ts = 4\n\treturn s\n\ndef val(a, b, s):\n\t# a/b+c = (a+bc)/b\n\tif s == 1:\n\t\t# 1 - a/b\n\t\ta = -a + b\n\telif s == 2:\n\t\t# 2 + a/b - 1 = a/b + 1\n\t\ta = a + b\n\telif s == 3:\n\t\t# 3 - a/b\n\t\ta = -a + 3*b\n\telse:\n\t\t# 4 + a/b - 1 = a/b + 3\n\t\ta = a + 3*b\n\treturn a/b\n\t\ndef vec(n, x, y):\n\t# cos = x/sqrt(xx+yy)\n\ta = x*x\n\tb = l = x*x + y*y\n\ts = sec(x, y)\n\tv = val(a, b, s)\n\treturn (v, n, x, y, l)\n\t\ndef ang(v1, v2):\n\t# cos = (v1,v2) / |v1||v2|\n\tv = v1[X] * v2[X] + v1[Y] * v2[Y]\n\ts = 1 if v > 0 else 2\n\ta = v * v\n\tb = v1[L] * v2[L]\n\treturn val(a, b, s)\n\t\ndef quiz():\t\t\n\tn = int(input())\n\ta = []\n\tfor i in range(n):\n\t\tx, y = list(map(int, input().split()))\n\t\ta.append(vec(i+1,x,y))\n\n\ta.sort(key=lambda x: x[V])\n\t\n\timin, vmin = 0, 3\n\tfor i in range(0, n):\n\t\tv = ang(a[i-1], a[i])\n\t\tif v < vmin:\n\t\t\tvmin = v\n\t\t\timin = i\n\t\n\tprint(a[imin-1][N], a[imin][N])\n\t\nquiz()\n", "from math import atan2\n\ns = lambda a, b: a[0] * b[0] + a[1] * b[1]\nv = lambda a, b: a[0] * b[1] - a[1] * b[0]\n\np = []\nfor i in range(int(input())):\n    x, y = list(map(int, input().split()))\n    p.append((atan2(x, y), (x, y), i + 1))\np.sort()\n\nd = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]\nx = d[0]\n\nfor y in d:\n    if v(y[:2], x[:2]) > 0: x = y\n\nprint(x[2], x[3])\n", "from math import atan2\n\ns = lambda a, b: a[0] * b[0] + a[1] * b[1]\nv = lambda a, b: a[0] * b[1] - a[1] * b[0]\n\np = []\nfor i in range(int(input())):\n    x, y = list(map(int, input().split()))\n    p.append((atan2(x, y), (x, y), i + 1))\np.sort()\n\nd = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]\nx = d[0]\n\nfor y in d:\n    if v(y[:2], x[:2]) > 0: x = y\n\nprint(x[2], x[3])\n", "from math import atan2\n\ns = lambda a, b: a[0] * b[0] + a[1] * b[1]\nv = lambda a, b: a[0] * b[1] - a[1] * b[0]\n\np = []\nfor i in range(int(input())):\n    x, y = list(map(int, input().split()))\n    p.append((atan2(x, y), (x, y), i + 1))\np.sort()\n\nd = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]\nx = d[0]\n\nfor y in d:\n    if v(y[:2], x[:2]) > 0: x = y\n\nprint(x[2], x[3])\n", "from math import atan2\n\ns = lambda a, b: a[0] * b[0] + a[1] * b[1]\nv = lambda a, b: a[0] * b[1] - a[1] * b[0]\n\np = []\nfor i in range(int(input())):\n    x, y = list(map(int, input().split()))\n    p.append((atan2(x, y), (x, y), i + 1))\np.sort()\n\nd = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]\nx = d[0]\n\nfor y in d:\n    if v(y[:2], x[:2]) > 0: x = y\n\nprint(x[2], x[3])\n", "from math import atan2\n\ns = lambda a, b: a[0] * b[0] + a[1] * b[1]\nv = lambda a, b: a[0] * b[1] - a[1] * b[0]\n\np = []\nfor i in range(int(input())):\n    x, y = list(map(int, input().split()))\n    p.append((atan2(x, y), (x, y), i + 1))\np.sort()\n\nd = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]\nx = d[0]\n\nfor y in d:\n    if v(y[:2], x[:2]) > 0: x = y\n\nprint(x[2], x[3])\n", "from math import atan2\n\ns = lambda a, b: a[0] * b[0] + a[1] * b[1]\nv = lambda a, b: a[0] * b[1] - a[1] * b[0]\n\np = []\nfor i in range(int(input())):\n    x, y = list(map(int, input().split()))\n    p.append((atan2(x, y), (x, y), i + 1))\np.sort()\n\nd = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]\nx = d[0]\n\nfor y in d:\n    if v(y[:2], x[:2]) > 0: x = y\n\nprint(x[2], x[3])\n", "from math import atan2\n\ns = lambda a, b: a[0] * b[0] + a[1] * b[1]\nv = lambda a, b: a[0] * b[1] - a[1] * b[0]\n\np = []\nfor i in range(int(input())):\n    x, y = list(map(int, input().split()))\n    p.append((atan2(x, y), (x, y), i + 1))\np.sort()\n\nd = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]\nx = d[0]\n\nfor y in d:\n    if v(y[:2], x[:2]) > 0: x = y\n\nprint(x[2], x[3])\n", "from functools import cmp_to_key\n\nn = int(input())\n\ndef dot(p1,p2):\n    x1,y1 = p1\n    x2,y2 = p2\n    return x1 * x2 + y1 * y2\n    \ndef cross(p1,p2):\n    x1,y1 = p1\n    x2,y2 = p2\n    return x1 * y2 - x2 * y1\n\ndef top(p):\n    x,y = p\n    return y > 0 or (y == 0 and x > 0)\n\ndef polarCmp(p1,p2):\n    res = False\n    ta = top(p1)\n    tb = top(p2)\n    if (ta != tb):\n        res = ta\n    else:\n        res = cross(p1,p2) > 0\n    return -1 if res else 1\n\ndef angleLess(a1, b1, a2, b2):\n    p1 = (dot(a1, b1), abs(cross(a1, b1)))\n    p2 = (dot(a2, b2), abs(cross(a2, b2)))\n    return cross(p1, p2) > 0\n\n\nvals = []\nfor _ in range(n):\n    x, y = list(map(int, input().split()))\n    vals.append( (x,y) )\n    \nsvals = sorted(vals,key = cmp_to_key(polarCmp))\n\nidx1,idx2 = 0,1\nfor k in range(2,n):\n   if angleLess(svals[k-1],svals[k],svals[idx1],svals[idx2]):\n       idx1,idx2 = k-1,k\nif angleLess(svals[n-1],svals[0],svals[idx1],svals[idx2]):\n    idx1,idx2 = n-1,0\n\nres1 = res2 = -1\nfor k in range(n):\n    if vals[k] == svals[idx1]:\n        res1 = k\n    if vals[k] == svals[idx2]:\n        res2 = k\n\nprint(res1+1, res2+1)\n", "from math import atan2\n\n\n\ns = lambda a, b: a[0] * b[0] + a[1] * b[1]\n\nv = lambda a, b: a[0] * b[1] - a[1] * b[0]\n\n\n\np = []\n\nfor i in range(int(input())):\n\n    x, y = list(map(int, input().split()))\n\n    p.append((atan2(x, y), (x, y), i + 1))\n\np.sort()\n\n\n\nd = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]\n\nx = d[0]\n\n\n\nfor y in d:\n\n    if v(y[:2], x[:2]) > 0: x = y\n\n\n\nprint(x[2], x[3])\n\n\n\n\n# Made By Mostafa_Khaled\n", "import sys\nfrom math import atan2\n\ndef get_array(): return list(map(int, sys.stdin.readline().split()))\ndef get_ints(): return map(int, sys.stdin.readline().split())\ndef input(): return sys.stdin.readline().strip('\\n')\n\n\ndef dotp(a,b):\n    return a[0]*b[0] + a[1]*b[1]\n\ndef crossp(a,b):\n    return abs(a[0]*b[1]-a[1]*b[0])\n\nn = int(input())\nl = []\nfor i in range(n):\n    x,y = get_ints()\n    l.append((x,y,i+1))\n\nl.sort(key = lambda x : atan2(x[1],x[0]))\n\nl.append(l[0])\n\na = l[0][:2]\nb = l[1][:2]\nx = l[0][2]\ny = l[1][2]\n\ndot , cross = dotp(a,b) , crossp(a,b)\nmx , my = dot , cross\nfor i in range(1,n+1):\n    a = l[i-1][:2]\n    b = l[i][:2]\n    ndot , ncross = dotp(a,b) ,crossp(a,b)\n\n    if ndot*my - ncross*mx > 0:\n        x = l[i-1][2]\n        y = l[i][2]\n        mx = ndot\n        my = ncross\nprint(x,y)", "# FSX sb\n\n\ndef work():\n    def dot(x, y):\n        return x[0]*y[0]+x[1]*y[1]\n    n = int(input())\n    p = []\n    for i in range(n):\n        x, y = list(map(int, input().split(' ')))\n        k = (20000 if y > 0 else -20000) if x == 0 else y / x\n        l2 = x * x + y * y\n        p.append((x, y, i+1, x >= 0, k, l2))\n    p.sort(key=lambda item: (item[3], item[4]))\n    p.append(p[0])\n    ans1 = p[0][2]\n    ans2 = p[1][2]\n    ans_up = dot(p[0], p[1])\n    ans_down = p[0][5]*p[1][5]\n    for i in range(1, n):\n        now_up = dot(p[i], p[i+1])\n        now_down = p[i][5]*p[i+1][5]\n        if (now_up >= 0 and ans_up <= 0) or (now_up > 0 and ans_up > 0 and (now_up * now_up * ans_down > ans_up * ans_up * now_down)) or (now_up < 0 and ans_up < 0 and (now_up * now_up * ans_down < ans_up * ans_up * now_down)):\n            ans_up = now_up\n            ans_down = now_down\n            ans1 = p[i][2]\n            ans2 = p[i + 1][2]\n    print(ans1, ans2)\n\n\ndef __starting_point():\n    work()\n\n__starting_point()", "# FSX sb\n\n\ndef work():\n    def dot(x, y):\n        return x[0]*y[0]+x[1]*y[1]\n    n = int(input())\n    p = []\n    for i in range(n):\n        x, y = list(map(int, input().split(' ')))\n        k = (20000 if y > 0 else -20000) if x == 0 else y / x\n        l2 = x * x + y * y\n        p.append((x, y, i+1, x >= 0, k, l2))\n    p.sort(key=lambda item: (item[3], item[4]))\n    p.append(p[0])\n    ans1 = p[0][2]\n    ans2 = p[1][2]\n    ans_up = dot(p[0], p[1])\n    ans_down = p[0][5]*p[1][5]\n    for i in range(1, n):\n        now_up = dot(p[i], p[i+1])\n        now_down = p[i][5]*p[i+1][5]\n        if (now_up >= 0 and ans_up <= 0) or (now_up > 0 and ans_up > 0 and (now_up * now_up * ans_down > ans_up * ans_up * now_down)) or (now_up < 0 and ans_up < 0 and (now_up * now_up * ans_down < ans_up * ans_up * now_down)):\n            ans_up = now_up\n            ans_down = now_down\n            ans1 = p[i][2]\n            ans2 = p[i + 1][2]\n    print(ans1, ans2)\n\n\ndef __starting_point():\n    work()\n\n\n__starting_point()", "from functools import cmp_to_key\nn = int(input())\nx = [0 for i in range(n)]\ny = [0 for i in range(n)]\nfor i in range(n):\n    x[i], y[i] = list(map(int, input().strip().split(\" \")))\n\nvp = []\nvm = []\nfor i in range(n):\n    if y[i] >= 0:\n        vp.append(i)\n    else:\n        vm.append(i)\n\n\ndef cmp1(i, j):\n    xi = (1 if x[i] > 0 else -1)\n    xj = (1 if x[j] > 0 else -1)\n    b = xi * x[i] * x[i] * (x[j] * x[j] + y[j] * y[j]) > xj * x[j] * x[j] * (x[i] * x[i] + y[i] * y[i])\n    return (-1 if b else 1)\n\n\ndef cmp2(i, j):\n    xi = (1 if x[i] > 0 else -1)\n    xj = (1 if x[j] > 0 else -1)\n    b = xi * x[i] * x[i] * (x[j] * x[j] + y[j] * y[j]) < xj * x[j] * x[j] * (x[i] * x[i] + y[i] * y[i])\n    return (-1 if b else 1)\n\n\nvp = sorted(vp, key=cmp_to_key(cmp1))\nvm = sorted(vm, key=cmp_to_key(cmp2))\nvp = vp + vm\nvp.append(vp[0])\n\na = 0\nb = 0\nman = -2\nmad = 1\nfor i in range(n):\n    j = vp[i]\n    k = vp[i + 1]\n    tan = x[j] * x[k] + y[j] * y[k]\n    p = (tan > 0)\n    tan = tan * tan * (1 if p else -1)\n    tad = (x[j] * x[j] + y[j] * y[j]) * (x[k] * x[k] + y[k] * y[k])\n    if man * tad < tan * mad:\n        man = tan\n        mad = tad\n        a = j\n        b = k\n\n\nprint(\"{} {}\".format(a + 1, b + 1))\n"]