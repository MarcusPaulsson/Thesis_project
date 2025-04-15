["x1, y1, x2, y2 = list(map( int, input().split() ))\nx3, y3, x4, y4 = list(map( int, input().split() ))\nx5, y5, x6, y6 = list(map( int, input().split() ))\n\ncovered = False\nif x3 <= x1 and y3 <= y1 and x4 >= x2 and y4 >= y2:\n    covered = True\nelif x5 <= x1 and y5 <= y1 and x6 >= x2 and y6 >= y2:\n    covered = True\nelif x1 >= x3 and x1 >= x5 and x2 <= x4 and x2 <= x6:\n    if min( y4, y6 ) >= max( y3, y5 ) and min( y3, y5 ) <= y1 and max( y4, y6 ) >= y2:\n        covered = True\nelif y1 >= y3 and y1 >= y5 and y2 <= y4 and y2 <= y6:\n    if min( x4, x6 ) >= max( x3, x5 ) and min( x3, x5 ) <= x1 and max( x4, x6 ) >= x2:\n        covered = True\n\nprint( \"NO\" if covered else \"YES\" )\n", "w_x1, w_y1, w_x2, w_y2 = list(map(int, input().split()))\n\nx1, y1, x2, y2 = list(map(int, input().split()))\nif x1 <= w_x1 and w_x2 <= x2:\n    if y1 <= w_y1: \n        w_y1 = max(y2, w_y1)\n    if y2 >= w_y2: \n        w_y2 = min(y1, w_y2)  \n\nif y1 <= w_y1 and w_y2 <= y2:\n    if x1 <= w_x1: \n        w_x1 = max(x2, w_x1)\n    if x2 >= w_x2: \n        w_x2 = min(x1, w_x2) \n        \nx1, y1, x2, y2 = list(map(int, input().split()))\nif x1 <= w_x1 and w_x2 <= x2:\n    if y1 <= w_y1: \n        w_y1 = max(y2, w_y1)\n    if y2 >= w_y2: \n        w_y2 = min(y1, w_y2)  \n\nif y1 <= w_y1 and w_y2 <= y2:\n    if x1 <= w_x1: \n        w_x1 = max(x2, w_x1)\n    if x2 >= w_x2: \n        w_x2 = min(x1, w_x2) \n        \n\nif w_x1 >= w_x2 and w_y1 >= w_y2:\n    print(\"NO\")\nelse:\n    print(\"YES\")\n\n", "\n\ndef main():\n    x1, y1, x2, y2 = map(int, input().split())\n    x3, y3, x4, y4 = map(int, input().split())\n    x5, y5, x6, y6 = map(int, input().split())\n\n    ans = \"NO\"\n    for x in range(x1, x2+1):\n        if not (x3 <= x <= x4 and y3 <= y1 <= y4) and not (x5 <= x <= x6 and y5 <= y1 <= y6):\n            ans = \"YES\"\n        if not (x3 <= x <= x4 and y3 <= y2 <= y4) and not (x5 <= x <= x6 and y5 <= y2 <= y6):\n            ans = \"YES\"\n        if x == x2:\n            continue\n        x += 0.5\n        if not (x3 <= x <= x4 and y3 <= y1 <= y4) and not (x5 <= x <= x6 and y5 <= y1 <= y6):\n            ans = \"YES\"\n        if not (x3 <= x <= x4 and y3 <= y2 <= y4) and not (x5 <= x <= x6 and y5 <= y2 <= y6):\n            ans = \"YES\"\n        \n\n    for y in range(y1, y2+1):\n        if not (x3 <= x1 <= x4 and y3 <= y <= y4) and not (x5 <= x1 <= x6 and y5 <= y <= y6):\n            ans = \"YES\"\n        if not (x3 <= x2 <= x4 and y3 <= y <= y4) and not (x5 <= x2 <= x6 and y5 <= y <= y6):\n            ans = \"YES\"\n        if y == y2:\n            continue\n        y += 0.5\n        if not (x3 <= x1 <= x4 and y3 <= y <= y4) and not (x5 <= x1 <= x6 and y5 <= y <= y6):\n            ans = \"YES\"\n        if not (x3 <= x2 <= x4 and y3 <= y <= y4) and not (x5 <= x2 <= x6 and y5 <= y <= y6):\n            ans = \"YES\"\n\n    print(ans)\n\ndef __starting_point():\n    main()\n__starting_point()", "w = list(map(int,input().split()))\ng = list(map(int,input().split()))\nb = list(map(int,input().split()))\n\ndef cover(w,b):\n    return b[0] <= w[0] and w[2] <= b[2] and b[1] <= w[1] and w[3] <= b[3]\n\ndef hcover(w,b1,b2):\n    h = b1[0] <= w[0] and w[2] <= b1[2] and b2[0] <= w[0] and w[2] <= b2[2]\n    v1 = b1[1] <= w[1] and b2[1] <= b1[3] and  w[3] <= b2[3]\n    v2 = b2[1] <= w[1] and b1[1] <= b2[3] and  w[3] <= b1[3]\n\n    return h and (v1 or v2)\n\ndef vcover(w,b1,b2):\n    h = b1[1] <= w[1] and w[3] <= b1[3] and b2[1] <= w[1] and w[3] <= b2[3]\n    v1 = b1[0] <= w[0] and b2[0] <= b1[2] and  w[2] <= b2[2]\n    v2 = b2[0] <= w[0] and b1[0] <= b2[2] and  w[2] <= b1[2]\n    \n    return h and (v1 or v2)\n\nif cover(w,b) or cover(w,g) or hcover(w,b,g) or vcover(w,b,g):\n    print('NO')\nelse:\n    print('YES')\n", "#!python3\n\nfrom collections import deque, Counter\nimport array\nfrom itertools import combinations, permutations\nfrom math import sqrt\nimport unittest\n\n\ndef read_int():\n    return int(input().strip())\n\n\ndef read_int_array():\n    return [int(i) for i in input().strip().split(' ')]\n\n######################################################\n\nW = read_int_array()\nB1 = read_int_array()\nB2 = read_int_array()\n\nby_x = [W[0], W[2], B1[0], B1[2], B2[0], B2[2]]\nby_x.sort()\n\nfound = False\nfor x in by_x:\n    if not (W[0] <= x <= W[2]):\n        continue\n    interval = W[3] - W[1]\n    for b in [B1, B2]:\n        if b[0] <= x <= b[2]:\n            interval -= max(0, min(b[3], W[3]) - max(b[1], W[1]))\n    if interval > 0:\n        found = True\n        break\n\nif not found:\n    by_y = [W[1], W[3], B1[1], B1[3], B2[1], B2[3]]\n    by_y.sort()\n    for y in by_y:\n        if not (W[1] <= y <= W[3]):\n            continue\n        interval = W[2] - W[0]\n        for b in [B1, B2]:\n            if b[1] <= y <= b[3]:\n                interval -= max(0, min(b[2], W[2]) - max(b[0], W[0]))\n        if interval > 0:\n            found = True\n            break\nprint(\"YES\" if found else \"NO\")\n\n\n\n\n\n\n", "x1, y1, x2, y2 = map(int, input().split())\nx3, y3, x4, y4 = map(int, input().split())\nx5, y5, x6, y6 = map(int, input().split())\npl = (x2 - x1) * (y2 - y1)\n\n\ndef peresech(a, b, c, d, a2, b2, c2, d2):\n    l1 = [a, c, a2, c2]\n    l2 = [b, d, b2, d2]\n    l1.sort()\n    l2.sort()\n    if a == a2 and b == b2 and c == c2 and d == d2:\n        return [a, b, c, d]\n    if b > d2 or c < a2 or d < b2 or a > c2:\n        return 0\n    return [l1[1], l2[1], l1[2], l2[2]]\n\n\nl = peresech(x1, y1, x2, y2, x3, y3, x4, y4)\nl2 = peresech(x1, y1, x2, y2, x5, y5, x6, y6)\nif l == 0:\n    if l2 != 0:\n        if (l2[2] - l2[0]) * (l2[3] - l2[1]) != pl:\n            print(\"YES\")\n        else:\n            print(\"NO\")\n    else:\n        print(\"YES\")\n    return\nif l2 == 0 and l != 0:\n    if (l[2] - l[0]) * (l[3] - l[1]) != pl:\n        print(\"YES\")\n    else:\n        print(\"NO\")\n    return\nl3 = peresech(l[0], l[1], l[2], l[3], l2[0], l2[1], l2[2], l2[3])\nif l3 == 0:\n    if (l[2] - l[0]) * (l[3] - l[1]) + (l2[2] - l2[0]) * (l2[3] - l2[1]) == pl:\n        print(\"NO\")\n    else:\n        print(\"YES\")\n    return\nif (l[2] - l[0]) * (l[3] - l[1]) + (l2[2] - l2[0]) * (l2[3] - l2[1]) - (l3[2] - l3[0]) * (l3[3] - l3[1]) == pl:\n    print(\"NO\")\nelse:\n    print(\"YES\")", "from sys import stdin, stdout  \n\n\n\nx1, y1, x2, y2 = list(map(int, input().split()))\nx3, y3, x4, y4 = list(map(int, input().split()))\nx5, y5, x6, y6 = list(map(int, input().split()))\n\n\nS1 = 0\nS2 = 0\nS = 0\n\nl1 = min(x2, x4) - max(x1, x3)\nh1 = min(y2, y4) - max(y1, y3)\n\nif l1 >= 0 and h1 >= 0:\n    S1 = l1 * h1\n    \nl2 = min(x2, x6) - max(x1, x5)\nh2 = min(y2, y6) - max(y1, y5)\n\nif l2 >= 0 and h2 >= 0:\n    S2 = l2 * h2\n    \nl3 = min(x2, x6, x4) - max(x1, x5, x3)\nh3 = min(y2, y6, y4) - max(y1, y5, y3)\n\nif l3 >= 0 and h3 >= 0:\n    S = l3 * h3\n\nif S1 + S2 - S == (x2 - x1) * (y2 - y1):\n    print(\"NO\")\nelse:\n    print(\"YES\")\n      \n", "#!/usr/bin/env python3\n\nimport sys\n\nw = [int(i) for i in input().split()]\nb1 = [int(i) for i in input().split()]\nb2 = [int(i) for i in input().split()]\n\n\ndef is_inside(r_in, r_out):\n    return (r_out[0] <= r_in[0] <= r_out[2]) and (\n        r_out[1] <= r_in[1] <= r_out[3]) and (\n            r_out[0] <= r_in[2] <= r_out[2]) and (\n                r_out[1] <= r_in[3] <= r_out[3])\n\n\ndef bisects(r_in, r_out):\n    return ((r_out[0] <= r_in[0] <= r_out[2]) and\n            (r_out[0] <= r_in[2] <= r_out[2])) or (\n                (r_out[1] <= r_in[1] <= r_out[3]) and (\n                    r_out[1] <= r_in[3] <= r_out[3]))\n\n\n\nif is_inside(w, b1) or is_inside(w, b2):\n    print('NO')\n    return\n\n\nif b1[0] <= w[0] <= b1[2] and b1[0] <= w[2] <= b1[2]:\n    if b1[1] <= w[1] <= b1[3]:\n        w[1] = b1[3]\n    elif b1[1] <= w[3] <= b1[3]:\n        w[3] = b1[1]\nelif b1[1] <= w[1] <= b1[3] and b1[1] <= w[3] <= b1[3]:\n    if b1[0] <= w[0] <= b1[2]:\n        w[0] = b1[2]\n    elif b1[0] <= w[2] <= b1[2]:\n        w[2] = b1[0]\nelif b2[0] <= w[0] <= b2[2] and b2[0] <= w[2] <= b2[2]:\n    if b2[1] <= w[1] <= b2[3]:\n        w[1] = b2[3]\n    elif b2[1] <= w[3] <= b2[3]:\n        w[3] = b2[1]\nelif b2[1] <= w[1] <= b2[3] and b2[1] <= w[3] <= b2[3]:\n    if b2[0] <= w[0] <= b2[2]:\n        w[0] = b2[2]\n    elif b2[0] <= w[2] <= b2[2]:\n        w[2] = b2[0]\n\nif is_inside(w, b1) or is_inside(w, b2):\n    print('NO')\n    return\n\nprint('YES')\n", "x1,y1,x2,y2 = map(int, input().split())\nx3,y3,x4,y4 = map(int, input().split())\nx5,y5,x6,y6 = map(int, input().split())\n\nif y1 >= y3 and y2 <= y4 and x1 >= x3 and x2 <= x4:\n    print(\"NO\")\nelif y1 >= y5 and y2 <= y6 and x1 >= x5 and x2 <= x6:\n    print(\"NO\")\nelif x3 <= x1 and x4 >= x2 and x5 <= x1 and x6 >= x2 and y3 <= y1 <= y5 <=y4 <= y2 <= y6:\n    print(\"NO\")\nelif x3 <= x1 and x4 >= x2 and x5 <= x1 and x6 >= x2 and y5 <= y1 <= y3 <=y6 <= y2 <= y4:\n    print(\"NO\")\n\nelif y3 <= y1 and y4 >= y2 and y5 <= y1 and y6 >= y2 and x3 <= x1 <= x5 <=x4 <= x2 <= x6:\n    print(\"NO\")\nelif y3 <= y1 and y4 >= y2 and y5 <= y1 and y6 >= y2 and x5 <= x1 <= x3 <=x6 <= x2 <= x4:\n    print(\"NO\")\n\n\n\nelse:\n    print(\"YES\")", "x1, y1, x2, y2 = map(int, input().split(' '))\nx3, y3, x4, y4 = map(int, input().split(' '))\nx5, y5, x6, y6 = map(int, input().split(' '))\n\nb = True\nif x3 <= x1 and x2 <= x4 and x5 <= x1 and x2 <= x6:\n    if y3 <= y1 and y2 <= y6 and y4 >= y5 or y5 <= y1 and y2 <= y4 and y6 >= y3:\n        b = False\nif y3 <= y1 and y2 <= y4 and y5 <= y1 and y2 <= y6:\n    if x3 <= x1 and x2 <= x6 and x4 >= x5 or x5 <= x1 and x2 <= x4 and x6 >= x3:\n        b = False\nif x3 <= x1 and y3 <= y1 and x4 >= x2 and y4 >= y2:\n    b = False\nif x5 <= x1 and y5 <= y1 and x6 >= x2 and y6 >= y2:\n    b = False\n\nprint(\"YES\") if b == True else print(\"NO\")", "x1, y1, x2, y2 = map(int, input().split())\nx3, y3, x4, y4 = map(int, input().split())\nx5, y5, x6, y6 = map(int, input().split())\n\ndef do_mask(x1, y1, x2, y2, x3, y3, x4, y4):\n    # print(x1, y1, x2, y2, x3, y3, x4, y4)\n    if x1 == -1:\n        return -1, -1, -1, -1\n    # zenbu-kakusu\n    if x3 <= x1 and x2 <= x4 and y3 <= y1 and y2 <= y4:\n        return -1, -1, -1, -1\n\n    # haba-kakusu\n    if x3 <= x1 and x2 <= x4:\n        if y3 <= y1 and y1 <= y4:\n            y1 = y4\n        if y3 <= y2 and y2 <= y4:\n            y2 = y3\n\n    # yoko-kakusu\n    if y3 <= y1 and y2 <= y4:\n        if x3 <= x1 and x1 <= x4:\n            x1 = x4\n        if x3 <= x2 and x2 <= x4:\n            x2 = x3\n\n    return x1, y1, x2, y2\n\nx1, y1, x2, y2 = do_mask(x1, y1, x2, y2, x3, y3, x4, y4)\nx1, y1, x2, y2 = do_mask(x1, y1, x2, y2, x5, y5, x6, y6)\nprint(\"NO\" if x1 == -1 else \"YES\")", "import sys\n\nsin = sys.stdin\n\nw = sin.readline().split()\nw = [int(x) for x in w]\nb1 = sin.readline().split()\nb1 = [int(x) for x in b1]\nb2 = sin.readline().split()\nb2 = [int(x) for x in b2]\n\ndef reduce(w, b):\n    #Fully covered:\n    if b[0] <= w[0] and b[1] <= w[1] and b[2] >= w[2] and b[3] >= w[3]:\n        return True\n    if b[0] <= w[0] and b[1] <= w[1]:\n        if b[2] >= w[2] and b[3] >= w[1]:\n            w[1] = b[3]\n        if b[3] >= w[3] and b[2] >= w[0]:\n            w[0] = b[2]\n    elif b[2] >= w[2] and b[3] >= w[3]:\n        if b[1] <= w[1] and b[0] <= w[2]:\n            w[2] = b[0]\n        if b[0] <= w[0] and b[1] <= w[3]:\n            w[3] = b[1]\n\nflag = False\nif reduce(w, b1):\n    print(\"NO\")\n    flag = True\nelif not flag and reduce(w, b2):\n    print(\"NO\")\n    flag = True\nif not flag:\n    print(\"YES\")", "x1, y1, x2, y2 = map(int, input().split())\nx3, y3, x4, y4 = map(int, input().split())\nx5, y5, x6, y6 = map(int, input().split())\nif (y1 > y4 or y1 < y3 or x1 > x4 or x1 < x3) and (y1 < y5 or y1 > y6 or x1 < x5 or x1 > x6):\n    print('YES')\nelif (y2 > y4 or y2 < y3 or x4 < x2 or x2 < x3) and (y2 < y5 or y2 > y6 or x2 < x5 or x2 > x6):\n    print('YES')\nelif (y2 > y4 or y2 < y3 or x4 < x1 or x1 < x3) and (y2 < y5 or y2 > y6 or x1 < x5 or x1 > x6):\n    print(\"YES\")\nelif (y1 > y4 or y1 < y3 or x4 < x2 or x2 < x3) and (y1 < y5 or y1 > y6 or x2 < x5 or x2 > x6):\n    print(\"YES\")\nelif x5 > x4 and x1 < x5 < x2:\n    print(\"YES\")\nelif x6 < x3 and x1 < x6 < x2:\n    print(\"YES\")\nelif y6 < y3 and y1 < y6 < y2:\n    print('YES')\nelif y5 > y4 and y1 < y5 < y2:\n    print('YES')\nelse:\n    print('NO')", "ll = lambda:list(map(int, input().split()))\ntestcases = 1\n# testcases = ll()\nfor _ in range(testcases):\n\t[x1,y1,x2,y2] = ll()\n\t[x3,y3,x4,y4] = ll()\n\t[x5,y5,x6,y6] = ll()\n\tdef lies1(x0,y0):\n\t\treturn x0>=x3 and x0<=x4 and y0>=y3 and y0<=y4\n\tdef lies2(x0,y0):\n\t\t\n\t\treturn x0>=x5 and x0<=x6 and y0>=y5 and y0<=y6\n\tdef lies(x0,y0):\n\t\treturn lies1(x0,y0) or lies2(x0,y0)\n\n\tap = [[x1,y1],[x2,y2],[x1,y2],[x2,y1]]\n\tok = 1\n\tfor x in ap:\n\t\tif not (lies(x[0],x[1])):\n\t\t\tok = 0\n\t\t\tbreak\n\telse:\n\t\tif x1 >=max(x3,x5) and x2 <=min(x4,x6):\n\t\t\tif (y1<=y6 and y6<y3 and y3<=y2) or ((y1<=y4 and y4<y5 and y5<=y2)):\n\t\t\t\tok = 0\n\t\telse:\n\t\t\tif (x1<=x6 and x6<x3 and x3<=x2) or ((x1<=x4 and x4<x5 and x5<=x2)):\n\t\t\t\tok = 0\n\n\tif(ok):\n\t\tprint(\"NO\")\n\telse:\n\t\tprint(\"YES\")\n\n", "import sys\ninput = sys.stdin.readline\n\nx1,y1,x2,y2=list(map(int,input().split()))\nx3,y3,x4,y4=list(map(int,input().split()))\nx5,y5,x6,y6=list(map(int,input().split()))\n\ndef cut(x1,y1,x2,y2,x3,y3,x4,y4):\n    if x3<=x1 and x2<=x4:\n        if y3<=y1<=y4:\n            y1=min(y2,y4)\n\n        if y3<=y2<=y4:\n            y2=max(y1,y3)\n\n    if y3<=y1 and y2<=y4:\n        if x3<=x1<=x4:\n            x1=min(x2,x4)\n\n        if x3<=x2<=x4:\n            x2=max(x1,x3)\n\n    return x1,y1,x2,y2\n\nx1,y1,x2,y2=cut(x1,y1,x2,y2,x3,y3,x4,y4)\n\n#print(x1,y1,x2,y2)\n\nx1,y1,x2,y2=cut(x1,y1,x2,y2,x5,y5,x6,y6)\n\n#print(x1,y1,x2,y2)\n\nif x1==x2 or y1==y2:\n    print(\"NO\")\nelse:\n    print(\"YES\")\n\n    \n", "x1,y1,x2,y2 = list(map(int, input().split()))\nx3,y3,x4,y4 = list(map(int, input().split()))\nx5,y5,x6,y6 = list(map(int, input().split()))\nf = False\n\nif x3 <= x1 <= x4 and x3 <= x2 <= x4:\n    if y3 <= y1 <= y4 and y3 <= y2 <= y4:\n        f = True\n    elif y1 < y3 <= y2 <= y4:\n        y2 = y3\n    elif y3 <= y1 <= y4 < y2:\n        y1 = y4\n\nif y3 <= y1 <= y4 and y3 <= y2 <= y4:\n    if x3 <= x1 <= x4 and x3 <= x2 <= x4:\n        f = True\n    elif x1 < x3 <= x2 <= x4:\n        x2 = x3\n    elif x3 <= x1 <= x4 < x2:\n        x1 = x4    \n        \nif x5 <= x1 <= x6 and x5 <= x2 <= x6:\n    if y5 <= y1 <= y6 and y5 <= y2 <= y6:\n        f = True    \n    \nprint('NO' if f else 'YES')\n", "a=[*map(int,input().split())]\nb=[*map(int,input().split())]\nc=[*map(int,input().split())]\n\nab=[0]*4\nab[0] = max(a[0],b[0])\nab[2] = min(a[2],b[2])\nab[1] = max(a[1],b[1])\nab[3] = min(a[3],b[3])\n\n# print(ab)\nif ab==a:\n    print(\"NO\")\n    return\n\nac=[0]*4\nac[0] = max(a[0],c[0])\nac[2] = min(a[2],c[2])\nac[1] = max(a[1],c[1])\nac[3] = min(a[3],c[3])\n\n# print(ac)\nif ac==a:\n    print(\"NO\")\n    return\n\nif ab[0]>=ab[2] or ab[1]>=ab[3] or ac[0]>=ac[2] or ac[1]>=ac[3]:\n    print(\"YES\")\n    return\n\nabac=[0]*4\nabac[0] = max(ab[0],ac[0])\nabac[2] = min(ab[2],ac[2])\nabac[1] = max(ab[1],ac[1])\nabac[3] = min(ab[3],ac[3])\n\noo=(ab[2]-ab[0])*(ab[3]-ab[1])+(ac[2]-ac[0])*(ac[3]-ac[1])\nif abac[0]>=abac[2] or abac[1]>=abac[3]:\n    oo-=0\nelse:\n    oo-=(abac[2]-abac[0])*(abac[3]-abac[1])\n\nif oo>=(a[2]-a[0])*(a[3]-a[1]):\n    print(\"NO\")\nelse:\n    print(\"YES\")", "import itertools\n\nclass Rectangle:\n    def intersection(self, other):\n        a, b = self, other\n        x1 = max(min(a.x1, a.x2), min(b.x1, b.x2))\n        y1 = max(min(a.y1, a.y2), min(b.y1, b.y2))\n        x2 = min(max(a.x1, a.x2), max(b.x1, b.x2))\n        y2 = min(max(a.y1, a.y2), max(b.y1, b.y2))\n        if x1 < x2 and y1 < y2:\n            return type(self)(x1, y1, x2, y2)\n    __and__ = intersection\n\n    def difference(self, other):\n        inter = self & other\n        if not inter:\n            yield self\n            return\n        xs = {self.x1, self.x2}\n        ys = {self.y1, self.y2}\n        if self.x1 < other.x1 < self.x2: xs.add(other.x1)\n        if self.x1 < other.x2 < self.x2: xs.add(other.x2)\n        if self.y1 < other.y1 < self.y2: ys.add(other.y1)\n        if self.y1 < other.y2 < self.y2: ys.add(other.y2)\n        for (x1, x2), (y1, y2) in itertools.product(\n            pairwise(sorted(xs)), pairwise(sorted(ys))\n        ):\n            rect = type(self)(x1, y1, x2, y2)\n            if rect != inter:\n                yield rect\n    __sub__ = difference\n\n    def __init__(self, x1, y1, x2, y2):\n        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2\n\n    def __iter__(self):\n        yield self.x1\n        yield self.y1\n        yield self.x2\n        yield self.y2\n\n    def __eq__(self, other):\n        return isinstance(other, Rectangle) and tuple(self) == tuple(other)\n    def __ne__(self, other):\n        return not (self == other)\n\n\n\ndef pairwise(iterable):\n    a, b = itertools.tee(iterable)\n    next(b, None)\n    return list(zip(a, b))\n\n\nfirst_rect = Rectangle(*list([int(x) for x in input().split(' ')]))\nsecond_rect = Rectangle(*list([int(x) for x in input().split(' ')]))\nthird_rect = Rectangle(*list([int(x) for x in input().split(' ')]))\n\nfound = False\ndiff1 = first_rect - second_rect\nfor elem in diff1:\n    diff2 = elem - third_rect\n    for elem2 in diff2:\n        if elem2:\n            found = True\n\nprint('NO' if not found else 'YES')\n", "[x1, y1, x2, y2] = [int(x) for x in input().split()]\n[x3, y3, x4, y4] = [int(x) for x in input().split()]\n[x5, y5, x6, y6] = [int(x) for x in input().split()]\n\nno = 'NO'\nyes = 'YES'\n\ndef ries(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6):\n    if x3<=x1 and y3<=y1 and x4>=x2 and y4>=y2:\n        return(no)\n    if x5<=x1 and y5<=y1 and x6>=x2 and y6>=y2:\n        return(no)\n    if x3<=x1 and y3<=y1 and x4>=x5 and y4>=y2 and y5<=y1 and x6>=x2 and y6>=y2:\n        return(no)\n    if x5<=x1 and y5<=y1 and x6>=x3 and y6>=y2 and y3<=y1 and x4>=x2 and y4>=y2:\n        return(no)\n    if x3<=x1 and y3<=y1 and x4>=x2 and y4>=y5 and x5<=x1 and x6>=x2 and y6>=y2:\n        return(no)\n    if x5<=x1 and y5<=y1 and x6>=x2 and y6>=y3 and x3<=x1 and x4>=x2 and y4>=y2:\n        return(no)\n    return(yes)\n\nprint(ries(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6))\n\n", "a = [int(x) for x in input().split()]\nb = [int(x) for x in input().split()]\nc = [int(x) for x in input().split()]\nflag = 0\n\nif b[0] <= a[0] and b[1] <= a[1] and a[2] <= b[2] and a[3] <= b[3]:\n    flag = 1\nelif c[0] <= a[0] and c[1] <= a[1] and a[2] <= c[2] and a[3] <= c[3]:\n    flag = 1\nelse:\n    if b[0] <= a[0] and b[1] <= a[1]:\n        if a[2] <= c[2] and a[3] <= c[3]:\n            if a[3] <= b[3] and c[1] <= a[1] and c[0] <= b[2]:\n                flag = 1\n            elif a[2] <= b[2] and c[0] <= a[0] and c[1] <= b[3]:\n                flag = 1\n    elif c[0] <= a[0] and c[1] <= a[1]:\n        if a[2] <= b[2] and a[3] <= b[3]:\n            if a[3] <= c[3] and b[1] <= a[1] and b[0] <= c[2]:\n                flag = 1\n            elif a[2] <= c[2] and b[0] <= a[0] and b[1] <= c[3]:\n                flag = 1\n\nprint(\"YES\" if (flag == 0) else \"NO\")", "def intersect_area(x1, y1, x2, y2, x3, y3, x4, y4):\n    x_overlap1 = min(x2, x4) - max(x1, x3)\n    y_overlap1 = min(y2, y4) - max(y1, y3)\n    if x_overlap1 > 0 and y_overlap1 > 0:\n        return x_overlap1 * y_overlap1\n    return 0\n\n\nx1, y1, x2, y2 = map(int, input().split())\nx3, y3, x4, y4 = map(int, input().split())\nx5, y5, x6, y6 = map(int, input().split())\na = intersect_area(x1, y1, x2, y2, x3, y3, x4, y4)\nb = intersect_area(x1, y1, x2, y2, x5, y5, x6, y6)\nc = intersect_area(x1, y1, x2, y2, max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))\narea = (x2 - x1) * (y2 - y1)\nif area - (a + b - c) > 0:\n    print(\"YES\")\nelse:\n    print(\"NO\")", "i1 = input('').split(' ')\nx1 = int(i1[0])\ny1 = int(i1[1])\nx2 = int(i1[2])\ny2 = int(i1[3])\ni1 = input('').split(' ')\nx3 = int(i1[0])\ny3 = int(i1[1])\nx4 = int(i1[2])\ny4 = int(i1[3])\ni1 = input('').split(' ')\nx5 = int(i1[0])\ny5 = int(i1[1])\nx6 = int(i1[2])\ny6 = int(i1[3])\n\ndef chk(x1,y1,x2,y2,x3,y3):\n    if(x3 <= x2 and x3 >= x1 and y3 >= y1 and y3 <= y2):\n        return True\n    else:\n        return False\n\nr11 = chk(x3,y3,x4,y4,x1,y1)\nr12 = chk(x5,y5,x6,y6,x1,y1)\nr21 = chk(x3,y3,x4,y4,x2,y1)\nr22 = chk(x5,y5,x6,y6,x2,y1)\nr31 = chk(x3,y3,x4,y4,x1,y2)\nr32 = chk(x5,y5,x6,y6,x1,y2)\nr41 = chk(x3,y3,x4,y4,x2,y2)\nr42 = chk(x5,y5,x6,y6,x2,y2)\n\ndef car(x1,y1,x2,y2,x3,y3,x4,y4):\n    yy1 = max(y1,y3)\n    yy2 = min(y2,y4)\n    xx1 = max(x1,x3)\n    xx2 = min(x2,x4)\n    area = (abs(yy1 - yy2))*(abs(xx1 - xx2))\n    return area\n    \nif((r11 or r12) and (r21 or r22) and (r31 or r32) and (r41 or r42)):\n    a1 = car(x1,y1,x2,y2,x3,y3,x4,y4)\n    a2 = car(x1,y1,x2,y2,x5,y5,x6,y6)\n    ta = a1 + a2\n    if(ta >= (x2-x1)*(y2-y1)):\n        print('NO')\n    else:\n        print('YES')\nelse:\n    print('YES')\n", "def area(xmin, ymin, xmax, ymax):\n    dx = xmax - xmin\n    dy = ymax - ymin\n    if (dx >= 0) and (dy >= 0):\n        return dx * dy\n    else:\n        return 0\n\ndef intersect(a_xmin, a_ymin, a_xmax, a_ymax,\n            b_xmin, b_ymin, b_xmax, b_ymax):\n    xmax, xmin = min(a_xmax, b_xmax), max(a_xmin, b_xmin)\n    ymax, ymin = min(a_ymax, b_ymax), max(a_ymin, b_ymin)\n    return xmin, ymin, xmax, ymax    \n\na_xmin, a_ymin, a_xmax, a_ymax = list(map(int, input().split()))\nb_xmin, b_ymin, b_xmax, b_ymax = list(map(int, input().split()))\nc_xmin, c_ymin, c_xmax, c_ymax = list(map(int, input().split()))\n\ns1 = (a_xmax - a_xmin) * (a_ymax - a_ymin)\ns12_xmin, s12_ymin, s12_xmax, s12_ymax = intersect(\n    a_xmin, a_ymin, a_xmax, a_ymax,\n    b_xmin, b_ymin, b_xmax, b_ymax\n)\ns12 = area(s12_xmin, s12_ymin, s12_xmax, s12_ymax)\n\ns13_xmin, s13_ymin, s13_xmax, s13_ymax = intersect(\n    a_xmin, a_ymin, a_xmax, a_ymax,\n    c_xmin, c_ymin, c_xmax, c_ymax\n)\ns13 = area(s13_xmin, s13_ymin, s13_xmax, s13_ymax)\n\n\ns23_xmin, s23_ymin, s23_xmax, s23_ymax = intersect(\n    b_xmin, b_ymin, b_xmax, b_ymax,\n    c_xmin, c_ymin, c_xmax, c_ymax\n)\ns23 = area(s23_xmin, s23_ymin, s23_xmax, s23_ymax)\n\ns123_xmin, s123_ymin, s123_xmax, s123_ymax = intersect(\n    s13_xmin, s13_ymin, s13_xmax, s13_ymax,\n    s23_xmin, s23_ymin, s23_xmax, s23_ymax\n)\ns123 = area(s123_xmin, s123_ymin, s123_xmax, s123_ymax)\n\nprint(\"YES\" if s1 > s12 + s13 - s123 else \"NO\")", "x1,y1,x2,y2=list(map(int,input().split()))\nx3,y3,x4,y4=list(map(int,input().split()))\nx5,y5,x6,y6=list(map(int,input().split()))\nz=0\nif x3<=x1 and x4>=x2 and y3<=y1 and y4>=y2:\n    z=1\nif x5<=x1 and x6>=x2 and y5<=y1 and y6>=y2:\n    z=1\nif y3>y5:\n    if y3<=y6 and y4>=y2 and y5<=y1:\n        if x3<=x1 and x4>=x2 and x5<=x1 and x6>=x2:\n            z=1\nelse:\n    y3,y5=y5,y3\n    y6,y4=y4,y6\n    if y3<=y6 and y4>=y2 and y5<=y1:\n        if x3<=x1 and x4>=x2 and x5<=x1 and x6>=x2:\n            z=1\ny3,y5=y5,y3\ny6,y4=y4,y6\nif x3<x5:\n    if x3<=x1 and x4>=x5 and x6>=x2:\n        if y3<=y1 and y4>=y2 and y5<=y1 and y6>=y2:\n            z=1\nelse:\n    x3,x5=x5,x3\n    x6,x4=x4,x6\n    if x3<=x1 and x4>=x5 and x6>=x2:\n        if y3<=y1 and y4>=y2 and y5<=y1 and y6>=y2:\n            z=1\nif z==1:\n    print(\"NO\")\nelse:\n    print(\"YES\")\n    \n", "x=[]\n\nfor i in range(3):\n    a=list(map(int,input().split()))\n    x.append(a)\n\ndef ok(a,b,n):\n    nonlocal x\n    return x[n][0]<=a<=x[n][2] and x[n][1]<=b<=x[n][3]\n\n#a[0][0] a[0][1] : a[0][0] a[0][3] : a\n\ndef kol(n):\n    nonlocal x\n    t=0\n    x1=x[0][0]\n    y1=x[0][1]\n    x2=x[0][2]\n    y2=x[0][3]\n    if ok(x1,y1,n): t+=1\n    if ok(x1,y2,n): t+=1\n    if ok(x2,y1,n): t+=1\n    if ok(x2,y2,n): t+=1\n    return t\nk1=kol(1)\nk2=kol(2)\n\ndef ooo():\n    x1=x[0][0]\n    y1=x[0][1]\n    x2=x[0][2]\n    y2=x[0][3]\n    t=True\n    t=t and (ok(x1,y1,1) or ok(x1,y1,2))\n    t=t and (ok(x1,y2,1) or ok(x1,y2,2))\n    t=t and (ok(x2,y1,1) or ok(x2,y1,2))\n    t=t and (ok(x2,y2,1) or ok(x2,y2,2))\n    return t\n\n    \nif k1==4 or k2==4:\n    print('NO')\nelif k1+k2<4:\n    print('YES')\nelif not ooo():\n    print('YES')\nelse:\n    x1=x[0][0]\n    y1=x[0][1]\n    x2=x[0][2]\n    y2=x[0][3]\n    if ok(x1,y1,2):\n        x[1],x[2]=x[2],x[1]\n    if ok(x2,y1,1):\n        if x[1][3]>=x[2][1]:\n            print('NO')\n        else: print('YES')\n    else:\n        if x[1][2]>=x[2][0]:\n            print('NO')\n        else: print('YES')\n"]