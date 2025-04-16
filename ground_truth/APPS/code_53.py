["# AC\nimport sys\n\n\nclass Main:\n    def __init__(self):\n        self.buff = None\n        self.index = 0\n\n    def __next__(self):\n        if self.buff is None or self.index == len(self.buff):\n            self.buff = sys.stdin.readline().split()\n            self.index = 0\n        val = self.buff[self.index]\n        self.index += 1\n        return val\n\n    def next_int(self):\n        return int(next(self))\n\n    def solve(self):\n        n = self.next_int()\n        x = [self.next_int() for _ in range(0, n)]\n        d = 0\n        l = 0\n        r = n - 1\n        rs = []\n        while l <= r:\n            if x[l] <= d and x[r] <= d:\n                break\n            if x[l] <= d:\n                rs.append('R')\n                d = x[r]\n                r -= 1\n            elif x[r] <= d:\n                rs.append('L')\n                d = x[l]\n                l += 1\n            elif x[r] < x[l] or l == r:\n                rs.append('R')\n                d = x[r]\n                r -= 1\n            elif x[l] < x[r]:\n                rs.append('L')\n                d = x[l]\n                l += 1\n            else:\n                ll = l + 1\n                while x[ll] > x[ll - 1]:\n                    ll += 1\n                rr = r - 1\n                while x[rr] > x[rr + 1]:\n                    rr -= 1\n                if ll - l > r - rr:\n                    rs.append('L')\n                    d = x[l]\n                    l += 1\n                else:\n                    rs.append('R')\n                    d = x[r]\n                    r -= 1\n        print(len(rs))\n        print(''.join(rs))\n\n\ndef __starting_point():\n    Main().solve()\n\n__starting_point()", "from collections import deque\nn = int(input())\nA = list(map(int, input().split()))\nA = deque(A)\nans = ''\nlast = 0\nwhile len(A) and (A[0] > last or A[-1] > last):\n    if len(A) == 1:\n        ans += 'R'\n        break\n    if A[0] > last and A[-1] > last:\n        if A[0] < A[-1]:\n            last = A[0]\n            A.popleft()\n            ans += 'L'\n        elif A[-1] < A[0]:\n            last = A[-1]\n            A.pop()\n            ans += 'R'\n        else:\n            lal = last\n            cnt1 = -1\n            for i in A:\n                cnt1 += 1\n                if i > lal:\n                    lal = i\n                else:\n                    break\n            lol = last\n            cnt2 = -1\n            for i in range(len(A) - 1, -1, -1):\n                cnt2 += 1\n                if A[i] > lol:\n                    lol = A[i]\n                else:\n                    break\n            if cnt1 > cnt2:\n                ans += 'L' * cnt1\n            else:\n                ans += 'R' * cnt2\n            break\n    else:\n        if A[0] > last:\n            last = A[0]\n            A.popleft()\n            ans += 'L'\n        else:\n            last = A[-1]\n            A.pop()\n            ans += 'R'\nprint(len(ans))\nprint(ans)\n", "from collections import deque\n\ndef solve(A):\n    res = []\n    last = 0\n    while A:\n        if max(A[0],A[-1]) <= last:\n            return res\n\n        if A[0] == A[-1]:\n            v = A[0]-1\n            for i,a in enumerate(A):\n                if v < a:\n                    v = a\n                else:\n                    break\n            else:\n                i += 1\n            L = i\n            v = A[-1]-1\n            for i,a in enumerate(reversed(A)):\n                if v < a:\n                    v = a\n                else:\n                    break\n            else:\n                i += 1\n            R = i\n            _,op = max((L, ['L']*L), (R, ['R']*R))\n            res.extend(op)\n            return res\n        \n        v, op = min((v, op) for v,op in ((A[0], 'L'), (A[-1], 'R')) if v > last)\n        last = v\n        res.append(op)\n        if op == 'L':\n            A.popleft()\n        else:\n            A.pop()\n\n\ndef main():\n    input()\n    A = deque(map(int,input().split()))\n\n    res = solve(A)\n    print(len(res))\n    print(*res, sep='')\n\n\nmain()", "n = int(input())\nl = [*map(int, input().split())]\nprev = 0\nres = []\nwhile l:\n    if l[0] == l[-1]:\n        if prev >= l[0]: break\n        if len(l) <= 2:\n            res.append('L')\n            break\n        c0, c1 = [], []\n        p = prev\n        for e in l:\n            if p < e:\n                c0.append('L')\n                p = e\n            else: break\n        p = prev\n        for e in l[::-1]:\n            if p < e:\n                c1.append('R')\n                p = e\n            else:\n                break\n        if len(c0) <= len(c1):\n            res += c1\n        else:\n            res += c0\n        break\n    elif prev < l[0] and (l[0] < l[-1] or prev >= l[-1]):\n        i = 0\n        res.append('L')\n    elif prev < l[-1]: \n        i = -1\n        res.append('R')\n    else: break\n    prev = l[i]\n    del l[i]\nprint(len(res))\nprint(''.join(res))", "3\n\ndef check_l(a, l, r):\n    d = 0\n    last = 0\n    while l <= r and a[l] > last:\n        last = a[l]\n        l += 1\n        d += 1\n    return d\n\ndef check_r(a, l, r):\n    d = 0\n    last = 0\n    while l <= r and a[r] > last:\n        last = a[r]\n        r -= 1\n        d += 1\n    return d\n\ndef main():\n    # skip N\n    input()\n    a = [int(x) for x in input().split(' ')]\n    n = len(a)\n\n    l, r = 0, n - 1\n    res = []\n    \n    last = 0\n    picked = True\n\n    while l <= r and picked:\n        picked = False\n        if last < a[l] and last < a[r]:\n            if a[l] < a[r]:\n                last = a[l]\n                res.append('L')\n                l += 1\n            elif a[l] == a[r]:\n                dl = check_l(a, l, r)\n                dr = check_r(a, l, r)\n                \n                if dl > dr:\n                    res.extend(['L'] * dl)\n                    last = a[l + dl - 1]\n                    l += dl\n                else:\n                    res.extend(['R'] * dr)\n                    last = a[r - dr + 1]\n                    r -= dr\n            else:\n                last = a[r]\n                res.append('R')\n                r -= 1\n            picked = True\n            continue\n        \n        if last < a[l]:\n            last = a[l]\n            res.append('L')\n            l += 1\n            picked = True\n            continue\n        \n        if last < a[r]:\n            last = a[r]\n            res.append('R')\n            r -= 1\n            picked = True\n            continue\n    \n    print(len(res))\n    print(\"\".join(res))\n        \n\ndef __starting_point():\n    main()\n__starting_point()", "n = int(input())\nai = list(map(int,input().split()))\nans = 0\nans2 = \"\"\nnum = 0\nleft = 0\nright = n-1\nflag = 0\nfor i in range(n):\n    if ai[left] <= num:\n        if ai[right] <= num:\n            break\n        num = ai[right]\n        ans += 1\n        right -= 1\n        ans2 += \"R\"\n        continue\n        \n    if ai[right] <= num:\n        if ai[left] <= num:\n            break\n        num = ai[left]\n        ans += 1\n        left += 1\n        ans2 += \"L\"\n        continue\n    if ai[left] > ai[right]:\n        num = ai[right]\n        ans += 1\n        right -= 1\n        ans2 += \"R\"\n    elif ai[left] == ai[right]:\n        if left == right:\n            ans += 1\n            ans2 += \"L\"\n            break\n        flag = 1\n        break\n    else:\n        num = ai[left]\n        ans += 1\n        left += 1\n        ans2 += \"L\"\nif flag == 1:\n    left2 = left\n    temp = 0\n    num2 = num\n    while left2 < right:\n        if ai[left2] > num2:\n            temp += 1\n            num2 = ai[left2]\n        else:\n            break\n        left2 += 1\n    temp2 = 0\n    right2 = right\n    num2 = num\n    while right2 > left:\n        if ai[right2] > num2:\n            temp2 += 1\n            num2 = ai[right2]\n        else:\n            break\n        right2 -= 1\n    if temp >= temp2:\n        ans += temp\n        ans2 += \"L\" * temp\n    else:\n        ans += temp2\n        ans2 += \"R\" * temp2\nprint(ans)\nprint(ans2)\n", "n=int(input())\narr=list(map(int,input().split()))\ni=0\nj=n-1\nans=''\nprev=0\nwhile(i<j):\n\tif(arr[i]<arr[j]):\n\t\tif(arr[i]>prev):\n\t\t\tans+='L'\n\t\t\tprev=arr[i]\n\t\t\ti+=1\n\t\telif(arr[j]>prev):\n\t\t\tans+='R'\n\t\t\tprev=arr[j]\n\t\t\tj-=1\n\t\telse:\n\t\t\tbreak\n\telif(arr[i]>arr[j]):\n\t\tif(arr[j]>prev):\n\t\t\tans+='R'\n\t\t\tprev=arr[j]\n\t\t\tj-=1\n\t\telif(arr[i]>prev):\n\t\t\tans+='L'\n\t\t\tprev=arr[i]\n\t\t\ti+=1\n\t\telse:\n\t\t\tbreak\n\telse:\n\t\t#print(prev)\n\t\tif(arr[i]<prev):\n\t\t\tbreak\n\t\telse:\n\t\t\tcount1=0\n\t\t\tcount2=0\n\t\t\ttemp=i\n\t\t\ttemprev=prev\n\t\t\twhile(temp<j):\n\t\t\t\tif(arr[temp]>temprev):\n\t\t\t\t\ttemprev=arr[temp]\n\t\t\t\t\tcount1+=1\n\t\t\t\t\ttemp+=1\n\t\t\t\telse:\n\t\t\t\t\tbreak\n\t\t\ttemp=j\n\t\t\ttemprev2=prev\n\t\t\t#print(count1)\n\t\t\twhile(temp>i):\n\t\t\t\t#print(arr[temp],prev)\n\t\t\t\tif(arr[temp]>temprev2):\n\t\t\t\t\ttemprev2=arr[temp]\n\t\t\t\t\tcount2+=1\n\t\t\t\t\ttemp-=1\n\t\t\t\telse:\n\t\t\t\t\tbreak\n\t\t\t#print(count1,count2)\n\t\t\tif(count1>=count2):\n\t\t\t\tans+='L'*count1\n\t\t\t\ti+=count1\n\t\t\t\tprev=temprev\n\t\t\telif(count2>count1):\n\t\t\t\tans+='R'*count2\n\t\t\t\tj-=count2\n\t\t\t\tprev=temprev2\n\t\t\tbreak\n\n\t#print(ans)\n\t#print(i,j)\nif(i==j and arr[i]>prev):\n\tans+='R'\n\tprev=arr[i]\nprint(len(ans))\nprint(ans)\n\n", "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\n\"\"\"Codeforces Round #555 (Div. 3)\n\nProblem C. Increasing Subsequence\n\n:author:         Kitchen Tong\n:mail:    kctong529@gmail.com\n\nPlease feel free to contact me if you have any question\nregarding the implementation below.\n\"\"\"\n\n__version__ = '1.0'\n__date__ = '2019-04-26'\n\nimport sys\n\n\ndef rec_solve(a, l, r, last):\n    choices = []\n    while l <= r:\n        if a[l] == a[r] and a[l] > last:\n            sub_ans_1 = rec_solve(a, l+1, r, a[l])\n            sub_ans_2 = rec_solve(a, l, r-1, a[l])\n            if len(sub_ans_1) > len(sub_ans_2):\n                choices.append('L')\n                choices += sub_ans_1\n                return choices\n            else:\n                choices.append('R')\n                choices += sub_ans_2\n                return choices\n        elif a[l] < a[r] and a[l] > last:\n            last = a[l]\n            choices.append('L')\n            l += 1\n        elif a[r] > last:\n            last = a[r]\n            choices.append('R')\n            r -= 1\n        elif a[l] > last:\n            last = a[l]\n            choices.append('L')\n            l += 1\n        else:\n            return choices\n    return choices\n\ndef solve(n, a):\n    return rec_solve(a, 0, n-1, 0)\n\ndef main(argv=None):\n    n = int(input())\n    a = list(map(int, input().split()))\n    choice = solve(n, a)\n    print(len(choice))\n    print(''.join(choice))\n    return 0\n\ndef __starting_point():\n    STATUS = main()\n    return(STATUS)\n\n\n__starting_point()", "\nn = int(input())\n\narr = list(map(int,input().strip().split()))\n\nfl = 1\n\nans = \"\"\nc = 0\n\nst = 0\nen = n-1\n\nla = 0\nfloop = 0\nwhile fl:\n    if st>=n or en<=-1:\n        \n        break\n\n    if arr[st]==arr[en]:\n        floop =1\n        break;\n\n    \n    if arr[st] > la:\n        if arr[en]>la:\n            if arr[en] > arr[st]:\n                st+=1\n                la = arr[st-1]\n                ans+=\"L\"\n                c+=1\n            else:\n                en-=1\n                la  = arr[en+1]\n                ans+=\"R\"\n                c+=1\n        else:\n            st+=1\n            la = arr[st-1]\n            ans+=\"L\"\n            c+=1\n    else:\n        if arr[en]>la:\n            en-=1\n            la =arr[en+1]\n            ans+=\"R\"\n            c+=1\n        else:\n            break;\n#print(floop)\nif floop == 1:\n    orig = la\n    cm = 0\n    s1 = \"\"\n    for i in range(st,en+1):\n        if arr[i]>la:\n            la = arr[i]\n            cm+=1\n            s1+=\"L\"\n        else:\n            break;\n    cn = 0\n    s2 = \"\"\n    la = orig\n    for i in range(en,st-1,-1):\n        if la < arr[i]:\n            cn+=1\n            s2+=\"R\"\n            la = arr[i]\n        else:\n            break;\n    if cn>cm:\n        ans+=s2\n    else:\n        \n        ans+=s1\n    c+=max(cn,cm)\n    ##print(s1,s2)\n\n    \n    \nprint(c)\nprint(ans)\n                \n", "n = int(input())\na = [int(i) for i in input().split()]\nlast = -1\ni = 0\nj = n - 1\nans = ''\nwhile i <= j:\n    if max(a[i], a[j]) <= last:\n        break\n    if a[i] == a[j]:\n        start = i\n        k = 0\n        last = a[i]\n        i += 1\n        while i <= j:\n            if a[i] <= last:\n                break\n            else:\n                last = a[i]\n                k += 1\n                i += 1\n        last = a[j]\n        k2 = 0\n        i = start\n        j -= 1\n        while i <= j:\n            if a[j] <= last:\n                break\n            else:\n                last = a[j]\n                k2 += 1\n                j -= 1\n        if k > k2:\n            ans += 'L' * (k + 1)\n        else:\n            ans += 'R' * (k2 + 1)\n        break\n    if a[i] < a[j]:\n        if a[i] > last:\n            ans += 'L'\n            last = a[i]\n            i += 1\n        else:\n            ans += 'R'\n            last = a[j]\n            j -= 1\n    else:\n        if a[j] > last:\n            ans += 'R'\n            last = a[j]\n            j -= 1\n        else:\n            ans += 'L'\n            last = a[i]\n            i += 1\nprint(len(ans))\nprint(ans)\n", "def search(l, r, pr):\n\tposl = \"\"\n\tfl = True\n\twhile l <= r:\n\t\tif sp[l] < sp[r]:\n\t\t\tif sp[l] > pr:\n\t\t\t\tpr = sp[l]\n\t\t\t\tl += 1\n\t\t\t\tposl += \"L\"\n\t\t\telif sp[r] > pr:\n\t\t\t\tpr = sp[r]\n\t\t\t\tr -= 1\n\t\t\t\tposl += \"R\"\n\t\t\telse:\n\t\t\t\tfl = False\n\t\telif sp[l] > sp[r]:\n\t\t\tif sp[r] > pr:\n\t\t\t\tpr = sp[r]\n\t\t\t\tr -= 1\n\t\t\t\tposl += \"R\"\n\t\t\telif sp[l] > pr:\n\t\t\t\tpr = sp[l]\n\t\t\t\tl += 1\n\t\t\t\tposl += \"L\"\n\t\t\telse:\n\t\t\t\tfl = False\n\t\telse:\n\t\t\tif sp[l] > pr:\n\t\t\t\tfst = search(l + 1, r, sp[l]) + \"L\"\n\t\t\t\tsec = search(l, r - 1, sp[r]) + \"R\"\n\t\t\t\tif len(sec) > len(fst):\n\t\t\t\t\tposl += sec\n\t\t\t\telse:\n\t\t\t\t\tposl += fst\n\t\t\tfl = False\n\t\tif not fl:\n\t\t\tbreak\n\treturn posl\n\n\n\nn = int(input())\nsp = list(map(int, input().split()))\npr = 0\nposl = \"\"\nl = 0\nr = n - 1\nnew = search(l, r, 0)\nprint(len(new))\nprint(new)\n\n", "import sys\ninput = sys.stdin.readline\n#from collections import deque\n\nn=int(input())\nA=list(map(int,input().split()))\n#B=deque(A)\n\n\nLIST=[1]*n\nLIST_INV=[1]*n\n\nfor i in range(n-2,-1,-1):\n    if A[i]<A[i+1]:\n        LIST[i]=LIST[i+1]+1\n\n\nfor i in range(1,n):\n    if A[i]<A[i-1]:\n        LIST_INV[i]=LIST_INV[i-1]+1\n\nANS=[]\nSCORE=0\ni=0\nj=n-1\nwhile True:\n    if i==j and A[i]>SCORE:\n        ANS.append(\"R\")\n        SCORE=A[i]\n        break\n    \n    if A[i]>A[j] and A[j]>SCORE:\n        ANS.append(\"R\")\n        SCORE=A[j]\n        j-=1\n        \n    elif A[i]<A[j] and A[i]>SCORE:\n        ANS.append(\"L\")\n        SCORE=A[i]\n        i+=1\n        \n    elif A[i]>A[j] and A[j]<=SCORE and A[i]>SCORE:\n        ANS.append(\"L\")\n        SCORE=A[i]\n        i+=1\n        \n    elif A[i]<A[j] and A[i]<=SCORE and A[j]>SCORE:\n        ANS.append(\"R\")\n        SCORE=A[j]\n        j-=1\n\n    elif A[i]==A[j] and A[i]>SCORE:\n        if LIST[i]>LIST_INV[j]:\n            ANS.append(\"L\")\n            SCORE=A[i]\n            i+=1\n        else:\n            ANS.append(\"R\")\n            SCORE=A[j]\n            j-=1\n\n    else:\n        break\nprint(len(ANS))\nprint(\"\".join(ANS))            \n            \n    \n    \n", "n = int(input())\na = [int(item) for item in input().split()]\n\ns = []\ni = 0\nj = n - 1\nans = []\nwhile i <= j:\n    if a[i] < a[j]:\n        if not s or s[-1] < a[i]:\n            s.append(a[i])\n            ans.append('L')\n            i += 1\n        elif not s or s[-1] < a[j]:\n            s.append(a[j])\n            ans.append('R')\n            j -= 1\n        else:\n            break\n    elif a[i] > a[j]:\n        if not s or s[-1] < a[j]:\n            ans.append('R')\n            s.append(a[j])\n            j -= 1\n        elif not s or s[-1] < a[i]:\n            s.append(a[i])\n            ans.append('L')\n            i += 1\n        else:\n            break\n    else:\n        p1 = 0\n        p2 = 0\n        cur_last = s[-1] if s else None\n        or_i = i\n        while i <= j and (cur_last is None or a[i] > cur_last):\n            cur_last = a[i]\n            i += 1\n            p1 += 1\n\n        cur_last = s[-1] if s else None\n        while or_i <= j and (cur_last is None or a[j] > cur_last):\n            cur_last = a[j]\n            j -= 1\n            p2 += 1\n        if p1 > p2:\n            ans += list(\"L\" * p1)\n        else:\n            ans += list(\"R\" * p2)\n        break\n\nprint(len(ans))\nprint(''.join(str(x) for x in ans))\n", "\nn = int(input())\n\nM = list(map(int, input().split()))\nL = [1] * n\nR = [1] * n\n\nfor i in range(1, len(M)):\n    if M[i] < M[i-1]:\n        R[i] = R[i-1] + 1\n    if M[n - 1 - i] < M[n - i]:\n        L[n-1-i] = L[n-i] + 1\n\n         \n        \n#print(L)\n#print(R)        \nans = []\n\nlast = -1\nl, r = 0, n - 1\n\nwhile r >= l:\n    #print(str(l) + ' ' + str(r), end=': ')\n    #print(last)\n    if M[r] <= last and M[l] <= last:\n        break\n    if M[r] == M[l]:\n       \n        if L[l] > R[r]:\n            ans += [\"L\"]\n            last = M[l]\n            l += 1\n        else:\n            ans += [\"R\"]\n            last = M[r]\n            r -= 1\n    elif M[r] <= last:\n        last = M[l]\n        ans += [\"L\"]\n        l += 1\n    elif M[l] <= last:\n        last = M[r]\n        ans += [\"R\"]\n        r -= 1\n    else:\n        if M[l] < M[r]:\n            last = M[l]\n            ans += [\"L\"]\n            l += 1\n        else:\n            last = M[r]\n            ans += [\"R\"]\n            r -= 1\n\nprint(len(ans))\nprint(\"\".join(ans))\n", "R = lambda: map(int, input().split())\n\n\ndef isL():\n    k1 = 1\n    while i + k1 <= j and a[i+k1]>a[i+k1-1]:\n        k1 += 1\n    k2 = 1\n    while j - k2 >= i and a[j-k2]>a[j-k2+1]:\n        k2 += 1\n    return k1 >= k2\n\n\nn, a = int(input()), list(R())\nres = []\ni, j = 0, n-1\nv = 0\nwhile i <= j:\n    if a[i] <= v and a[j] <= v:\n        break\n    elif a[i] > v >= a[j]:\n        res.append('L')\n        v = a[i]\n        i += 1\n    elif a[j] > v >= a[i]:\n        res.append('R')\n        v = a[j]\n        j -= 1\n    elif a[i] < a[j]:\n        res.append('L')\n        v = a[i]\n        i += 1\n    elif a[j] < a[i]:\n        res.append('R')\n        v = a[j]\n        j -= 1\n    elif i == j:\n        res.append('L')\n        v = a[i]\n        i += 1\n    elif isL():\n        res.append('L')\n        v = a[i]\n        i += 1\n    else:\n        res.append('R')\n        v = a[j]\n        j -= 1\n\nres = ''.join(res)\nprint(len(res))\nprint(res)", "n = int(input())\nsl = list(map(int, input().split()))\nans = \"\"\ncurrent = 0\nfor i in range(n):\n    if(current<sl[0] and current<sl[-1]):\n        #print(sl)\n        if(sl[0] == sl[-1] and i!=(n-1)):\n            l, r = 1, 1\n            for j in range(len(sl)):\n                #print(sl[j], sl[j+1])\n                if(sl[j]<sl[j+1]): l += 1\n                else: break\n            for j in range(len(sl)):\n                #print(sl[-(j+1)], sl[-(j+2)], sl[-(j+1)]>sl[-(j+2)])\n                if(sl[-(j+1)]<sl[-(j+2)]): r += 1\n                else: break\n            #print(l, r)\n            if(l>r): ans += \"L\"*l\n            else: ans += \"R\"*r\n            break\n        elif(current<sl[0] and sl[0] <= sl[-1]):\n            ans += \"L\"\n            current = sl.pop(0)\n        elif(current<sl[-1] and sl[0]>sl[-1]):\n            ans += \"R\"\n            current = sl.pop()\n    elif(current<sl[0] and current>=sl[-1]):\n        ans += \"L\"\n        current = sl.pop(0)\n    elif(current>=sl[0] and current<sl[-1]):\n        ans += \"R\"\n        current = sl.pop()\n    else: break\nprint(len(ans))\nprint(ans)", "# -*- coding: utf-8 -*-\n\"\"\"\n@Project : CodeForces\n@File    : 32.py \n@Time    : 2019/4/26 23:43\n@Author  : Koushiro \n\"\"\"\n\ndef __starting_point():\n    n = int(input())\n    nums = list(map(int, input().split()))\n    result = []\n    last = -1\n    left = 0\n    right = len(nums) - 1\n    while left <= right:\n        if nums[left] < nums[right]:\n            if nums[left] > last:\n                last = nums[left]\n                left += 1\n                result.append('L')\n            elif nums[right] > last:\n                last = nums[right]\n                right -= 1\n                result.append('R')\n            else:\n                break\n        elif nums[left] > nums[right]:\n            if nums[right] > last:\n                last = nums[right]\n                right -= 1\n                result.append('R')\n            elif nums[left] > last:\n                last = nums[left]\n                left += 1\n                result.append('L')\n            else:\n                break\n        elif nums[left] == nums[right]:\n            l_n = left\n            r_n = right\n            l_c = 0\n            r_c = 0\n            l_last = last\n            r_last = last\n            while l_n <= right:\n                if nums[l_n] > l_last:\n                    l_c += 1\n                    l_last = nums[l_n]\n                    l_n += 1\n                else:\n                    break\n            while r_n >= left:\n                if nums[r_n] > r_last:\n                    r_c += 1\n                    r_last = nums[r_n]\n                    r_n -= 1\n                else:\n                    break\n            if l_c > r_c:\n                for i in range(l_c):\n                    result.append(\"L\")\n            else:\n                for i in range(r_c):\n                    result.append(\"R\")\n            break\n\n    print(len(result))\n    print(\"\".join(result))\n\n__starting_point()", "n = int(input())\nnums = list(map(int, input().split()))\n\n\ndef foo(l, r, prev=0):\n    ans = \"\"\n    while l <= r:\n        if nums[l] <= prev and nums[r] <= prev:\n            break\n        if prev < nums[l] < nums[r]:\n            ans += \"L\"\n            prev = nums[l]\n            l += 1\n        elif prev < nums[r] < nums[l]:\n            ans += \"R\"\n            prev = nums[r]\n            r -= 1\n        elif nums[r] > nums[l]:\n            ans += \"R\"\n            prev = nums[r]\n            r -= 1\n        elif nums[r] < nums[l]:\n            ans += \"L\"\n            prev = nums[l]\n            l += 1\n        elif l == r:\n            ans += 'R'\n            break\n        else:\n            a1 = 'L' + foo(l + 1, r, nums[l])\n            a2 = 'R' + foo(l, r - 1, nums[l])\n            ans += a1 if len(a1) > len(a2) else a2\n            break\n    return ans\n\n\nans = foo(0, n - 1)\nprint(len(ans))\nprint(ans)\n", "from collections import deque\nn=int(input())\na=deque([int(x) for x in input().split()])\ncur=-1\nans=''\nwhile (cur<a[0] or cur<a[-1]):\n    if a[0]<a[-1]:\n        if cur<a[0]:\n            ans+='L'\n            cur=a[0]\n            a.popleft()\n        else:\n            ans+='R'\n            cur=a[-1]\n            a.pop()\n        \n    elif a[0]>a[-1]:\n        if cur<a[-1]:\n            ans+='R'\n            cur=a[-1]\n            a.pop()\n        else:\n            ans+='L'\n            cur=a[0]\n            a.popleft()\n    elif len(a)==1:\n        ans+='R'\n        cur=a[-1]\n        a.pop()\n    elif a[0]==a[-1]:\n        cur1=cur\n        cur2=cur\n        b=a.copy()\n        c=a.copy()\n        count1=0\n        count2=0\n        while cur1<b[0]:\n            count1+=1\n            cur1=b[0]\n            b.popleft()\n        while cur2<c[-1]:\n            count2+=1\n            cur2=c[-1]\n            c.pop()\n        if count1>count2:\n            for i in range(count1):\n                ans+='L'\n            break\n        else:\n            for i in range(count2):\n                ans+='R'\n            break\n            \n    if len(a)==0:\n        break\n\nprint(len(ans))\nprint(ans)", "''' CODED WITH LOVE BY SATYAM KUMAR '''\n\nfrom sys import stdin, stdout\nimport cProfile, math\nfrom collections import Counter,defaultdict,deque\nfrom bisect import bisect_left,bisect,bisect_right\nimport itertools\nfrom copy import deepcopy\nfrom fractions import Fraction\nimport sys, threading\nimport operator as op\nfrom functools import reduce\nsys.setrecursionlimit(10**6) # max depth of recursion\nthreading.stack_size(2**27)  # new thread will get stack of such size\nfac_warmup = False\nprintHeap = str()\nmemory_constrained = False\nP = 10**9+7\nimport sys\n\nclass merge_find:\n    def __init__(self,n):\n        self.parent = list(range(n))\n        self.size = [1]*n\n        self.num_sets = n\n        self.lista = [[_] for _ in range(n)]\n    def find(self,a):\n        to_update = []\n        while a != self.parent[a]:\n            to_update.append(a)\n            a = self.parent[a]\n        for b in to_update:\n            self.parent[b] = a\n        return self.parent[a]\n    def merge(self,a,b):\n        a = self.find(a)\n        b = self.find(b)\n        if a==b:\n            return\n        if self.size[a]<self.size[b]:\n            a,b = b,a\n        self.num_sets -= 1\n        self.parent[b] = a\n        self.size[a] += self.size[b]\n        self.lista[a] += self.lista[b]\n    def set_size(self, a):\n        return self.size[self.find(a)]\n    def __len__(self):\n        return self.num_sets\n\ndef display(string_to_print):\n    stdout.write(str(string_to_print) + \"\\n\")\n\ndef primeFactors(n): #n**0.5 complex \n    factors = dict()\n    for i in range(2,math.ceil(math.sqrt(n))+1):  \n        while n % i== 0: \n            if i in factors:\n                factors[i]+=1\n            else: factors[i]=1\n            n = n // i \n    if n>2:\n        factors[n]=1\n    return (factors)\n\ndef all_factors(n):    \n    return set(reduce(list.__add__, \n                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))\n\ndef fibonacci_modP(n,MOD):\n    if n<2: return 1\n    #print (n,MOD)\n    return (cached_fn(fibonacci_modP, (n+1)//2, MOD)*cached_fn(fibonacci_modP, n//2, MOD) + cached_fn(fibonacci_modP, (n-1) // 2, MOD)*cached_fn(fibonacci_modP, (n-2) // 2, MOD)) % MOD\n\ndef factorial_modP_Wilson(n , p): \n    if (p <= n): \n        return 0\n    res = (p - 1) \n    for i in range (n + 1, p): \n        res = (res * cached_fn(InverseEuler,i, p)) % p \n    return res \n\ndef binary(n,digits = 20):\n    b = bin(n)[2:]\n    b = '0'*(20-len(b))+b\n    return b\n\ndef isprime(n):\n    \"\"\"Returns True if n is prime.\"\"\"\n    if n < 4:\n        return True\n    if n % 2 == 0:\n        return False\n    if n % 3 == 0:\n        return False\n    i = 5\n    w = 2\n    while i * i <= n:\n        if n % i == 0:\n            return False\n        i += w\n        w = 6 - w\n    return True\nfactorial_modP = []\ndef warm_up_fac(MOD):\n    nonlocal factorial_modP,fac_warmup\n    if fac_warmup: return\n    factorial_modP= [1 for _ in range(fac_warmup_size+1)]\n    for i in range(2,fac_warmup_size):\n        factorial_modP[i]= (factorial_modP[i-1]*i) % MOD\n    fac_warmup = True\n\ndef InverseEuler(n,MOD):\n    return pow(n,MOD-2,MOD)\n\ndef nCr(n, r, MOD):\n    nonlocal fac_warmup,factorial_modP\n    if not fac_warmup:\n        warm_up_fac(MOD)\n        fac_warmup = True\n    return (factorial_modP[n]*((pow(factorial_modP[r], MOD-2, MOD) * pow(factorial_modP[n-r], MOD-2, MOD)) % MOD)) % MOD\n\ndef test_print(*args):\n    if testingMode:\n        print(args)\n\ndef display_list(list1, sep=\" \"):\n    stdout.write(sep.join(map(str, list1)) + \"\\n\")\n\ndef display_2D_list(li):\n    for i in li:\n        print(i)\ndef prefix_sum(li):\n    sm = 0\n    res = []\n    for i in li:\n        sm+=i\n        res.append(sm)\n    return res\n\ndef get_int():\n    return int(stdin.readline().strip())\n\ndef get_tuple():\n    return map(int, stdin.readline().split())\n\ndef get_list():\n    return list(map(int, stdin.readline().split()))\nimport heapq,itertools\npq = []                         # list of entries arranged in a heap\nentry_finder = {}               # mapping of tasks to entries\nREMOVED = '<removed-task>' \ndef add_task(task, priority=0):\n    'Add a new task or update the priority of an existing task'\n    if task in entry_finder:\n        remove_task(task)\n    count = next(counter)\n    entry = [priority, count, task]\n    entry_finder[task] = entry\n    heapq.heappush(pq, entry)\n\ndef remove_task(task):\n    'Mark an existing task as REMOVED.  Raise KeyError if not found.'\n    entry = entry_finder.pop(task)\n    entry[-1] = REMOVED\n\ndef pop_task():\n    'Remove and return the lowest priority task. Raise KeyError if empty.'\n    while pq:\n        priority, count, task = heapq.heappop(pq)\n        if task is not REMOVED:\n            del entry_finder[task]\n            return task\n    raise KeyError('pop from an empty priority queue')\nmemory = dict()\ndef clear_cache():\n    nonlocal memory\n    memory = dict()\ndef cached_fn(fn, *args):\n    nonlocal memory\n    if args in memory:\n        return memory[args]\n    else:\n        result = fn(*args)\n        memory[args] = result\n        return result\n\ndef ncr (n,r):\n    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))\ndef binary_serach(i,li):\n    #print(\"Search for \",i)\n    fn = lambda x: li[x]-x//i\n    x = -1\n    b = len(li)\n    while b>=1:\n        #print(b,x)\n        while b+x<len(li) and fn(b+x)>0: #Change this condition 2 to whatever you like\n            x+=b\n        b=b//2\n    return x\n\n# -------------------------------------------------------------- MAIN PROGRAM\nTestCases = False\ntestingMode = False\nfac_warmup_size = 10**5+100\noptimiseForReccursion = True #Can not be used clubbed with TestCases # WHen using recursive functions, use Python 3\nfrom math import factorial\n\ndef main():\n    get_int()\n    li = deque(get_list())\n    prev = 0\n    res = []\n    while len(li)>0:\n        if li[0]==li[-1] and li[0]>prev and len(li)>1:\n            guess1 = 0\n            guess2 = 0\n            prev = li[0]\n            p = prev\n            dq = list(li)\n            n = len(dq)\n            for i in range(1,n):\n                if dq[i]>prev: prev=dq[i]\n                else: break\n                if i==n-1: i=n\n            guess1 = i\n            dq.reverse()\n            prev = p\n            for i in range(1,n):\n                if dq[i]>prev: prev=dq[i]\n                else: break\n                if i==n-1: i=n\n            guess2 = i\n            if guess1>guess2:\n                res += [\"L\"]*guess1\n            else:\n                res += [\"R\"]*guess2\n            break\n\n        elif li[0]<li[-1] and li[0]>prev:\n            prev = li.popleft()\n            res.append(\"L\")     \n        elif li[-1]>prev:\n            prev = li.pop()\n            res.append(\"R\")\n        elif li[0]>prev:\n            prev = li.popleft()\n            res.append(\"L\") \n        else: break\n    print(len(res))\n    display_list(res,\"\")\n\n# --------------------------------------------------------------------- END=\n\n\nif TestCases: \n    for i in range(get_int()): \n        cProfile.run('main()') if testingMode else main(i) \nelse: (cProfile.run('main()') if testingMode else main()) if not optimiseForReccursion else threading.Thread(target=main).start()", "N = int(input())\na_list = list(map(int, input().split()))\nfrom collections import deque\nimport bisect\n\ndeq = deque(a_list)\nans = \"\"\nleft = 0\nright = 0\nmin_num = -1\ncnt = 0\nf = False\nlr = False\nwhile len(deq) >= 2:\n    left = deq.popleft()\n    right = deq.pop()\n    # print(left, right)\n    max_num = max(left, right)\n    if max_num > min_num:\n\n        if left == right:\n            deq.appendleft(left)\n            deq.append(right)\n            lr = True\n            break\n        cnt += 1\n        if right > left > min_num:\n            ans += \"L\"\n            deq.append(right)\n            min_num = left\n        elif left > right > min_num:\n            ans += \"R\"\n            deq.appendleft(left)\n            min_num = right\n        elif left > min_num:\n            ans += \"L\"\n            deq.append(right)\n            min_num = left\n        else:\n            ans += \"R\"\n            deq.appendleft(left)\n            min_num = right\n    else:\n        f = True\n        break\nif lr:\n    l = 0\n    r = 0\n    tmp = deq.copy()\n    prv = -1\n    for t in tmp:\n        if t > prv:\n            l += 1\n        else:\n            break\n        prv = t\n    tmp = list(reversed(tmp))\n    prv = -1\n    for t in tmp:\n        if t > prv:\n            r += 1\n        else:\n            break\n        prv = t\n    if l > r:\n        print(cnt + l)\n        print(ans + \"L\" * l)\n    else:\n        print(cnt + r)\n        print(ans + \"R\" * r)\n    return\n\n\nif f:\n    print(cnt)\n    print(ans)\nelse:\n    tmp = deq.pop()\n    if tmp > min_num:\n        cnt += 1\n        print(cnt)\n        print(ans + \"R\")\n    else:\n        print(cnt)\n        print(ans)\n", "n = int(input())\na = [int(i) for i in input().split()]\nnew = [0]\ns = ''\ni = 0\nj = -1\n\ndef rec(a, i, j):\n    c = func(a, i + 1, j, new + [a[i]], s)\n    d = func(a, i, j - 1, new + [a[j]], s)\n    if c[0] < d[0]:\n        return True\n    else:\n        return False\n\ndef func(a, i, j, new, s):\n    while True:\n        if n - i < -j:\n            return len(new) - 1, s\n            break\n        if a[i] > new[-1] and a[j] > new[-1]:\n            if a[i] == a[j]:\n                if rec(a, i, j):\n                    new.append(a[j])\n                    j -= 1\n                    s += 'R'\n                else:\n                    s += 'L'\n                    new.append(a[i])\n                    i += 1\n            elif a[i] < a[j]:\n                new.append(a[i])\n                s += 'L'\n                i += 1\n            else:\n                new.append(a[j])\n                s += 'R'\n                j -= 1\n        elif a[i] > new[-1] or a[j] > new[-1]:\n            if a[i] > new[-1]:\n                new.append(a[i])\n                s += 'L'\n                i += 1\n            else:\n                new.append(a[j])\n                s += 'R'\n                j -= 1\n        else:\n            return len(new) - 1, s\n            break\n\nfor j in func(a, i, j, new, s):\n    print(j)\n", "def solve(p, q, r):\n    ans = \"\"\n    current = r\n    i = p\n    j = q\n    while True:\n        if j < i:\n            break\n        if current < num[i] < num[j] or num[j] <= current < num[i]:\n            ans += \"L\"\n            current = num[i]\n            i += 1\n            continue\n        if current < num[j] < num[i] or num[i] <= current < num[j]:\n            ans += \"R\"\n            current = num[j]\n            j -= 1\n            continue\n        if current < num[i] == num[j]:\n            ans1 = solve(i, j - 1, num[i])\n            ans2 = solve(i + 1, j, num[i])\n            if len(ans1) > len(ans2):\n                ans += \"R\" + ans1\n            else:\n                ans += \"L\" + ans2\n        break\n    return ans\n\nn = int(input())\nnum = [*list(map(int, input().split()))]\nans = solve(0, n - 1, -1)\nprint(len(ans))\nprint(ans)\n", "def main():\n    n = int(input())\n    a = list(map(int, input().split()))\n    i = 0\n    j = n - 1\n    last = -1\n    anz = []\n    stop = False\n    while i != j:\n        if a[i] == a[j]:\n            stop = True\n            break\n        if a[i] < a[j]:\n            if a[i] > last:\n                last = a[i]\n                i += 1\n                anz.append(\"L\") \n            elif a[j] > last:\n                last = a[j]\n                j -= 1\n                anz.append(\"R\")\n            else:\n                break\n        else:\n            if a[j] > last:\n                last = a[j]\n                j -= 1\n                anz.append(\"R\") \n            elif a[i] > last:\n                last = a[i]\n                i += 1\n                anz.append(\"L\")\n            else:\n                break\n    if i == j and a[i] > last:\n        anz.append(\"R\")\n    if stop:\n        l = []\n        r = []\n        i1 = i\n        last1 = last\n        while last1 < a[i] and i != j:\n            last1 = a[i]\n            i += 1\n            l.append(\"L\")\n        while last < a[j] and i1 != j:\n            last = a[j]\n            j -= 1\n            r.append(\"R\")\n        if len(l) > len(r):\n            print(len(anz) + len(l))\n            for elem in anz:\n                print(elem, end=\"\")\n            for elem in l:\n                print(elem, end=\"\")\n        else:\n            print(len(r) + len(anz))\n            for elem in anz:\n                print(elem, end=\"\")\n            for elem in r:\n                print(elem, end=\"\")            \n    else:\n        print(len(anz))\n        for elem in anz:\n            print(elem, end=\"\")\nmain()"]