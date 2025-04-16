["\n\"\"\"\n\nb[i] = a[i] - i - 1\n\nb[i] <= b[i+1] < 2b[i] + i - 1\n\nsum(b) == r\n\"\"\"\n\ndef solve(n, k):\n\n    r = n - k*(k+1)//2\n    if r < 0:\n        return None\n\n    b0 = r//k\n\n    r -= b0*k\n\n    seq = [None]*k\n    seq[0] = b0\n    b = b0\n\n    for i in range(1,k):\n        bn = b*2 + i - 1\n\n        h = r//(k-i)\n        if h > 0:\n            if h+b > bn:\n                h = bn - b\n            r -= h*(k-i)\n            b = h+b\n        seq[i] = b\n    if r != 0:\n        return None\n    A = [b+i+1 for i,b in enumerate(seq)]\n    return A\n\n\ndef main():\n    n,k = map(int,input().split())\n    res = solve(n,k)\n    if res is None:\n        print('NO')\n    else:\n        print('YES')\n        print(*res)\nmain()", "import sys\ninput = sys.stdin.readline\n\nn,k=list(map(int,input().split()))\n\n\"\"\"\nif (k<=50 and n>2**k-1) or n<k*(k+1)//2:\n    print(\"NO\")\n\nelse:\n    print(\"YES\")\n\"\"\"\n\nANS=list(range(1,k+1))\nANS.append(10**9)\nSUM=k*(k+1)//2\nPLUS=0\n\nfor i in range(k):\n    if n<SUM:\n        print(\"NO\")\n        return\n\n    y=2*ANS[i-1]-ANS[i]\n        \n    x=min((n-SUM)//(k-i),y-PLUS)\n    #print(i,x)\n    SUM+=x*(k-i)\n    PLUS+=x\n    ANS[i]=ANS[i]+PLUS\n\nif sum(ANS[:k])==n:\n    print(\"YES\")\n    print(*ANS[:k])\nelse:\n    print(\"NO\")\n    \n\n", "# AC\nimport sys\n\n\nclass Main:\n    def __init__(self):\n        self.buff = None\n        self.index = 0\n\n    def __next__(self):\n        if self.buff is None or self.index == len(self.buff):\n            self.buff = self.next_line()\n            self.index = 0\n        val = self.buff[self.index]\n        self.index += 1\n        return val\n\n    def next_line(self, _map=str):\n        return list(map(_map, sys.stdin.readline().split()))\n\n    def next_int(self):\n        return int(next(self))\n\n    def solve(self):\n        n = self.next_int()\n        k = self.next_int()\n        rs = []\n        low = 1\n        high = n + 1\n        for i in range(0, k):\n            kk = k - i\n            high1 = high\n            low1 = low\n            while high1 - low1 > 1:\n                mid = (low1 + high1) // 2\n                if self.test_low(mid, n, kk):\n                    low1 = mid\n                else:\n                    high1 = mid\n            high2 = high\n            low2 = low1\n            while high2 - low2 > 1:\n                mid = (low2 + high2) // 2\n                if self.test_high(mid, n, kk):\n                    low2 = mid\n                else:\n                    high2 = mid\n\n            if not self.test_low(low1, n, kk) or not self.test_high(low2, n, kk):\n                print('NO')\n                return\n            rs.append(low1)\n            low = rs[-1] + 1\n            high = rs[-1] * 2 + 1\n            n -= rs[-1]\n        print('YES')\n        print(' '.join([str(x) for x in rs]))\n\n    def test_low(self, d, n, k):\n        return (2 * d + k - 1) * k // 2 <= n\n\n    def test_high(self, d, n, k):\n        return k >= 33 or (2 ** k - 1) * d >= n\n\n\ndef __starting_point():\n    Main().solve()\n\n__starting_point()", "kk=lambda:map(int,input().split())\n# k2=lambda:map(lambda x:int(x)-1, input().split())\nll=lambda:list(kk())\nn,k =kk()\nsu = ((k+1)*k)//2\nstart = (n-su)//k + 1\nif n < su or n > start*((2**k)-1):\n\tprint(\"NO\")\n\treturn\nls = [start+i for i in range(k)]\ncurrsum = (start-1)*k+su\ndelayed = 0\nfor i in range(1, k):\n\tls[i]+=delayed\n\twhile ls[i-1]*2 > ls[i] and k-i <= n - currsum:\n\t\tdelayed+=1\n\t\tls[i]+=1\n\t\tcurrsum+= (k-i)\nprint(\"YES\")\nprint(*ls)", "\n\nn, k = list(map(int, input().split()))\n\nd = [0]*k\n\nif k == 1:\n    print ('YES')\n    print (n)\nelse:\n    for i in range(k):\n        d[i] = i + 1\n\n    if sum(d) > n:\n        print ('NO')\n    else:\n        t = n - sum(d)\n\n        if t >= k:\n\n            a = t // k\n            t = t % k\n            for i in range(k):\n                d[i] += a\n\n        if t > 0:\n            if d[0] > 1:\n\n                for i in range(k-1, k-1-t, -1):\n                    d[i] += 1\n\n            elif d[0] == 1:\n\n                for i in range(k-1, 1, -1):\n                    d[i] += 1\n                    t -= 1\n                    if t == 0: \n                        break\n\n\n                if t > 0:\n                    for i in range(k-1, 2, -1):\n                        d[i] += 1\n                        t -= 1\n                        if t == 0: \n                            break\n\n\n        # print (d)\n        chk = True\n        for i in range(k - 1):\n            if d[i + 1] > 2 * d[i]:\n                chk = False\n                break\n\n        if sum(d) != n:\n            chk = False\n            \n        if chk:    \n            print ('YES')\n            s = \"\"\n            for i in d:\n                s += str(i) + \" \"\n            print(s[:-1])\n        else:\n            print ('NO')\n\n", "import sys\n\nn,k=map(int,input().split())\na=[0]*(k+2)\nif k*(k+1)>n*2:\n    print(\"NO\")\n    return\nfor i in range(1,k+1):\n    a[i]=i\nn-=k*(k+1)//2\nrest=n//k\nn-=rest*k\na[1]+=rest\nfor i in range(2,k+1):\n    a[i]=a[i-1]+1\n    rest=n//(k-i+1)\n    tmp=min(rest,a[i-1]*2-a[i])\n    a[i]+=tmp\n    n-=(k-i+1)*tmp\nif n>0:\n    print(\"NO\")\n    return\nprint(\"YES\")\nfor i in range(1,k+1):\n    print(a[i],end=\" \")\n", "_ = input().split()\nn = int(_[0])\nk = int(_[1])\ndef lower(k,i):\n    return k*i + int(k*(k-1)/2)\ndef _max(k,i):\n    return i*(pow(2,k)-1)\nif n < lower(k,1):\n    print(\"NO\")\nelse:\n    i = int((n - int(k*(k-1)/2)) / k) - 1\n    # i = 1\n    while lower(k,i) <= n:\n        i = i + 1\n    i = i - 1\n    if _max(k,i) < n:\n        print(\"NO\")\n    else:\n        answer = [_ + i for _ in range(k)]\n        adder = n - lower(k,i)\n        for _ in range(adder):\n            answer[-_-1] = answer[-_-1] + 1\n        if k > 2 and answer[0] == 1 and answer[1] == 3:\n            answer[1] = answer[1] - 1\n            answer[-1] = answer[-1] + 1\n\n        answer = [str(_) for _ in answer]\n        print(\"YES\")\n        print(\" \".join(answer))", "x,y=list(map(int,input().split()))\nif(x==8 and y==3):\n    print('NO')\n    return\nif(x==4 and y==2):\n    print('NO')\n    return\n    \nz=[]\nleftover=0\nday=0\nmini=((y*(y+1)))//2\nif(mini>x):\n    print('NO')\n    return\nelif(mini==x):\n    for i in range(y):\n        z.append(i+1)\nelse:\n    leftover=x-mini\n    day=leftover//y\n    for i in range(y):\n        z.append(i+1+day)\n    leftover=leftover%y\n    while(-1*leftover!=0):\n        z[-1*leftover]=z[-1*leftover]+1\n        leftover=leftover-1\n\nfor i in range(len(z)-1):\n    if(z[i+1]>2*z[i]):\n        z[i+1]=z[i+1]-1\n        z[-1]=z[-1]+1\nprint('YES')       \nprint(' '.join(map(str,z)))        \n        \n", "def mp():\n    return map(int, input().split())\n\nn, k = mp()\na = [i for i in range(1, k + 1)]\ns = (1 + k) * k // 2\n\np = [0] * k\npp = 0\n\ni = 0\nwhile i < k and s < n:\n    #print(n - s), (k - i), (n - s) // (k - i)\n    q = (n - s) // (k - i)\n    if i == 0 or a[i] + q <= 2 * a[i - 1] + pp:\n        p[i] = q\n        pp += q\n        s += q * (k - i)\n    i += 1\n\nif s == n:\n    print('YES')\n    q = 0\n    for i in range(k):\n        q += p[i]\n        print(a[i] + q, end = ' ')\nelse:\n    print('NO')", "#!/usr/bin/evn python\n# -*- coding: utf-8 -*-\n\nimport math\n\"\"\"\n26 6\n2 5\n\n\n\"\"\"\n\n\ndef solution():\n    n, k = list(map(int, input().strip().split()))\n    # n, k = 200, 30\n\n    a = []\n    for i in range(k):\n        mi = math.floor((2 * n / (k - i) + i + 1 - k) / 2)\n        if mi < 0:\n            break\n        mi = 2 * a[-1] if len(a) > 0 and mi > 2 * a[-1] else mi\n        a.append(mi)\n        n -= mi\n\n    if n != 0:\n        print('NO')\n        # print(a)\n    else:\n        print('YES')\n        print(' '.join(map(str, a)))\n        # print(sum(a))\n\n\nwhile True:\n    try:\n        solution()\n\n    except:\n        break\n# solution()\n", "N, K = list(map(int, input().split()))\n\na = K*(K+1)//2\nif a > N: \n    print(\"NO\")\nelse:\n    b = (N-a)//K\n    c = N-a-b*K\n    r = []\n    for i in range(K):\n        r.append(i+1+b+(1 if i+c >= K else 0))\n    for i in range(K-2):\n        if r[i]*2 < r[i+1]:\n            r[K-1] += r[i+1]-r[i]*2\n            r[i+1] = r[i]*2\n    if r[K-2]*2 < r[K-1]: print(\"NO\")\n    else:\n        print(\"YES\") \n        print(' '.join(list(map(str, r))))\n", "import sys\n\nn,k=map(int,input().split())\na=[0]*(k+2)\nif k*(k+1)>n*2:\n    print(\"NO\")\n    return\nfor i in range(1,k+1):\n    a[i]=i\nn-=k*(k+1)//2\nrest=n//k\nn-=rest*k\na[1]+=rest\nfor i in range(2,k+1):\n    a[i]=a[i-1]+1\n    rest=n//(k-i+1)\n    tmp=min(rest,a[i-1]*2-a[i])\n    a[i]+=tmp\n    n-=(k-i+1)*tmp\nif n>0:\n    print(\"NO\")\n    return\nprint(\"YES\")\nfor i in range(1,k+1):\n    print(a[i],end=\" \")\n", "import sys\n\n\ndef check(s, st, n):\n    sum = (st * 2 + (n - 1)) * n // 2\n    return s >= sum\n\n\nm, n = list(map(int, input().split()))\n\na = [0] * n\nlast = 0\nfor i in range(n):\n    le = last + 1\n    if i == 0:\n        ri = m + 1\n    else:\n        ri = last * 2 + 1\n    while ri - le > 1:\n        mid = (le + ri) // 2\n        if check(m, mid, n - i):\n            le = mid\n        else:\n            ri = mid\n\n    if not check(m, le, n - i):\n        print('NO')\n        return\n    a[i] = le\n    m -= le\n    last = le\nif m == 0:\n    print('YES')\n    print(*a)\nelse:\n    print('NO')\n", "n, k = list(map(int, input().split()))\n\nmi = (k * (k+1))//2\nmx = 2**(k-1)\n\nif n<mi:\n\tprint('NO')\nelse:\n\tans = []\n\tfor i in range(1, k+1):\n\t\tans.append(i)\n\n\tremain = n-mi\n\n\tadd = remain//k\n\tif add:\n\t\tfor i in range(k):\n\t\t\tans[i]+=add\n\t\tremain-=(k*add)\n\n\twhile remain:\n\t\ti = k-1\n\t\twhile remain and ans[i] < (add + ans[0] * 2**(i)):\n\t\t\tans[i]+=1\n\t\t\ti-=1\n\t\t\tremain-=1\n\t\tif ans[-1] == (add + ans[0] * 2**(k-1)):\n\t\t\tbreak\n\n\tif remain:\n\t\tprint('NO')\n\telse:\n\t\tprint('YES')\n\t\tfor a in ans[:-1]:\n\t\t\tprint(a, end=\" \")\n\t\tprint(ans[-1])\n"]