["MOD=10**9+7\nn=int(input())\ns=[c=='(' for c in input()]\nm=len(s)\nz=[[0,0]]\nfor v in s:\n a=z[-1][v]\n z[-1][v]=len(z)\n z.append(z[a][:])\nz[m][0]=z[m][1]=m\ndp=[[0 for _ in range(m+1)] for _ in range(n+1)]\ndp[0][0]=1\nfor _ in range(2*n):\n ndp=[[0 for _ in range(m+1)] for _ in range(n+1)]\n for i in range(n+1):\n  for j in range(m+1):\n   if dp[i][j]<1:continue\n   if i>0:ndp[i-1][z[j][0]]=(ndp[i-1][z[j][0]]+dp[i][j])%MOD\n   if i<n:ndp[i+1][z[j][1]]=(ndp[i+1][z[j][1]]+dp[i][j])%MOD\n dp=ndp\nprint(dp[0][m])", "MOD=10**9+7\nn=int(input())\ns=[c=='(' for c in input()]\nm=len(s)\nz=[[0,0]]\nfor v in s:\n a=z[-1][v]\n z[-1][v]=len(z)\n z.append(z[a][:])\nz[m][0]=z[m][1]=m\ndp=[[0 for _ in range(m+1)] for _ in range(n+1)]\ndp[0][0]=1\nfor _ in range(2*n):\n ndp=[[0 for _ in range(m+1)] for _ in range(n+1)]\n for i in range(n+1):\n  for j in range(m+1):\n   if i>0:ndp[i-1][z[j][0]]=(ndp[i-1][z[j][0]]+dp[i][j])%MOD\n   if i<n:ndp[i+1][z[j][1]]=(ndp[i+1][z[j][1]]+dp[i][j])%MOD\n dp=ndp\nprint(dp[0][m])", "M=10**9+7\nn=int(input())\ns=[c=='(' for c in input()]\nm=len(s)\nz=[[0,0]]\nfor v in s:\n a=z[-1][v]\n z[-1][v]=len(z)\n z+=[z[a][:]]\nz[m]=[m,m]\ndp=[[0]*(m+1) for _ in range(n+1)]\ndp[0][0]=1\nfor _ in range(2*n):\n ndp=[[0]*(m+1) for _ in range(n+1)]\n for i in range(n+1):\n  for j in range(m+1):\n   if i>0:ndp[i-1][z[j][0]]=(ndp[i-1][z[j][0]]+dp[i][j])%M\n   if i<n:ndp[i+1][z[j][1]]=(ndp[i+1][z[j][1]]+dp[i][j])%M\n dp=ndp\nprint(dp[0][m])", "M=10**9+7\nn=int(input())\ns=[c=='(' for c in input()]\nm=len(s)\nz=[[0,0]]\nfor v in s:\n a=z[-1][v]\n z[-1][v]=len(z)\n z+=[z[a][:]]\nz[m]=[m,m]\ndp=[[0]*(m+1) for _ in range(n+1)]\ndp[0][0]=1\nfor _ in range(2*n):\n ndp=[[0]*(m+1) for _ in range(n+1)]\n for i in range(n+1):\n  for j in range(m+1):\n   if i>0:ndp[i-1][z[j][0]]=(ndp[i-1][z[j][0]]+dp[i][j])%M\n   if i<n:ndp[i+1][z[j][1]]=(ndp[i+1][z[j][1]]+dp[i][j])%M\n dp=ndp\n \nprint(dp[0][m])"]