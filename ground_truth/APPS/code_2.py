["def main():\n    s = input()\n    n = len(s)\n    t = int(str(int(s[0]) + 1) + '0' * (n - 1))\n\n    print(t - int(s))\n\nmain()\n", "s = input()\nx = int(s)\ny = int(str(int(s[0]) + 1) + '0' * (len(s) - 1))\nprint(y - x)", "n = int(input())\n\nfor i in range(0,11):\n    for j in range(1,10):\n        m = j*10**i\n        if (n<m) :\n            print(m-n)\n            return\n\n\n", "n = int(input())\ns = str(n)\ns = str(int(s[0]) + 1) + '0' * (len(s) - 1)\ns = int(s)\nprint(s - n)\n", "y = input()\nly = len(y)\niy = int(y)\ntd = iy/(10**(ly-1))\n#print(ly,iy,td)\nif(td == 9):\n    print(10**ly-iy)\nelse:\n    print((int(y[0])+1)*(10**(ly-1))-iy)", "N = input()\nprint((int(N[0])+1)*(10**(len(N)-1))-int(N))\n", "def solve(n):\n    if (n<10):\n        return 1\n    a = str(n)\n    b=int(a[1:])\n    return 10**(len(a)-1)-b\n    \n\n\nn = int(input())\nprint(solve(n))\n", "n = str(int(input())+1)\nif n.count(\"0\")+1 == len(n):\n    print(1)\nelse:\n    print((int(n[0])+1)*10**(len(n)-1)-int(n)+1)\n    \n", "import sys\nimport math\n\nn = int(input())\ns = n\nr = 1\nwhile n // 10  != 0:\n    n = n // 10\n    r *= 10 \nnext  = (s // r + 1) * r\nprint(next - s)", "n=(input())\ncur=int(n[0])\npre=str(cur+1)\nnext=pre+'0'*(len(n)-1)\nprint(int(next)-int(n))\n", "n = int(input())\nans = 0\nprev = 0\nN = n\nwhile n:\n\ta = n%10\n\tn //= 10\n\tans += 1\n\tprev = a\nif ans==1:\n\tprint(1)\nelse:\n\tprint(((prev+1)*(10**(ans-1)))-N)\n", "x=input()\nn=int(x)\nln=len(x)\ny=int(x[0])\ny+=1\ny=y*(10**(ln-1))\nprint(y-n)\n", "a=int(input())\nb=a\nnr=1\nwhile b>9:\n    nr*=10\n    b/=10\nprint(int(b+1)*int(nr)-int(a))", "t=input()\nl=len(t)\nprint((int(t[0:1])+1)*(10**(l-1))-int(t))\n\n", "def main():\n    n = input()\n    d = int(n[0])\n    if d < 9:\n        year = int(str(d + 1) + '0' * (len(n) - 1))\n    else:\n        year = int('1' + '0' * len(n))\n\n    print(year - int(n))\n\ndef __starting_point():\n    main()\n\n__starting_point()", "x = int(input())\na = x\nx += 1\nif len(str(x))-str(x).count('0') <= 1:\n    b = x;\nelse:\n    b = int(str(int(str(x)[0])+1)+'0'*(len(str(x))-1))\nprint(b-a)", "# -*- coding: utf-8 -*-\n\nimport sys\nimport os\nimport math\n\n# input_text_path = __file__.replace('.py', '.txt')\n# fd = os.open(input_text_path, os.O_RDONLY)\n# os.dup2(fd, sys.stdin.fileno())\n\nn = int(input())\n\nif n < 10:\n    print(1)\nelse:\n    s = str(n)\n    l = len(s)\n\n    v = 10 ** (l-1)\n    w = int(s[1:])\n\n    print(v - w)", "n = int(input())\nsize = len(str(n))\nnum = str(n)[0]\nres = (int(num) + 1) * 10 ** (size - 1) - n\nprint(res)\n", "def main():\n    NUMBERS = [str(i) for i in range(1, 10)]\n    num = input()\n    result = ''\n    if num in NUMBERS:\n        result = 1\n        return result\n    if len(num) == num.count('0') + 1:\n        result = int(str(int(num[0]) + 1) + num[1:]) - int(num)\n        return result\n    result = int(str(int(num[0]) + 1) + (len(num) - 1) * '0') - int(num)\n    return result\nprint(main())", "n=input()\ni=len(n)-1\nt=int(n[0])+1\nprint(10**i*t-int(n))", "n = int(input())\ny = 1\nd = 0\nwhile y <= n:\n    y += 10**d\n    if y // 10**(d + 1) == 1:\n        d += 1\nprint(y - n)\n\n", "import math\n\nn = int(input())\n\np10 = int(math.log10(n + 1))\np = pow(10, p10)\nyears = (int(n / p) + 1) * p - n\n\nprint(years)\n", "n = input()\ny = int(n)\n\nif y < 10:\n    print(1)\nelse:\n    l = len(n)\n    f = int(n[0]) + 1\n    f *= 10 ** (l - 1)\n    print(f - y)\n", "n = int(input())\ni = 1\ncur = n\nx = 1\nwhile cur > 0:\n    a = cur % 10\n    cur //= 10\n    x *= 10\nprint((a+1)*x//10 - n)"]